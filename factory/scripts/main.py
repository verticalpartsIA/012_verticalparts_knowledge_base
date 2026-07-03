"""CLI da Omie Knowledge Factory MVP."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from crawler import crawl
from extract_methods import extract_methods
from generate_chunks import generate_chunks
from generate_documents import generate_documents
from generate_questions import generate_questions
from generate_reports import generate_reports
from models import FactoryResult, ServiceInfo
from parser import parse_html


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Executa o MVP da Omie Knowledge Factory.")
    parser.add_argument("--url", required=True, help="URL da documentacao oficial.")
    parser.add_argument("--output", default="factory/output", help="Diretorio de saida isolado.")
    parser.add_argument("--dry-run", action="store_true", help="Planeja sem gravar saidas de docs/datasets/rag/reports.")
    parser.add_argument("--service", help="Nome do servico quando a pagina nao possuir titulo claro.")
    return parser


def run_pipeline(url: str, output: Path, dry_run: bool = False, service: str | None = None) -> FactoryResult:
    crawl_result = crawl(url)
    parsed_service = parse_html(crawl_result.html, url, service_name=service)
    methods = extract_methods(parsed_service)
    service_info = ServiceInfo(
        name=parsed_service.name,
        endpoint=parsed_service.endpoint,
        domain=parsed_service.domain,
        description=parsed_service.description,
        source_url=parsed_service.source_url,
        methods=methods,
    )

    generated: list[Path] = []
    ensure_output_structure(output, dry_run=dry_run)
    generated.extend(generate_documents(service_info, output, dry_run=dry_run))
    generated.extend(generate_questions(service_info, output, dry_run=dry_run))
    generated.extend(generate_chunks(service_info, output, dry_run=dry_run))
    generated.extend(generate_reports(service_info, output, generated, dry_run=dry_run))
    return FactoryResult(service=service_info, output_dir=output, generated_files=tuple(generated), dry_run=dry_run)


def ensure_output_structure(output: Path, dry_run: bool = False) -> list[Path]:
    roots = ["docs", "schemas", "datasets", "graphs", "business", "rag", "reports", "coverage"]
    paths = [output / root for root in roots]
    if not dry_run:
        for path in paths:
            path.mkdir(parents=True, exist_ok=True)
    return paths


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run_pipeline(args.url, Path(args.output), dry_run=args.dry_run, service=args.service)
    mode = "dry-run" if result.dry_run else "geracao"
    print(f"Factory MVP concluida em modo {mode}.")
    print(f"Servico: {result.service.name}")
    print(f"Metodos: {len(result.service.methods)}")
    print(f"Arquivos: {len(result.generated_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
