"""Execution Engine deterministico da Autonomous Knowledge Factory."""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

from planner import build_plan
from registry import RegistryService, load_registry, validate_services


ENGINE_VERSION = "0.7.0"
DEFAULT_STATE_PATH = Path("factory/state/factory_state.json")
DEFAULT_HISTORY_PATH = Path("factory/reports/execution_history.json")
DEFAULT_REPORT_PATH = Path("factory/reports/execution_report.md")
DEFAULT_OUTPUT_ROOT = Path("factory/output/execution")
SERVICE_ID_ALIASES = {
    "omie-financeiro-contas-pagar": "financas_contas_a_pagar_lancamentos",
}


@dataclass(frozen=True)
class ExecutionResult:
    service_id: str
    service_name: str
    status: str
    started_at: str
    finished_at: str
    duration_seconds: float
    generated_files: tuple[str, ...]
    warnings: tuple[str, ...]
    errors: tuple[str, ...]
    quality_score: float
    documentation_hash: str
    dry_run: bool
    no_write: bool = False


class ExecutionError(RuntimeError):
    """Erro controlado do Execution Engine."""


def empty_state() -> dict:
    return {
        "last_service_executed": None,
        "last_execution": None,
        "last_version": ENGINE_VERSION,
        "last_planner": None,
        "services_completed": [],
        "services_pending": [],
        "services_failed": [],
        "services_ignored": [],
        "average_duration_seconds": 0.0,
        "documentation_hash": None,
        "status": "idle",
        "current_service": None,
    }


def load_state(path: Path = DEFAULT_STATE_PATH) -> dict:
    if not path.exists():
        return empty_state()
    data = json.loads(path.read_text(encoding="utf-8"))
    return {**empty_state(), **data}


def save_state(state: dict, path: Path = DEFAULT_STATE_PATH) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def load_history(path: Path = DEFAULT_HISTORY_PATH) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_history(history: list[dict], path: Path = DEFAULT_HISTORY_PATH) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def get_status(state_path: Path = DEFAULT_STATE_PATH) -> str:
    state = load_state(state_path)
    return (
        f"status={state['status']} | last_service={state['last_service_executed']} | "
        f"last_execution={state['last_execution']} | failed={len(state['services_failed'])}"
    )


def get_history(history_path: Path = DEFAULT_HISTORY_PATH) -> str:
    history = load_history(history_path)
    if not history:
        return "Nenhuma execução registrada."
    lines = ["service_id | status | started_at | duration_seconds", "--- | --- | --- | ---:"]
    lines.extend(
        f"{item['service_id']} | {item['status']} | {item['started_at']} | {item['duration_seconds']}"
        for item in history[-20:]
    )
    return "\n".join(lines)


def validate_before_execution(
    service: RegistryService,
    *,
    registry_path: Path,
    state_path: Path = DEFAULT_STATE_PATH,
) -> list[str]:
    services = load_registry(registry_path)
    validate_services(services)
    known_ids = {item.id for item in services}
    if service.id not in known_ids:
        raise ExecutionError(f"Serviço inexistente: {service.id}")
    if service.implemented:
        raise ExecutionError(f"Serviço já concluído: {service.id}")
    state = load_state(state_path)
    if state["status"] == "running":
        raise ExecutionError(f"Execução já em andamento: {state['current_service']}")
    if service.id in state.get("services_completed", []):
        raise ExecutionError(f"Execução duplicada bloqueada: {service.id}")

    plan = build_plan(registry_path=registry_path, write_reports=False)
    planned = {item.service.id: item for item in plan.services}
    planned_service = planned.get(service.id)
    if not planned_service:
        raise ExecutionError(f"Planner desatualizado: {service.id} não está no plano")
    if not planned_service.dependencies_resolved:
        raise ExecutionError(f"Dependência não resolvida para: {service.id}")
    return validate_quality_inputs()


def validate_quality_inputs() -> list[str]:
    warnings = []
    required = [
        Path("coverage/omie_api_coverage.md"),
        Path("reports/dashboard.md"),
        Path("reports/knowledge_score.md"),
    ]
    for path in required:
        if not path.exists():
            warnings.append(f"Arquivo de qualidade ausente: {path}")
    return warnings


