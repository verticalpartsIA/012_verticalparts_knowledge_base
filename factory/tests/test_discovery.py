from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import discovery
from main import main


HTML = """
<html><body>
<table class="table">
  <tr class="active api-categ">
    <td colspan="4"><strong>Geral</strong><p>Cadastros compartilhados.</p></td>
  </tr>
  <tr class="row api-item">
    <td><a class="step1" href="https://app.omie.com.br/api/v1/geral/clientes/">Clientes</a></td>
    <td>Cadastro de clientes.</td><td><code>v1</code></td>
  </tr>
  <tr class="active api-categ">
    <td colspan="4"><strong>Finanças</strong><p>Serviços financeiros.</p></td>
  </tr>
  <tr class="row api-item">
    <td><a class="step1" href="https://app.omie.com.br/api/v1/financas/contapagar/">Contas a Pagar</a></td>
    <td>Lançamentos de contas a pagar.</td><td><code>v1</code></td>
  </tr>
</table>
</body></html>
"""


def test_parse_service_list_extracts_services() -> None:
    services = discovery.parse_service_list(HTML)
    assert len(services) == 2
    assert services[0].name == "Clientes"
    assert services[0].category == "Geral"
    assert services[0].domain == "geral"
    assert services[1].documentation_url == "https://app.omie.com.br/api/v1/financas/contapagar/"


def test_compare_registry_detects_new_removed_and_changed() -> None:
    current = [
        {
            "name": "Clientes Antigo",
            "domain": "geral",
            "description": "Descricao antiga",
            "documentation_url": "https://app.omie.com.br/api/v1/geral/clientes/",
        },
        {
            "name": "Removido",
            "documentation_url": "https://app.omie.com.br/api/v1/geral/removido/",
        },
    ]
    discovered = discovery.parse_service_list(HTML)
    comparison = discovery.compare_registry(current, discovered)
    assert len(comparison.new_services) == 1
    assert len(comparison.removed_services) == 1
    assert comparison.changed_services


def test_discover_services_writes_generated_registry_and_report(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    official = tmp_path / "omie_services.yaml"
    generated = tmp_path / "omie_services.generated.yaml"
    report = tmp_path / "discovery_report.md"
    official.write_text("services: []\n", encoding="utf-8")
    monkeypatch.setattr(discovery, "fetch_service_list", lambda source_url: HTML)

    services, comparison = discovery.discover_services(
        official_registry=official,
        generated_registry=generated,
        report_path=report,
    )

    data = yaml.safe_load(generated.read_text(encoding="utf-8"))
    assert len(services) == 2
    assert data["service_count"] == 2
    assert data["generator_version"] == discovery.GENERATOR_VERSION
    assert data["source"] == discovery.SOURCE_URL
    assert data["hash"]
    assert len(comparison.new_services) == 2
    assert "Serviços encontrados" in report.read_text(encoding="utf-8")


def test_cli_discover_compare_does_not_modify_official_registry(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    official = tmp_path / "official.yaml"
    generated = tmp_path / "generated.yaml"
    report = tmp_path / "report.md"
    official.write_text("services: []\n", encoding="utf-8")
    before = official.read_text(encoding="utf-8")
    monkeypatch.setattr(discovery, "DEFAULT_GENERATED_REGISTRY", generated)
    monkeypatch.setattr(discovery, "DEFAULT_DISCOVERY_REPORT", report)
    monkeypatch.setattr(discovery, "fetch_service_list", lambda source_url: HTML)

    assert main(["--discover", "--registry", str(official)]) == 0
    assert official.read_text(encoding="utf-8") == before
    assert generated.exists()
    assert main(["--compare-registry", "--registry", str(official)]) == 0
    assert report.exists()
