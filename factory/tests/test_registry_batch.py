from __future__ import annotations

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import json

from batch_runner import run_batch, select_services
from main import main
from registry import RegistryError, load_registry, list_implemented, list_pending, next_recommended, registry_health, validate_services


REGISTRY = Path("factory/registry/omie_services.yaml")


def test_registry_yaml_valid_and_required_fields() -> None:
    services = load_registry(REGISTRY)
    validate_services(services)
    assert len(services) == 137
    assert all(service.id and service.documentation_url for service in services)
    health = registry_health(services)
    assert health.healthy
    assert health.total_services == 137


def test_registry_filters_and_next_service() -> None:
    services = load_registry(REGISTRY)
    implemented = list_implemented(services)
    pending_financeiro = list_pending(services, domain="finanças")
    recommended = next_recommended(services)

    assert len(implemented) == 2
    assert pending_financeiro
    assert recommended is not None
    assert recommended.implemented is False
    assert recommended.priority in {"alta", "media", "baixa"}


def test_batch_dry_run_with_filters() -> None:
    services = load_registry(REGISTRY)
    selected = select_services(services, domain="finanças", priority="alta", limit=2)
    result = run_batch(registry_path=REGISTRY, dry_run=True, limit=2, domain="finanças", priority="alta")

    assert len(selected) <= 2
    assert result.dry_run is True
    assert len(result.results) == len(selected)
    assert all(item.status == "planned" for item in result.results)
    assert (result.run_dir / "run_summary.md").exists()
    assert (result.run_dir / "services_processed.json").exists()
    assert (result.run_dir / "services_failed.json").exists()
    assert (result.run_dir / "dry_run_report.md").exists()
    assert result.manifest_path.exists()


def test_cli_registry_commands(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--list-services"]) == 0
    assert "clientes" in capsys.readouterr().out.lower()

    assert main(["--list-pending", "--domain", "finanças"]) == 0
    assert "finanças" in capsys.readouterr().out.lower()

    assert main(["--next"]) == 0
    assert "https://app.omie.com.br/api/v1/" in capsys.readouterr().out

    assert main(["--batch", "--limit", "2", "--dry-run"]) == 0
    assert "Batch concluido. Servicos: 2" in capsys.readouterr().out


def test_service_id_output_root_and_manifest(tmp_path: Path) -> None:
    result = run_batch(
        registry_path=REGISTRY,
        output_root=tmp_path,
        dry_run=True,
        service_id="omie-financeiro-contas-pagar",
    )
    assert len(result.results) == 1
    assert result.results[0].service_id == "omie-financeiro-contas-pagar"
    manifest = json.loads(result.manifest_path.read_text(encoding="utf-8"))
    assert manifest[0]["service_id"] == "omie-financeiro-contas-pagar"


def test_no_write_executes_planning_without_final_writes(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    import crawler

    html = """
    <html><body>
      <h1>ContasPagar</h1>
      <h2>IncluirContaPagar</h2>
      <p>Inclui conta a pagar.</p>
    </body></html>
    """
    monkeypatch.setattr(crawler, "fetch_html", lambda url, timeout=30: (html, 200))
    result = run_batch(
        registry_path=REGISTRY,
        output_root=tmp_path,
        no_write=True,
        service_id="omie-financeiro-contas-pagar",
    )
    assert result.no_write is True
    assert result.results[0].status == "planned_no_write"
    assert result.results[0].planned_files > 0
    assert not any((result.run_dir / "generated").rglob("*.md"))


def test_missing_service_id_raises_controlled_error() -> None:
    with pytest.raises(RegistryError, match="service-id nao encontrado"):
        run_batch(registry_path=REGISTRY, dry_run=True, service_id="servico-inexistente")
