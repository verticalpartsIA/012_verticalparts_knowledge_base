"""Service Registry da Autonomous Knowledge Factory."""

from __future__ import annotations

from dataclasses import dataclass
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
    ids = [service.id for service in services]
    duplicates = sorted({service_id for service_id in ids if ids.count(service_id) > 1})
    if duplicates:
        raise RegistryError(f"IDs duplicados no registry: {', '.join(duplicates)}")
    for service in services:
        if not service.documentation_url.startswith(("http://", "https://")):
            raise RegistryError(f"documentation_url invalida em {service.id}")
        if service.priority not in {"alta", "media", "baixa"}:
            raise RegistryError(f"priority invalida em {service.id}: {service.priority}")


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
