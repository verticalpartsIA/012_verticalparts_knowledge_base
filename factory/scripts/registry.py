"""Service Registry da Autonomous Knowledge Factory."""

from __future__ import annotations

from dataclasses import dataclass
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


DEFAULT_REGISTRY_PATH = Path("factory/registry/omie_services.yaml")
REQUIRED_FIELDS = {
    "id",
    "name",
    "domain",
    "endpoint",
    "status",
    "priority",
    "implemented",
    "methods_count",
    "documentation_url",
    "output_slug",
    "depends_on",
    "notes",
}


@dataclass(frozen=True)
class RegistryService:
    id: str
    name: str
    domain: str
    endpoint: str
    status: str
    priority: str
    implemented: bool
    methods_count: int | None
    documentation_url: str
    output_slug: str
    depends_on: tuple[str, ...]
    notes: str


class RegistryError(RuntimeError):
    """Erro de carga ou validacao do registry."""


@dataclass(frozen=True)
class RegistryHealth:
    total_services: int
    implemented_services: int
    duplicate_ids: tuple[str, ...]
    duplicate_endpoints: tuple[str, ...]
    duplicate_output_slugs: tuple[str, ...]
    missing_dependencies: tuple[str, ...]

    @property
    def healthy(self) -> bool:
        return not (
            self.duplicate_ids
            or self.duplicate_endpoints
            or self.duplicate_output_slugs
            or self.missing_dependencies
        )


