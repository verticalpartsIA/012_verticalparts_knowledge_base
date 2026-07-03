from __future__ import annotations

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from batch_runner import run_batch, select_services
from main import main
from registry import load_registry, list_implemented, list_pending, next_recommended, validate_services


REGISTRY = Path("factory/registry/omie_services.yaml")


def test_registry_yaml_valid_and_required_fields() -> None:
    services = load_registry(REGISTRY)
    validate_services(services)
    assert len(services) == 137
    assert all(service.id and service.documentation_url for service in services)


def test_registry_filters_and_next_service() -> None:
    services = load_registry(REGISTRY)
    implemented = list_implemented(services)
    pending_financeiro = list_pending(services, domain="finanças")
    recommended = next_recommended(services)

    assert len(implemented) == 3
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


def test_cli_registry_commands(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--list-services"]) == 0
    assert "clientes" in capsys.readouterr().out.lower()

    assert main(["--list-pending", "--domain", "finanças"]) == 0
    assert "finanças" in capsys.readouterr().out.lower()

    assert main(["--next"]) == 0
    assert "https://app.omie.com.br/api/v1/" in capsys.readouterr().out

    assert main(["--batch", "--limit", "2", "--dry-run"]) == 0
    assert "Batch concluido. Servicos: 2" in capsys.readouterr().out