def validate_after_execution(result: ExecutionResult) -> list[str]:
    warnings = []
    if result.status == "success" and not result.generated_files and not result.dry_run:
        warnings.append("Execução sem arquivos gerados.")
    if result.quality_score < 1:
        warnings.append("Quality score abaixo do mínimo.")
    return warnings


def execute_next(
    *,
    registry_path: Path = Path("factory/registry/omie_services.yaml"),
    dry_run: bool = False,
    no_write: bool = False,
    state_path: Path = DEFAULT_STATE_PATH,
    history_path: Path = DEFAULT_HISTORY_PATH,
    report_path: Path = DEFAULT_REPORT_PATH,
    output_root: Path = DEFAULT_OUTPUT_ROOT,
) -> ExecutionResult:
    plan = build_plan(registry_path=registry_path, write_reports=True)
    if not plan.next_best_service:
        raise ExecutionError("Nenhum serviço recomendado pelo planner.")
    return execute_service(
        plan.next_best_service.service.id,
        registry_path=registry_path,
        dry_run=dry_run,
        no_write=no_write,
        state_path=state_path,
        history_path=history_path,
        report_path=report_path,
        output_root=output_root,
    )


def execute_service(
    service_id: str,
    *,
    registry_path: Path = Path("factory/registry/omie_services.yaml"),
    dry_run: bool = False,
    no_write: bool = False,
    state_path: Path = DEFAULT_STATE_PATH,
    history_path: Path = DEFAULT_HISTORY_PATH,
    report_path: Path = DEFAULT_REPORT_PATH,
    output_root: Path = DEFAULT_OUTPUT_ROOT,
) -> ExecutionResult:
    services = load_registry(registry_path)
    service = find_service(services, service_id)
    started = now_iso()
    start_monotonic = time.monotonic()
    warnings = validate_before_execution(service, registry_path=registry_path, state_path=state_path)
    state = load_state(state_path)
    state.update(
        {
            "status": "running",
            "current_service": service.id,
            "last_version": ENGINE_VERSION,
            "last_planner": "factory/reports/documentation_plan.md",
            "services_pending": [item.id for item in services if not item.implemented and item.id != service.id],
        }
    )
    save_state(state, state_path)

    errors: list[str] = []
    generated_files: tuple[str, ...] = ()
    status = "dry-run" if dry_run else "no-write" if no_write else "success"
    try:
        if dry_run:
            generated_files = planned_files_for(service, output_root)
        elif no_write:
            from main import run_pipeline

            output_dir = output_dir_for(service, output_root)
            pipeline_result = run_pipeline(service.documentation_url, output_dir, dry_run=True, service=service.name)
            generated_files = tuple(str(path).replace("\\", "/") for path in pipeline_result.generated_files)
        else:
            from main import run_pipeline

            output_dir = output_dir_for(service, output_root)
            pipeline_result = run_pipeline(service.documentation_url, output_dir, dry_run=False, service=service.name)
            generated_files = tuple(str(path).replace("\\", "/") for path in pipeline_result.generated_files)
    except Exception as exc:  # pragma: no cover - caminho defensivo de execucao externa
        status = "failed"
        errors.append(str(exc))

    finished = now_iso()
    duration = round(time.monotonic() - start_monotonic, 3)
    doc_hash = hash_generated_files(generated_files)
    quality_score = 1.0 if status in {"success", "dry-run", "no-write"} and not errors else 0.0
    result = ExecutionResult(
        service_id=service.id,
        service_name=service.name,
        status=status,
        started_at=started,
        finished_at=finished,
        duration_seconds=duration,
        generated_files=generated_files,
        warnings=tuple(warnings),
        errors=tuple(errors),
        quality_score=quality_score,
        documentation_hash=doc_hash,
        dry_run=dry_run,
        no_write=no_write,
    )
    warnings.extend(validate_after_execution(result))
    result = ExecutionResult(**{**asdict(result), "warnings": tuple(warnings)})
    update_state_after_execution(result, services, state_path, history_path)
    append_history(result, history_path)
    write_execution_report(result, report_path)
    sync_first_real_generation_report(result)
    return result


def resume_execution(state_path: Path = DEFAULT_STATE_PATH) -> str:
    state = load_state(state_path)
    if state["status"] == "running":
        state["status"] = "idle"
        state["current_service"] = None
        save_state(state, state_path)
        return "Execução anterior marcada como interrompida e liberada para retomada."
    return "Nenhuma execução em andamento para retomar."