def load_registry(path: Path = DEFAULT_REGISTRY_PATH) -> list[RegistryService]:
    if not path.exists():
        raise RegistryError(f"Registry nao encontrado: {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    services = raw.get("services")
    if not isinstance(services, list):
        raise RegistryError("Registry deve conter uma lista em 'services'.")
    return [service_from_dict(item, index) for index, item in enumerate(services, start=1)]


def service_from_dict(item: dict[str, Any], index: int) -> RegistryService:
    missing = sorted(REQUIRED_FIELDS - set(item))
    if missing:
        raise RegistryError(f"Servico #{index} sem campos obrigatorios: {', '.join(missing)}")
    depends_on = item.get("depends_on") or []
    if not isinstance(depends_on, list):
        raise RegistryError(f"Servico #{index} possui depends_on invalido.")
    return RegistryService(
        id=str(item["id"]),
        name=str(item["name"]),
        domain=str(item["domain"]).lower(),
        endpoint=str(item["endpoint"]),
        status=str(item["status"]),
        priority=str(item["priority"]).lower(),
        implemented=bool(item["implemented"]),
        methods_count=item["methods_count"] if isinstance(item["methods_count"], int) else None,
        documentation_url=str(item["documentation_url"]),
        output_slug=str(item["output_slug"]),
        depends_on=tuple(str(value) for value in depends_on),
        notes=str(item["notes"]),
    )


def validate_services(services: list[RegistryService]) -> None:
    health = registry_health(services)
    if health.duplicate_ids:
        raise RegistryError(f"IDs duplicados no registry: {', '.join(health.duplicate_ids)}")
    if health.duplicate_endpoints:
        raise RegistryError(f"Endpoints duplicados no registry: {', '.join(health.duplicate_endpoints)}")
    if health.duplicate_output_slugs:
        raise RegistryError(f"output_slug duplicado no registry: {', '.join(health.duplicate_output_slugs)}")
    if health.missing_dependencies:
        raise RegistryError(f"Dependencias inexistentes no registry: {', '.join(health.missing_dependencies)}")
    for service in services:
        if not service.documentation_url.startswith(("http://", "https://")):
            raise RegistryError(f"documentation_url invalida em {service.id}")
        if service.priority not in {"alta", "media", "baixa"}:
            raise RegistryError(f"priority invalida em {service.id}: {service.priority}")


def registry_health(services: list[RegistryService]) -> RegistryHealth:
    ids = [service.id for service in services]
    endpoints = [service.endpoint for service in services]
    output_slugs = [service.output_slug for service in services]
    known_ids = set(ids)
    missing_dependencies = sorted(
        f"{service.id}->{dependency}"
        for service in services
        for dependency in service.depends_on
        if dependency not in known_ids
    )
    return RegistryHealth(
        total_services=len(services),
        implemented_services=sum(1 for service in services if service.implemented),
        duplicate_ids=duplicates(ids),
        duplicate_endpoints=duplicates(endpoints),
        duplicate_output_slugs=duplicates(output_slugs),
        missing_dependencies=tuple(missing_dependencies),
    )


def duplicates(values: list[str]) -> tuple[str, ...]:
    counts = Counter(values)
    return tuple(sorted(value for value, count in counts.items() if count > 1))


def find_service(services: list[RegistryService], service_id: str) -> RegistryService:
    for service in services:
        if service.id == service_id:
            return service
    raise RegistryError(f"service-id nao encontrado: {service_id}")


def filter_services(
    services: list[RegistryService],
    *,
    status: str | None = None,
    domain: str | None = None,
    priority: str | None = None,
    implemented: bool | None = None,
) -> list[RegistryService]:
    result = services
    if status:
        result = [service for service in result if service.status.lower() == status.lower()]
    if domain:
        wanted = domain.lower()
        result = [service for service in result if wanted in service.domain]
    if priority:
        result = [service for service in result if service.priority == priority.lower()]
    if implemented is not None:
        result = [service for service in result if service.implemented is implemented]
    return result


def list_implemented(services: list[RegistryService]) -> list[RegistryService]:
    return filter_services(services, implemented=True)


def list_pending(services: list[RegistryService], *, domain: str | None = None) -> list[RegistryService]:
    return filter_services(services, domain=domain, implemented=False)


def next_recommended(
    services: list[RegistryService],
    *,
    domain: str | None = None,
    priority: str | None = None,
) -> RegistryService | None:
    priority_order = {"alta": 0, "media": 1, "baixa": 2}
    pending = filter_services(services, domain=domain, priority=priority, implemented=False)
    pending.sort(key=lambda service: (priority_order.get(service.priority, 99), service.status != "Planejado", service.id))
    return pending[0] if pending else None


def format_services(services: list[RegistryService]) -> str:
    if not services:
        return "Nenhum servico encontrado."
    lines = ["id | dominio | prioridade | status | url", "--- | --- | --- | --- | ---"]
    lines.extend(
        f"{service.id} | {service.domain} | {service.priority} | {service.status} | {service.documentation_url}"
        for service in services
    )
    return "\n".join(lines)


def render_health_report(services: list[RegistryService]) -> str:
    health = registry_health(services)
    status = "Saudavel" if health.healthy else "Com inconsistencias"
    return f"""# Registry Health

Status: {status}

| Métrica | Valor |
| --- | ---: |
| Serviços | {health.total_services} |
| Serviços implementados | {health.implemented_services} |
| IDs duplicados | {len(health.duplicate_ids)} |
| Endpoints duplicados | {len(health.duplicate_endpoints)} |
| Output slugs duplicados | {len(health.duplicate_output_slugs)} |
| Dependências inexistentes | {len(health.missing_dependencies)} |

## IDs duplicados

{format_list(health.duplicate_ids)}

## Endpoints duplicados

{format_list(health.duplicate_endpoints)}

## Output slugs duplicados

{format_list(health.duplicate_output_slugs)}

## Dependências inexistentes

{format_list(health.missing_dependencies)}
"""


def write_health_report(
    services: list[RegistryService],
    path: Path = Path("factory/reports/registry_health.md"),
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_health_report(services), encoding="utf-8")
    return path


def format_list(values: tuple[str, ...]) -> str:
    if not values:
        return "- Nenhuma."
    return "\n".join(f"- {value}" for value in values)
