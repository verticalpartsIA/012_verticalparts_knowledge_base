from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import crawler
from extract_methods import extract_methods
from generate_chunks import generate_chunks
from generate_documents import generate_documents
from generate_questions import generate_questions
from generate_reports import generate_reports
from main import ensure_output_structure, run_pipeline
from models import MethodInfo, ServiceInfo
from parser import parse_html


HTML = """
<html>
  <body>
    <h1>Clientes</h1>
    <p>Cadastro de clientes, fornecedores e transportadoras.</p>
    <h2>IncluirCliente</h2>
    <p>Inclui um cliente no cadastro.</p>
    <table>
      <tr><th>Campo</th><th>Tipo</th><th>Obrigatorio</th><th>Descricao</th></tr>
      <tr><td>codigo_cliente_integracao</td><td>string</td><td>Sim</td><td>Codigo interno</td></tr>
      <tr><td>razao_social</td><td>string</td><td>Nao</td><td>Razao social</td></tr>
    </table>
    <pre>{"call":"IncluirCliente","param":[{"codigo_cliente_integracao":"CLI-001"}]}</pre>
    <h2>ConsultarCliente</h2>
    <p>Consulta cliente cadastrado.</p>
  </body>
</html>
"""


def test_crawler_saves_cache(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(crawler, "fetch_html", lambda url, timeout=30: (HTML, 200))
    result = crawler.crawl("https://app.omie.com.br/api/v1/geral/clientes/", cache_dir=tmp_path)
    assert result.cache_path.exists()
    assert result.metadata_path.exists()
    assert json.loads(result.metadata_path.read_text(encoding="utf-8"))["status_code"] == 200


def test_parser_extracts_service_and_methods() -> None:
    service = parse_html(HTML, "https://app.omie.com.br/api/v1/geral/clientes/")
    methods = extract_methods(service)
    assert service.name == "Clientes"
    assert [method.name for method in methods] == ["ConsultarCliente", "IncluirCliente"]
    incluir = next(method for method in methods if method.name == "IncluirCliente")
    assert any(field.name == "codigo_cliente_integracao" and field.required for field in incluir.request_fields)


def test_generators_create_minimal_output(tmp_path: Path) -> None:
    service = parse_html(HTML, "https://app.omie.com.br/api/v1/geral/clientes/")
    files = []
    files.extend(ensure_output_structure(tmp_path))
    files.extend(generate_documents(service, tmp_path))
    files.extend(generate_questions(service, tmp_path))
    files.extend(generate_chunks(service, tmp_path))
    files.extend(generate_reports(service, tmp_path, files))

    assert (tmp_path / "docs").exists()
    assert (tmp_path / "schemas").exists()
    assert (tmp_path / "datasets" / "questions" / "clientes.json").exists()
    assert (tmp_path / "graphs").exists()
    assert (tmp_path / "business").exists()
    assert (tmp_path / "rag" / "chunks" / "clientes" / "index.json").exists()
    assert (tmp_path / "reports" / "dashboard.md").exists()
    assert (tmp_path / "coverage" / "omie_api_coverage.md").exists()
    assert (tmp_path / "reports" / "knowledge_score.md").exists()


def test_run_pipeline_dry_run(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(crawler, "fetch_html", lambda url, timeout=30: (HTML, 200))
    result = run_pipeline(
        "https://app.omie.com.br/api/v1/geral/clientes/",
        tmp_path,
        dry_run=True,
    )
    assert result.dry_run is True
    assert result.service.methods
    assert not (tmp_path / "docs").exists()


def test_method_file_slugs_are_unique_for_colliding_upsert_names(tmp_path: Path) -> None:
    service = ServiceInfo(
        name="Contas a Pagar - Lançamentos",
        endpoint="https://app.omie.com.br/api/v1/financas/contapagar/",
        domain="omie.financas",
        description="Servico financeiro.",
        source_url="https://app.omie.com.br/api/v1/financas/contapagar/",
        methods=(
            MethodInfo(
                name="Upsert",
                endpoint="https://app.omie.com.br/api/v1/financas/contapagar/",
                service="Contas a Pagar - Lançamentos",
                domain="omie.financas",
                description="Upsert do Contas a Pagar.",
            ),
            MethodInfo(
                name="UPSERT",
                endpoint="https://app.omie.com.br/api/v1/financas/contapagar/",
                service="Contas a Pagar - Lançamentos",
                domain="omie.financas",
                description="Efetua o UPSERT do Contas a Pagar por Lote.",
            ),
            MethodInfo(
                name="UpsertContaPagar",
                endpoint="https://app.omie.com.br/api/v1/financas/contapagar/",
                service="Contas a Pagar - Lançamentos",
                domain="omie.financas",
                description="Upsert do Contas a Pagar.",
            ),
        ),
    )

    document_files = [path for path in generate_documents(service, tmp_path, dry_run=True) if path.suffix == ".md"]
    chunk_files = [path for path in generate_chunks(service, tmp_path, dry_run=True) if path.suffix == ".md"]

    assert len(document_files) == len(set(document_files))
    assert len(chunk_files) == len(set(chunk_files))
