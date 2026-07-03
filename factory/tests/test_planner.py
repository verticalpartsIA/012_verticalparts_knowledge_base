from __future__ import annotations

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from main import main
from planner import build_plan, infer_dependencies, load_config
from registry import load_registry


REGISTRY = Path("factory/registry/omie_services.yaml")


def test_planner_generates_scores_and_order() -> None:
    result = build_plan(registry_path=REGISTRY, write_reports=False)
    assert len(result.services) == 137
    assert result.services[0].generation_order == 1
    assert all(item.priority_score >= 0 for item in result.services)
    assert {item.classification for item in result.services} <= {"Critical", "High", "Medium", "Low"}


def test_planner_resolves_dependencies_for_finance_services() -> None:
    result = build_plan(registry_path=REGISTRY, write_reports=False)
    by_id = {item.service.id: item for item in result.services}
    contas_pagar = by_id["financas_contas_a_pagar_lancamentos"]
    assert "geral_clientes_fornecedores_transportadoras_etc" in contas_pagar.dependencies
    assert contas_pagar.dependencies_resolved is True


def test_planner_orders_foundation_before_pending_services() -> None:
    result = build_plan(registry_path=REGISTRY, write_reports=False)
    by_id = {item.service.id: item for item in result.services}
    assert by_id["geral_clientes_fornecedores_transportadoras_etc"].generation_order < by_id["financas_contas_a_pagar_lancamentos"].generation_order
    assert result.next_best_service is not None
    assert result.next_best_service.service.implemented is False
    assert result.next_best_service.dependencies_resolved is True


def test_dependency_inference_is_deterministic() -> None:
    services = load_registry(REGISTRY)
    config = load_config()
    deps_first = infer_dependencies(services, config)
    deps_second = infer_dependencies(services, config)
    assert deps_first == deps_second


def test_planner_cli_commands(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--plan"]) == 0
    assert "documentation_plan.md" in capsys.readouterr().out

    assert main(["--priority-report"]) == 0
    assert "planner_report.md" in capsys.readouterr().out

    assert main(["--dependency-graph"]) == 0
    assert "service_dependency_graph.md" in capsys.readouterr().out

    assert main(["--next-best-service"]) == 0
    assert "score=" in capsys.readouterr().out