def abort_execution(state_path: Path = DEFAULT_STATE_PATH) -> str:
    state = load_state(state_path)
    if state["status"] != "running":
        return "Nenhuma execução em andamento para abortar."
    state["services_ignored"] = sorted(set(state.get("services_ignored", []) + [state["current_service"]]))
    state["status"] = "aborted"
    state["current_service"] = None
    save_state(state, state_path)
    return "Execução abortada."


def update_state_after_execution(
    result: ExecutionResult,
    services: list[RegistryService],
    state_path: Path,
    history_path: Path,
) -> None:
    state = load_state(state_path)
    history = load_history(history_path)
    durations = [float(item.get("duration_seconds", 0.0)) for item in history] + [result.duration_seconds]
    completed = set(state.get("services_completed", []))
    failed = set(state.get("services_failed", []))
    if result.status == "success":
        completed.add(result.service_id)
        failed.discard(result.service_id)
    elif result.status == "failed":
        failed.add(result.service_id)
    state.update(
        {
            "last_service_executed": result.service_id,
            "last_execution": result.finished_at,
            "last_version": ENGINE_VERSION,
            "services_completed": sorted(completed),
            "services_pending": sorted(item.id for item in services if not item.implemented and item.id not in completed),
            "services_failed": sorted(failed),
            "average_duration_seconds": round(sum(durations) / len(durations), 3) if durations else 0.0,
            "documentation_hash": result.documentation_hash,
            "status": "idle" if result.status != "failed" else "failed",
            "current_service": None,
        }
    )
    save_state(state, state_path)


def append_history(result: ExecutionResult, history_path: Path) -> None:
    history = load_history(history_path)
    history.append(asdict(result))
    save_history(history, history_path)


def write_execution_report(result: ExecutionResult, path: Path = DEFAULT_REPORT_PATH) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_execution_report(result), encoding="utf-8")
    return path


def sync_first_real_generation_report(result: ExecutionResult) -> None:
    path = Path("factory/reports/first_real_generation.md")
    if not path.exists() or result.status != "success":
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "| Hash | `calculado pelo Execution Engine em factory/reports/execution_report.md` |",
        f"| Hash | `{result.documentation_hash}` |",
    )
    path.write_text(text, encoding="utf-8")


def render_execution_report(result: ExecutionResult) -> str:
    return f"""# Execution Report

| Campo | Valor |
| --- | --- |
| Serviço | {result.service_name} |
| Service ID | {result.service_id} |
| Status | {result.status} |
| Início | {result.started_at} |
| Fim | {result.finished_at} |
| Tempo | {result.duration_seconds}s |
| Arquivos gerados | {len(result.generated_files)} |
| Quality score | {result.quality_score} |
| Hash | {result.documentation_hash} |

## Warnings

{format_list(result.warnings)}

## Erros

{format_list(result.errors)}

## Arquivos

{format_list(result.generated_files)}
"""


def find_service(services: list[RegistryService], service_id: str) -> RegistryService:
    resolved_id = SERVICE_ID_ALIASES.get(service_id, service_id)
    for service in services:
        if service.id == resolved_id:
            return service
    raise ExecutionError(f"Serviço inexistente: {service_id}")


def planned_files_for(service: RegistryService, output_root: Path) -> tuple[str, ...]:
    base = output_dir_for(service, output_root)
    return (
        str(base / "docs").replace("\\", "/"),
        str(base / "schemas").replace("\\", "/"),
        str(base / "datasets").replace("\\", "/"),
        str(base / "graphs").replace("\\", "/"),
        str(base / "business").replace("\\", "/"),
        str(base / "rag").replace("\\", "/"),
        str(base / "reports").replace("\\", "/"),
        str(base / "coverage").replace("\\", "/"),
    )


def output_dir_for(service: RegistryService, output_root: Path) -> Path:
    if output_root in {Path("."), Path("")}:
        return Path(".")
    return output_root / service.output_slug


def hash_generated_files(files: tuple[str, ...]) -> str:
    raw = "\n".join(sorted(files))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def format_list(values: tuple[str, ...]) -> str:
    if not values:
        return "- Nenhum."
    return "\n".join(f"- {value}" for value in values)
