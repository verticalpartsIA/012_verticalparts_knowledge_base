from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from execution_engine import (
    ExecutionError,
    execute_next,
    execute_service,
    get_history,
    get_status,
    load_state,
    resume_execution,
    save_state,
    validate_before_execution,
)
from main import main
from registry import load_registry


REGISTRY = Path("factory/registry/omie_services.yaml")


def paths(tmp_path: Path) -> dict[str, Path]:
    return {
        "state_path": tmp_path / "factory_state.json",
        "history_path": tmp_path / "execution_history.json",
        "report_path": tmp_path / "execution_report.md",
        "output_root": tmp_path / "output",
    }


def test_execute_next_dry_run_updates_state_history_and_report(tmp_path: Path) -> None:
    result = execute_next(registry_path=REGISTRY, dry_run=True, **paths(tmp_path))

    assert result.service_id == "financas_contas_a_pagar_lancamentos"
    assert result.status == "dry-run"
    assert result.generated_files
    state = load_state(tmp_path / "factory_state.json")
    assert state["last_service_executed"] == result.service_id
    assert result.service_id not in state["services_completed"]
    history = json.loads((tmp_path / "execution_history.json").read_text(encoding="utf-8"))
    assert history[-1]["service_id"] == result.service_id
    assert "Contas a Pagar" in (tmp_path / "execution_report.md").read_text(encoding="utf-8")


def test_execute_service_dry_run_by_id(tmp_path: Path) -> None:
    result = execute_service(
        "financas_contas_a_pagar_lancamentos",
        registry_path=REGISTRY,
        dry_run=True,
        **paths(tmp_path),
    )
    assert result.service_name == "Contas a Pagar - Lançamentos"
    assert result.quality_score == 1.0


def test_execution_blocks_unknown_completed_and_unresolved_services(tmp_path: Path) -> None:
    with pytest.raises(ExecutionError, match="Serviço inexistente"):
        execute_service("nao-existe", registry_path=REGISTRY, dry_run=True, **paths(tmp_path))

    services = load_registry(REGISTRY)
    completed_service = next(service for service in services if service.implemented)
    with pytest.raises(ExecutionError, match="Serviço já concluído"):
        validate_before_execution(completed_service, registry_path=REGISTRY, state_path=tmp_path / "state.json")

    pending_service = next(service for service in services if service.id == "financas_movimentos_financeiros")
    with pytest.raises(ExecutionError, match="Dependência não resolvida"):
        validate_before_execution(pending_service, registry_path=REGISTRY, state_path=tmp_path / "state2.json")

    duplicate_state = tmp_path / "duplicate_state.json"
    save_state({"status": "idle", "services_completed": ["financas_contas_a_pagar_lancamentos"]}, duplicate_state)
    duplicate_service = next(service for service in services if service.id == "financas_contas_a_pagar_lancamentos")
    with pytest.raises(ExecutionError, match="Execução duplicada bloqueada"):
        validate_before_execution(duplicate_service, registry_path=REGISTRY, state_path=duplicate_state)


def test_resume_status_and_history(tmp_path: Path) -> None:
    state_path = tmp_path / "factory_state.json"
    save_state({"status": "running", "current_service": "svc"}, state_path)
    assert "liberada" in resume_execution(state_path)
    assert "status=idle" in get_status(state_path)
    assert "Nenhuma execução" in get_history(tmp_path / "missing_history.json")


def test_cli_execution_commands(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--status"]) == 0
    assert "status=" in capsys.readouterr().out

    assert main(["--history"]) == 0
    assert "execução" in capsys.readouterr().out.lower() or "service_id" in capsys.readouterr().out
