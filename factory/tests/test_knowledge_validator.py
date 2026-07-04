from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from knowledge_validator import (
    compare_scores,
    load_previous_scores,
    validate,
    write_improvement_report,
    write_quality_ranking,
)
from main import main


def test_validator_scores_documents_without_modifying_docs() -> None:
    result = validate(service_id="geral_clientes_fornecedores_transportadoras_etc", write_reports=False)

    assert result.documents
    assert result.average_score > 0
    assert all(0 <= item.score <= 100 for item in result.documents)
    assert all(item.path.as_posix().startswith("docs/omie") for item in result.documents)


def test_quality_ranking_and_improvement_report_are_generated() -> None:
    result = validate(write_reports=False)
    ranking = write_quality_ranking(result)
    improvement = write_improvement_report(result)

    assert ranking.exists()
    assert "Document Quality Ranking" in ranking.read_text(encoding="utf-8")
    assert improvement.exists()
    assert "Knowledge Improvement Report" in improvement.read_text(encoding="utf-8")


def test_regression_comparison_is_deterministic() -> None:
    assert compare_scores(80, 90) == "melhorou"
    assert compare_scores(90, 80) == "piorou"
    assert compare_scores(90, 90) == "igual"
    assert compare_scores(None, 90) == "sem baseline"
    assert load_previous_scores()


def test_validator_cli_commands(capsys) -> None:
    assert main(["--validate-service", "clientes"]) == 0
    assert "Knowledge Validation" in capsys.readouterr().out

    assert main(["--improvement-report"]) == 0
    assert "improvement_report.md" in capsys.readouterr().out

    assert main(["--quality-ranking"]) == 0
    assert "document_quality_ranking.md" in capsys.readouterr().out
