"""Batch runner da Autonomous Knowledge Factory."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from registry import RegistryService, filter_services, load_registry


@dataclass(frozen=True)
class BatchItemResult:
    service_id: str
    service_name: str
    documentation_url: str
    status: str
    generated_files: int = 0
    error: str | None = None


@dataclass(frozen=True)
class BatchRunResult:
    dry_run: bool
    results: tuple[BatchItemResult, ...]
    report_path: Path


def select_services(
    services: list[RegistryService],
    *,
    domain: str | None = None,
    priority: str | None = None,
    limit: int | None = None,
) -> list[RegistryService]:
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
    output_dir: Path = Path("factory/output/batch"),
    dry_run: bool = False,
    limit: int | None = None,
    domain: str | None = None,
    priority: str | None = None,
) -> BatchRunResult:
    services = select_services(load_registry(registry_path), domain=domain, priority=priority, limit=limit)
    results: list[BatchItemResult] = []
    for service in services:
        if dry_run:
            results.append(
                BatchItemResult(
                    service_id=service.id,
                    service_name=service.name,
                    documentation_url=service.documentation_url,
                    status="planned",
                )
            )
            continue
        try:
            from main import run_pipeline

            result = run_pipeline(
                service.documentation_url,
                output_dir / service.output_slug,
                dry_run=False,
                service=service.name,
            )
            results.append(
                BatchItemResult(
                    service_id=service.id,
                    service_name=service.name,
                    documentation_url=service.documentation_url,
                    status="generated",
                    generated_files=len(result.generated_files),
                )
            )
        except Exception as exc:  # pragma: no cover - caminho defensivo de execucao externa
            results.append(
                BatchItemResult(
                    service_id=service.id,
                    service_name=service.name,
                    documentation_url=service.documentation_url,
                    status="failed",
                    error=str(exc),
                )
            )
    report_path = write_batch_report(results, output_dir, dry_run=dry_run)
    return BatchRunResult(dry_run=dry_run, results=tuple(results), report_path=report_path)


def write_batch_report(results: list[BatchItemResult], output_dir: Path, *, dry_run: bool) -> Path:
    report_dir = output_dir / "_reports"
    report_path = report_dir / "batch_report.md"
    if dry_run:
        return report_path
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_batch_report(results, dry_run=dry_run), encoding="utf-8")
    return report_path


def render_batch_report(results: list[BatchItemResult], *, dry_run: bool) -> str:
    mode = "dry-run" if dry_run else "geracao"
    lines = [f"# Batch Runner Report", "", f"Modo: {mode}", "", "| Serviço | URL | Status | Arquivos | Erro |", "|---|---|---|---:|---|"]
    for item in results:
        lines.append(
            f"| {item.service_name} | {item.documentation_url} | {item.status} | {item.generated_files} | {item.error or ''} |"
        )
    return "\n".join(lines) + "\n"
