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
from registry import DEFAULT_REGISTRY_PATH, format_services, list_implemented, list_pending, load_registry, next_recommended, validate_services


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Executa o MVP da Omie Knowledge Factory.")
    parser.add_argument("--url", help="URL da documentacao oficial.")
    parser.add_argument("--output", default="factory/output", help="Diretorio de saida isolado.")
    parser.add_argument("--dry-run", action="store_true", help="Planeja sem gravar saidas de docs/datasets/rag/reports.")
    parser.add_argument("--service", help="Nome do servico quando a pagina nao possuir titulo claro.")
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY_PATH), help="Arquivo YAML do service registry.")
    parser.add_argument("--batch", action="store_true", help="Executa a Factory em lote a partir do registry.")
    parser.add_argument("--limit", type=int, help="Limite de servicos no batch.")
    parser.add_argument("--domain", help="Filtra por dominio do registry.")
    parser.add_argument("--priority", choices=["alta", "media", "baixa"], help="Filtra por prioridade.")
    parser.add_argument("--next", action="store_true", help="Mostra a proxima URL recomendada para documentacao.")
    parser.add_argument("--list-services", action="store_true", help="Lista todos os servicos do registry.")
    parser.add_argument("--list-pending", action="store_true", help="Lista servicos pendentes.")
    parser.add_argument("--list-implemented", action="store_true", help="Lista servicos implementados.")
    parser.add_argument("--plan", action="store_true", help="Gera o plano deterministico de documentacao.")
    parser.add_argument("--priority-report", action="store_true", help="Gera e imprime o caminho do relatorio de prioridades.")
    parser.add_argument("--dependency-graph", action="store_true", help="Gera e imprime o caminho do grafo de dependencias.")
    parser.add_argument("--next-best-service", action="store_true", help="Mostra o proximo melhor servico recomendado pelo planner.")
    parser.add_argument("--execute-next", action="store_true", help="Executa o proximo servico recomendado pelo planner.")
    parser.add_argument("--execute-service", help="Executa um servico especifico pelo ID do registry.")
    parser.add_argument("--resume", action="store_true", help="Retoma/libera execucao interrompida.")
    parser.add_argument("--status", action="store_true", help="Mostra o estado atual da Factory.")
    parser.add_argument("--history", action="store_true", help="Mostra o historico de execucoes.")
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
    registry_path = Path(args.registry)

    if args.execute_next or args.execute_service or args.resume or args.status or args.history:
        from execution_engine import execute_next, execute_service, get_history, get_status, resume_execution

        if args.status:
            print(get_status())
            return 0
        if args.history:
            print(get_history())
            return 0
        if args.resume:
            print(resume_execution())
            return 0
        if args.execute_next:
            result = execute_next(registry_path=registry_path, dry_run=args.dry_run)
        else:
            result = execute_service(args.execute_service, registry_path=registry_path, dry_run=args.dry_run)
        print(f"Execution Engine concluido: {result.service_id} status={result.status}")
        print("Relatorio: factory/reports/execution_report.md")
        return 0

    if args.plan or args.priority_report or args.dependency_graph or args.next_best_service:
        from planner import DEFAULT_REPORT_DIR, build_plan, format_next_best

        result = build_plan(registry_path=registry_path)
        if args.next_best_service:
            print(format_next_best(result))
            return 0
        if args.dependency_graph:
            print(DEFAULT_REPORT_DIR / "service_dependency_graph.md")
            return 0
        if args.priority_report:
            print(DEFAULT_REPORT_DIR / "planner_report.md")
            return 0
        print(DEFAULT_REPORT_DIR / "documentation_plan.md")
        return 0

    if args.list_services or args.list_pending or args.list_implemented or args.next:
        services = load_registry(registry_path)
        validate_services(services)
        if args.list_services:
            print(format_services(services))
            return 0
        if args.list_pending:
            print(format_services(list_pending(services, domain=args.domain)))
            return 0
        if args.list_implemented:
            print(format_services(list_implemented(services)))
            return 0
        recommended = next_recommended(services, domain=args.domain, priority=args.priority)
        if recommended is None:
            print("Nenhum servico pendente encontrado.")
            return 1
        print(recommended.documentation_url)
        return 0

    if args.batch:
        from batch_runner import run_batch

        result = run_batch(
            registry_path=registry_path,
            output_dir=Path(args.output),
            dry_run=args.dry_run,
            limit=args.limit,
            domain=args.domain,
            priority=args.priority,
        )
        print(f"Batch concluido. Servicos: {len(result.results)}")
        for item in result.results:
            print(f"{item.service_id}: {item.status}")
        print(f"Relatorio: {result.report_path}")
        return 0

    if not args.url:
        raise SystemExit("--url e obrigatorio quando nao usar comandos de registry ou batch.")
    result = run_pipeline(args.url, Path(args.output), dry_run=args.dry_run, service=args.service)
    mode = "dry-run" if result.dry_run else "geracao"
    print(f"Factory MVP concluida em modo {mode}.")
    print(f"Servico: {result.service.name}")
    print(f"Metodos: {len(result.service.methods)}")
    print(f"Arquivos: {len(result.generated_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
