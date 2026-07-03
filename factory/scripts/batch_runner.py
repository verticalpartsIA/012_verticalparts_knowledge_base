"""Batch runner seguro da Autonomous Knowledge Factory."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

from registry import RegistryService, filter_services, find_service, load_registry


DEFAULT_OUTPUT_ROOT = Path("factory/runs")


@dataclass(frozen=True)
class BatchItemResult:
    service_id: str
    service_name: str
    documentation_url: str
    status: str
    generated_files: int = 0
    planned_files: int = 0
    error: str | None = None


@dataclass(frozen=True)
class BatchRunResult:
    dry_run: bool
    no_write: bool
    results: tuple[BatchItemResult, ...]
    run_dir: Path
    report_path: Path
    manifest_path: Path


def select_services(
    services: list[RegistryService],
    *,
    domain: str | None = None,
    priority: str | None = None,
    limit: int | None = None,
    service_id: str | None = None,
) -> list[RegistryService]:
    if service_id:
        return [find_service(services, service_id)]
    selected = filter_services(services, domain=domain, priority=priority, implemented=False)
    selected.sort(key=lambda service: (priority_rank(service.priority), service.id))
    if limit is not None:
        selected = selected[:limit]
    return selected


def priority_rank(priority: str) -> int:
    return {"alta": 0, "media": 1, "baixa": 2}.get(priority, 99)


def run_batch(
    *,
    registry_path: Path = Path("factory/registry/omie_services.yaml"),
    output_root: Path = DEFAULT_OUTPUT_ROOT,
    dry_run: bool = False,
    no_write: bool = False,
    limit: int | None = None,
    domain: str | None = None,
    priority: str | None = None,
    service_id: str | None = None,
) -> BatchRunResult:
    run_dir = make_run_dir(output_root)
    services = select_services(
        load_registry(registry_path),
        domain=domain,
        priority=priority,
        limit=limit,
        service_id=service_id,
    )
    results: list[BatchItemResult] = []
    manifest: list[dict[str, object]] = []
    failed: list[dict[str, object]] = []

    for service in services:
        if dry_run:
            result = BatchItemResult(
                service_id=service.id,
                service_name=service.name,
                documentation_url=service.documentation_url,
                status="planned",
            )
            results.append(result)
            manifest.append(manifest_item(service, [], status=result.status))
            continue
        try:
            from main import run_pipeline

            service_output = run_dir / "generated" / service.output_slug
            pipeline_result = run_pipeline(
                service.documentation_url,
                service_output,
                dry_run=no_write,
                service=service.name,
            )
            planned_files = [str(path).replace("\\", "/") for path in pipeline_result.generated_files]
            status = "planned_no_write" if no_write else "generated"
            result = BatchItemResult(
                service_id=service.id,
                service_name=service.name,
                documentation_url=service.documentation_url,
                status=status,
                generated_files=0 if no_write else len(planned_files),
                planned_files=len(planned_files),
            )
            results.append(result)
            manifest.append(manifest_item(service, planned_files, status=status))
        except Exception as exc:  # pragma: no cover - caminho defensivo de execucao externa
            result = BatchItemResult(
                service_id=service.id,
                service_name=service.name,
                documentation_url=service.documentation_url,
                status="failed",
                error=str(exc),
            )
            results.append(result)
            failed.append(asdict(result))
            manifest.append(manifest_item(service, [], status="failed", error=str(exc)))

    write_run_artifacts(run_dir, results, failed, manifest, dry_run=dry_run, no_write=no_write)
    return BatchRunResult(
        dry_run=dry_run,
        no_write=no_write,
        results=tuple(results),
        run_dir=run_dir,
        report_path=run_dir / "run_summary.md",
        manifest_path=run_dir / "generated_files_manifest.json",
    )


def make_run_dir(output_root: Path) -> Path:
    run_id = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    run_dir = output_root / run_id
    counter = 1
    while run_dir.exists():
        run_dir = output_root / f"{run_id}_{counter:02d}"
        counter += 1
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_dir


def manifest_item(
    service: RegistryService,
    files: list[str],
    *,
    status: str,
    error: str | None = None,
) -> dict[str, object]:
    return {
        "service_id": service.id,
        "service_name": service.name,
        "documentation_url": service.documentation_url,
        "status": status,
        "files": files,
        "error": error,
    }


def write_run_artifacts(
    run_dir: Path,
    results: list[BatchItemResult],
    failed: list[dict[str, object]],
    manifest: list[dict[str, object]],
    *,
    dry_run: bool,
    no_write: bool,
) -> None:
    processed = [asdict(item) for item in results if item.status != "failed"]
    (run_dir / "run_summary.md").write_text(render_run_summary(results, dry_run=dry_run, no_write=no_write), encoding="utf-8")
    (run_dir / "dry_run_report.md").write_text(render_dry_run_report(results, dry_run=dry_run, no_write=no_write), encoding="utf-8")
    write_json(run_dir / "services_processed.json", processed)
    write_json(run_dir / "services_failed.json", failed)
    write_json(run_dir / "generated_files_manifest.json", manifest)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def render_run_summary(results: list[BatchItemResult], *, dry_run: bool, no_write: bool) -> str:
    mode = "dry-run" if dry_run else "no-write" if no_write else "geracao"
    lines = [
        "# Safe Batch Execution",
        "",
        f"Modo: {mode}",
        f"Serviços processados: {len(results)}",
        f"Falhas: {sum(1 for item in results if item.status == 'failed')}",
        "",
        "| Serviço | URL | Status | Arquivos gerados | Arquivos planejados | Erro |",
        "|---|---|---|---:|---:|---|",
    ]
    for item in results:
        lines.append(
            f"| {item.service_name} | {item.documentation_url} | {item.status} | {item.generated_files} | {item.planned_files} | {item.error or ''} |"
        )
    return "\n".join(lines) + "\n"


def render_dry_run_report(results: list[BatchItemResult], *, dry_run: bool, no_write: bool) -> str:
    if dry_run:
        title = "Dry-run: geração não executada"
    elif no_write:
        title = "No-write: parsing e planejamento executados sem gravar arquivos finais"
    else:
        title = "Execução com gravação"
    return f"""# {title}

Serviços avaliados: {len(results)}

{chr(10).join(f'- {item.service_id}: {item.status}' for item in results)}
"""
