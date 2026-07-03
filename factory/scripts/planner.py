"""Generation Planner deterministico da Autonomous Knowledge Factory."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from registry import DEFAULT_REGISTRY_PATH, RegistryService, load_registry, validate_services


DEFAULT_PLANNER_CONFIG = Path("factory/config/planner.yaml")
DEFAULT_REPORT_DIR = Path("factory/reports")


@dataclass(frozen=True)
class PlannedService:
    service: RegistryService
    priority_score: int
    generation_order: int
    classification: str
    complexity: str
    estimated_duration: str
    dependencies: tuple[str, ...]
    dependencies_resolved: bool
    recommended_after: tuple[str, ...]
    recommended_before: tuple[str, ...]
    dependent_services_count: int
    has_existing_documentation: bool
    score_reasons: tuple[str, ...]


@dataclass(frozen=True)
class PlanResult:
    services: tuple[PlannedService, ...]
    next_best_service: PlannedService | None
    report_dir: Path


def load_config(path: Path = DEFAULT_PLANNER_CONFIG) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def build_plan(
    *,
    registry_path: Path = DEFAULT_REGISTRY_PATH,
    config_path: Path = DEFAULT_PLANNER_CONFIG,
    report_dir: Path = DEFAULT_REPORT_DIR,
    write_reports: bool = True,
) -> PlanResult:
    services = load_registry(registry_path)
    validate_services(services)
    config = load_config(config_path)
    dependencies_by_id = infer_dependencies(services, config)
    dependents_by_id = invert_dependencies(dependencies_by_id)
    implemented_ids = {service.id for service in services if service.implemented}

    scored: list[PlannedService] = []
    for service in services:
        dependencies = dependencies_by_id.get(service.id, ())
        dependencies_resolved = all(dependency in implemented_ids for dependency in dependencies)
        score, reasons = calculate_priority_score(
            service,
            dependencies=dependencies,
            dependencies_resolved=dependencies_resolved,
            dependent_services_count=len(dependents_by_id.get(service.id, ())),
            config=config,
        )
        classification = classify_score(score, config)
        complexity = calculate_complexity(service, classification)
        scored.append(
            PlannedService(
                service=service,
                priority_score=score,
                generation_order=0,
                classification=classification,
                complexity=complexity,
                estimated_duration=config["duration_by_complexity"].get(complexity, "1-2 dias"),
                dependencies=dependencies,
                dependencies_resolved=dependencies_resolved,
                recommended_after=dependencies,
                recommended_before=dependents_by_id.get(service.id, ()),
                dependent_services_count=len(dependents_by_id.get(service.id, ())),
                has_existing_documentation=service.implemented,
                score_reasons=tuple(reasons),
            )
        )

    ordered = assign_generation_order(scored)
    next_best = next((item for item in ordered if not item.service.implemented and item.dependencies_resolved), None)
    result = PlanResult(services=tuple(ordered), next_best_service=next_best, report_dir=report_dir)
    if write_reports:
        write_reports_for_plan(result, report_dir)
    return result


def infer_dependencies(services: list[RegistryService], config: dict[str, Any]) -> dict[str, tuple[str, ...]]:
    service_ids = {service.id for service in services}
    dependencies: dict[str, set[str]] = {service.id: set(service.depends_on) for service in services}
    rules = config.get("dependency_rules", {})
    for service in services:
        haystack = normalize(f"{service.name} {service.domain} {service.output_slug}")
        for keyword, dependency_ids in rules.items():
            if normalize(keyword) in haystack:
                for dependency_id in dependency_ids:
                    if dependency_id in service_ids and dependency_id != service.id:
                        dependencies[service.id].add(dependency_id)
    return {service_id: tuple(sorted(values)) for service_id, values in dependencies.items()}


def invert_dependencies(dependencies_by_id: dict[str, tuple[str, ...]]) -> dict[str, tuple[str, ...]]:
    dependents: dict[str, list[str]] = {}
    for service_id, dependencies in dependencies_by_id.items():
        for dependency in dependencies:
            dependents.setdefault(dependency, []).append(service_id)
    return {service_id: tuple(sorted(values)) for service_id, values in dependents.items()}


def calculate_priority_score(
    service: RegistryService,
    *,
    dependencies: tuple[str, ...],
    dependencies_resolved: bool,
    dependent_services_count: int,
    config: dict[str, Any],
) -> tuple[int, list[str]]:
    weights = config["weights"]
    reasons: list[str] = []
    score = 0

    registry_points = weights["registry_priority"].get(service.priority, 0)
    score += registry_points
    reasons.append(f"prioridade registry={registry_points}")

    domain_points = weights["domain"].get(service.domain, 0)
    score += domain_points
    reasons.append(f"dominio={domain_points}")

    status_points = weights["status"].get(service.status.lower(), 0)
    score += status_points
    reasons.append(f"status={status_points}")

    if service.implemented:
        score += weights["implemented_bonus"]
        score += weights["documented_penalty"]
        reasons.append("documentacao existente")
    else:
        score += weights["pending_bonus"]
        reasons.append("pendente de documentacao")

    if dependencies_resolved:
        score += weights["dependency_resolved_bonus"]
        reasons.append("dependencias resolvidas")
    elif dependencies:
        score += weights["dependency_blocked_penalty"]
        reasons.append("dependencias pendentes")

    if isinstance(service.methods_count, int):
        method_points = min(service.methods_count, 20) // 3 + weights["methods_known_bonus"]
        score += method_points
        reasons.append(f"metodos conhecidos={method_points}")

    dependent_points = dependent_services_count * weights["dependent_service_factor"]
    score += dependent_points
    if dependent_points:
        reasons.append(f"servicos dependentes={dependent_points}")

    financial_points = calculate_keyword_points(service, config.get("financial_keywords", []), 10)
    score += financial_points
    if financial_points:
        reasons.append(f"criticidade financeira={financial_points}")

    erp_points = calculate_erp_impact(service, config)
    score += erp_points
    if erp_points:
        reasons.append(f"impacto ERP={erp_points}")

    coverage_points = 8 if not service.implemented else 0
    score += coverage_points
    if coverage_points:
        reasons.append("lacuna de cobertura")

    return max(0, score), reasons


def calculate_keyword_points(service: RegistryService, keywords: list[str], points: int) -> int:
    haystack = normalize(f"{service.name} {service.domain} {service.output_slug}")
    return points if any(normalize(keyword) in haystack for keyword in keywords) else 0


def calculate_erp_impact(service: RegistryService, config: dict[str, Any]) -> int:
    haystack = normalize(f"{service.name} {service.domain} {service.output_slug}")
    impact_rules = config.get("erp_impact_keywords", {})
    if any(normalize(keyword) in haystack for keyword in impact_rules.get("critical", [])):
        return 16
    if any(normalize(keyword) in haystack for keyword in impact_rules.get("high", [])):
        return 11
    if any(normalize(keyword) in haystack for keyword in impact_rules.get("medium", [])):
        return 6
    return 0


def classify_score(score: int, config: dict[str, Any]) -> str:
    thresholds = config["classification_thresholds"]
    if score >= thresholds["critical"]:
        return "Critical"
    if score >= thresholds["high"]:
        return "High"
    if score >= thresholds["medium"]:
        return "Medium"
    return "Low"


def calculate_complexity(service: RegistryService, classification: str) -> str:
    if isinstance(service.methods_count, int):
        if service.methods_count >= 15:
            return "Critical"
        if service.methods_count >= 8:
            return "High"
        if service.methods_count >= 4:
            return "Medium"
        return "Low"
    if classification in {"Critical", "High"}:
        return "High"
    if classification == "Medium":
        return "Medium"
    return "Low"


def assign_generation_order(scored: list[PlannedService]) -> list[PlannedService]:
    ordered = sorted(
        scored,
        key=lambda item: (
            not item.service.implemented,
            not item.dependencies_resolved,
            -item.priority_score,
            item.service.id,
        ),
    )
    result: list[PlannedService] = []
    for index, item in enumerate(ordered, start=1):
        result.append(
            PlannedService(
                service=item.service,
                priority_score=item.priority_score,
                generation_order=index,
                classification=item.classification,
                complexity=item.complexity,
                estimated_duration=item.estimated_duration,
                dependencies=item.dependencies,
                dependencies_resolved=item.dependencies_resolved,
                recommended_after=item.recommended_after,
                recommended_before=item.recommended_before,
                dependent_services_count=item.dependent_services_count,
                has_existing_documentation=item.has_existing_documentation,
                score_reasons=item.score_reasons,
            )
        )
    return result


def write_reports_for_plan(result: PlanResult, report_dir: Path = DEFAULT_REPORT_DIR) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "planner_report.md").write_text(render_priority_report(result), encoding="utf-8")
    (report_dir / "documentation_plan.md").write_text(render_documentation_plan(result), encoding="utf-8")
    (report_dir / "service_dependency_graph.md").write_text(render_dependency_graph(result), encoding="utf-8")


def render_priority_report(result: PlanResult) -> str:
    lines = [
        "# Generation Planner Report",
        "",
        "| Ordem | Serviço | Score | Classe | Complexidade | Dependências resolvidas | Duração |",
        "|---:|---|---:|---|---|---|---|",
    ]
    for item in result.services:
        lines.append(
            f"| {item.generation_order} | {item.service.name} | {item.priority_score} | {item.classification} | {item.complexity} | {item.dependencies_resolved} | {item.estimated_duration} |"
        )
    if result.next_best_service:
        lines.extend(["", "## Próximo melhor serviço", "", f"- {result.next_best_service.service.name}"])
    return "\n".join(lines) + "\n"


def render_documentation_plan(result: PlanResult) -> str:
    lines = ["# Documentation Plan", ""]
    for item in result.services:
        lines.append(f"{item.generation_order:02d} {item.service.name}")
        lines.append(f"- Score: {item.priority_score}")
        lines.append(f"- Classificação: {item.classification}")
        lines.append(f"- Duração estimada: {item.estimated_duration}")
        lines.append("")
    return "\n".join(lines)


def render_dependency_graph(result: PlanResult) -> str:
    by_id = {item.service.id: item.service.name for item in result.services}
    lines = ["# Service Dependency Graph", "", "```mermaid", "graph TD"]
    for item in result.services:
        node_id = mermaid_id(item.service.id)
        lines.append(f'  {node_id}["{escape_mermaid(item.service.name)}"]')
        for dependency in item.dependencies:
            if dependency in by_id:
                lines.append(f"  {mermaid_id(dependency)} --> {node_id}")
    lines.append("```")
    return "\n".join(lines) + "\n"


def format_next_best(result: PlanResult) -> str:
    if not result.next_best_service:
        return "Nenhum serviço pendente com dependências resolvidas."
    item = result.next_best_service
    return (
        f"{item.service.id} | {item.service.name} | score={item.priority_score} | "
        f"classificacao={item.classification} | url={item.service.documentation_url}"
    )


def normalize(value: str) -> str:
    import unicodedata

    normalized = unicodedata.normalize("NFKD", value)
    return normalized.encode("ascii", "ignore").decode("ascii").lower()


def mermaid_id(value: str) -> str:
    return "svc_" + "".join(ch if ch.isalnum() else "_" for ch in value)


def escape_mermaid(value: str) -> str:
    return value.replace('"', "'")
