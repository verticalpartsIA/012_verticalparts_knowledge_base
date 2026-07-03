from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

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


def registry_with_contas_pagar_pending(tmp_path: Path) -> Path:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    for service in data["services"]:
        if service["id"] == "financas_contas_a_pagar_lancamentos":
            service["status"] = "Planejado"
            service["implemented"] = False
            service["methods_count"] = None
    path = tmp_path / "omie_services.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return path


def test_execute_next_dry_run_updates_state_history_and_report(tmp_path: Path) -> None:
    registry = registry_with_contas_pagar_pending(tmp_path)
    result = execute_next(registry_path=registry, dry_run=True, **paths(tmp_path))

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
    registry = registry_with_contas_pagar_pending(tmp_path)
    result = execute_service(
        "financas_contas_a_pagar_lancamentos",
        registry_path=registry,
        dry_run=True,
        **paths(tmp_path),
    )
    assert result.service_name == "Contas a Pagar - Lançamentos"
    assert result.quality_score == 1.0

    alias_result = execute_service(
        "omie-financeiro-contas-pagar",
        registry_path=registry,
        dry_run=True,
        **paths(tmp_path / "alias"),
    )
    assert alias_result.service_id == "financas_contas_a_pagar_lancamentos"


def test_execute_service_no_write_uses_output_root_without_final_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry = registry_with_contas_pagar_pending(tmp_path)
    output_root = tmp_path / "runs" / "first-autonomous-cycle"

    def fake_run_pipeline(url: str, output: Path, dry_run: bool = False, service: str | None = None) -> SimpleNamespace:
        assert dry_run is True
        return SimpleNamespace(generated_files=(output / "docs" / "planned.md", output / "reports" / "dashboard.md"))

    monkeypatch.setattr("main.run_pipeline", fake_run_pipeline)
    result = execute_service(
        "omie-financeiro-contas-pagar",
        registry_path=registry,
        no_write=True,
        output_root=output_root,
        **{key: value for key, value in paths(tmp_path).items() if key != "output_root"},
    )

    assert result.status == "no-write"
    assert result.no_write is True
    assert result.generated_files
    assert all(str(path).replace("\\", "/").startswith(str(output_root).replace("\\", "/")) for path in result.generated_files)
    assert not (output_root / "contas_a_pagar_lancamentos" / "docs").exists()


def test_execution_blocks_unknown_completed_and_unresolved_services(tmp_path: Path) -> None:
    with pytest.raises(ExecutionError, match="Serviço inexistente"):
        execute_service("nao-existe", registry_path=REGISTRY, dry_run=True, **paths(tmp_path))

    services = load_registry(REGISTRY)
    completed_service = next(service for service in services if service.implemented)
    with pytest.raises(ExecutionError, match="Serviço já concluído"):
        validate_before_execution(completed_service, registry_path=REGISTRY, state_path=tmp_path / "state.json")

    pending_service = next(service for service in services if service.id == "geral_produtos")
    with pytest.raises(ExecutionError, match="Dependência não resolvida"):
        validate_before_execution(pending_service, registry_path=REGISTRY, state_path=tmp_path / "state2.json")

    duplicate_state = tmp_path / "duplicate_state.json"
    save_state({"status": "idle", "services_completed": ["financas_contas_a_pagar_lancamentos"]}, duplicate_state)
    duplicate_registry = registry_with_contas_pagar_pending(tmp_path / "duplicate")
    duplicate_service = next(
        service for service in load_registry(duplicate_registry) if service.id == "financas_contas_a_pagar_lancamentos"
    )
    with pytest.raises(ExecutionError, match="Execução duplicada bloqueada"):
        validate_before_execution(duplicate_service, registry_path=duplicate_registry, state_path=duplicate_state)


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
    history_output = capsys.readouterr().out
    assert "execução" in history_output.lower() or "service_id" in history_output
