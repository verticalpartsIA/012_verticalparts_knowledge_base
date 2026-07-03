"""Dynamic Service Discovery para a API publica da Omie."""

from __future__ import annotations

import hashlib
import html
import json
import re
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import yaml


SOURCE_URL = "https://developer.omie.com.br/service-list/"
GENERATOR_VERSION = "0.7.0"
DEFAULT_GENERATED_REGISTRY = Path("factory/registry/omie_services.generated.yaml")
DEFAULT_OFFICIAL_REGISTRY = Path("factory/registry/omie_services.yaml")
DEFAULT_DISCOVERY_REPORT = Path("factory/reports/discovery_report.md")


@dataclass(frozen=True)
class DiscoveredService:
    id: str
    name: str
    category: str
    description: str
    endpoint: str
    url: str
    domain: str
    status: str
    priority: str
    implemented: bool
    methods_count: int | None
    documentation_url: str
    output_slug: str
    depends_on: tuple[str, ...]
    notes: str


@dataclass(frozen=True)
class RegistryComparison:
    new_services: tuple[DiscoveredService, ...]
    removed_services: tuple[dict, ...]
    changed_services: tuple[dict, ...]


class DiscoveryError(RuntimeError):
    """Erro de discovery publico da lista de servicos Omie."""


class ServiceListParser(HTMLParser):
    """Parser conservador da tabela publica de service-list."""

    def __init__(self) -> None:
        super().__init__()
        self.current_category = "Sem categoria"
        self.current_category_description = ""
        self.rows: list[dict[str, str]] = []
        self._in_category = False
        self._in_row = False
        self._in_cell = False
        self._in_link = False
        self._cell_text: list[str] = []
        self._row_cells: list[str] = []
        self._row_link = ""
        self._row_name = ""
        self._category_text: list[str] = []
        self._category_title: list[str] = []
        self._in_category_strong = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        css_class = attrs_dict.get("class", "")
        if tag == "tr" and "api-categ" in css_class:
            self._in_category = True
            self._category_text = []
            self._category_title = []
        elif tag == "tr" and "api-item" in css_class:
            self._in_row = True
            self._row_cells = []
            self._row_link = ""
            self._row_name = ""
        elif tag == "td" and (self._in_row or self._in_category):
            self._in_cell = True
            self._cell_text = []
        elif tag == "a" and self._in_row:
            href = attrs_dict.get("href", "")
            if "app.omie.com.br/api/v1/" in href:
                self._in_link = True
                self._row_link = href
                self._cell_text = []
        elif tag == "strong" and self._in_category:
            self._in_category_strong = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._in_link:
            self._row_name = clean_text(" ".join(self._cell_text))
            self._in_link = False
        elif tag == "strong" and self._in_category_strong:
            self._in_category_strong = False
        elif tag == "td" and self._in_cell:
            text = clean_text(" ".join(self._cell_text))
            if self._in_category and text:
                self._category_text.append(text)
            elif self._in_row:
                self._row_cells.append(text)
            self._cell_text = []
            self._in_cell = False
        elif tag == "tr" and self._in_category:
            texts = [text for text in self._category_text if text]
            title = clean_text(" ".join(self._category_title))
            if title:
                self.current_category = title
                description = clean_text(" ".join(texts)).removeprefix(title).strip()
                self.current_category_description = description
            elif texts:
                self.current_category = texts[0]
                self.current_category_description = texts[1] if len(texts) > 1 else ""
            self._in_category = False
        elif tag == "tr" and self._in_row:
            if self._row_link:
                description = self._row_cells[1] if len(self._row_cells) > 1 else ""
                self.rows.append(
                    {
                        "name": self._row_name or (self._row_cells[0] if self._row_cells else ""),
                        "category": self.current_category,
                        "category_description": self.current_category_description,
                        "description": description,
                        "url": normalize_service_url(self._row_link),
                    }
                )
            self._in_row = False

    def handle_data(self, data: str) -> None:
        if self._in_category_strong:
            self._category_title.append(html.unescape(data))
        if self._in_cell or self._in_link:
            self._cell_text.append(html.unescape(data))


def fetch_service_list(url: str = SOURCE_URL, timeout: int = 30) -> str:
    request = Request(url, headers={"User-Agent": "VerticalParts-Knowledge-Factory/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            raw = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            return raw.decode(charset, errors="replace")
    except HTTPError as exc:
        raise DiscoveryError(f"Falha HTTP no discovery: {exc.code}") from exc
    except URLError as exc:
        raise DiscoveryError(f"Falha de rede no discovery: {exc.reason}") from exc


def parse_service_list(html_text: str, existing_services: list[dict] | None = None) -> list[DiscoveredService]:
    parser = ServiceListParser()
    parser.feed(html_text)
    existing_by_url = {service.get("documentation_url") or service.get("endpoint"): service for service in existing_services or []}
    used_ids: dict[str, int] = {}
    used_slugs: dict[str, int] = {}
    services: list[DiscoveredService] = []
    for row in parser.rows:
        url = row["url"]
        existing = existing_by_url.get(url, {})
        base_id = slugify(f"{row['category']} {row['name']}")
        service_id = unique_value(base_id, used_ids)
        output_slug = unique_value(slugify(row["name"]), used_slugs)
        services.append(
            DiscoveredService(
                id=service_id,
                name=row["name"],
                category=row["category"],
                description=row["description"],
                endpoint=url,
                url=url,
                domain=infer_domain(url, row["category"]),
                status=existing.get("status", "Não iniciado"),
                priority=existing.get("priority", infer_priority(row["name"], row["category"])),
                implemented=bool(existing.get("implemented", False)),
                methods_count=existing.get("methods_count") if isinstance(existing.get("methods_count"), int) else None,
                documentation_url=url,
                output_slug=existing.get("output_slug", output_slug),
                depends_on=tuple(existing.get("depends_on") or []),
                notes="Servico descoberto automaticamente em documentação publica da Omie.",
            )
        )
    return services


def load_registry_dict(path: Path) -> dict:
    if not path.exists():
        return {"services": []}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {"services": []}


def discover_services(
    *,
    source_url: str = SOURCE_URL,
    official_registry: Path = DEFAULT_OFFICIAL_REGISTRY,
    generated_registry: Path = DEFAULT_GENERATED_REGISTRY,
    report_path: Path = DEFAULT_DISCOVERY_REPORT,
) -> tuple[list[DiscoveredService], RegistryComparison]:
    current = load_registry_dict(official_registry)
    html_text = fetch_service_list(source_url)
    services = parse_service_list(html_text, existing_services=current.get("services", []))
    write_generated_registry(services, generated_registry, source_url=source_url)
    comparison = compare_registry(current.get("services", []), services)
    write_discovery_report(comparison, services, report_path)
    return services, comparison


def refresh_registry(**kwargs) -> tuple[list[DiscoveredService], RegistryComparison]:
    """Atualiza somente o registry gerado, preservando o registry oficial."""

    return discover_services(**kwargs)


def compare_registry(current_services: list[dict], discovered_services: list[DiscoveredService]) -> RegistryComparison:
    current_by_url = {normalize_service_url(service.get("documentation_url") or service.get("endpoint", "")): service for service in current_services}
    discovered_by_url = {service.documentation_url: service for service in discovered_services}
    new_services = tuple(service for url, service in discovered_by_url.items() if url not in current_by_url)
    removed_services = tuple(service for url, service in current_by_url.items() if url and url not in discovered_by_url)
    changed = []
    for url, service in discovered_by_url.items():
        current = current_by_url.get(url)
        if not current:
            continue
        changes = {}
        if clean_text(current.get("name", "")) != service.name:
            changes["name"] = {"current": current.get("name", ""), "discovered": service.name}
        current_category = clean_text(current.get("category", "") or current.get("domain", ""))
        if current_category and current_category.lower() != service.category.lower():
            changes["category"] = {"current": current_category, "discovered": service.category}
        if normalize_service_url(current.get("documentation_url", "")) != service.documentation_url:
            changes["url"] = {"current": current.get("documentation_url", ""), "discovered": service.documentation_url}
        current_description = clean_text(current.get("description", ""))
        if current_description and current_description != service.description:
            changes["description"] = {"current": current_description, "discovered": service.description}
        if changes:
            changed.append({"endpoint": url, "changes": changes})
    return RegistryComparison(new_services=new_services, removed_services=removed_services, changed_services=tuple(changed))


def write_generated_registry(services: list[DiscoveredService], path: Path, *, source_url: str = SOURCE_URL) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload_services = [service_to_registry_dict(service) for service in services]
    content_hash = registry_hash(payload_services)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator_version": GENERATOR_VERSION,
        "source": source_url,
        "service_count": len(payload_services),
        "hash": content_hash,
        "services": payload_services,
    }
    path.write_text(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return path


def write_discovery_report(comparison: RegistryComparison, services: list[DiscoveredService], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_discovery_report(comparison, services), encoding="utf-8")
    return path


def render_discovery_report(comparison: RegistryComparison, services: list[DiscoveredService]) -> str:
    return f"""# Dynamic Service Discovery

Fonte: {SOURCE_URL}

| Métrica | Valor |
| --- | ---: |
| Serviços encontrados | {len(services)} |
| Serviços novos | {len(comparison.new_services)} |
| Serviços removidos | {len(comparison.removed_services)} |
| Serviços alterados | {len(comparison.changed_services)} |

## Serviços novos

{format_services_markdown(comparison.new_services)}

## Serviços removidos

{format_removed_markdown(comparison.removed_services)}

## Serviços alterados

{format_changed_markdown(comparison.changed_services)}
"""


def service_to_registry_dict(service: DiscoveredService) -> dict:
    return {
        "id": service.id,
        "name": service.name,
        "category": service.category,
        "description": service.description,
        "domain": service.domain,
        "endpoint": service.endpoint,
        "url": service.url,
        "status": service.status,
        "priority": service.priority,
        "implemented": service.implemented,
        "methods_count": service.methods_count,
        "documentation_url": service.documentation_url,
        "output_slug": service.output_slug,
        "depends_on": list(service.depends_on),
        "notes": service.notes,
    }


def service_from_generated_dict(item: dict) -> DiscoveredService:
    return DiscoveredService(
        id=str(item["id"]),
        name=str(item["name"]),
        category=str(item.get("category") or item.get("domain", "")),
        description=str(item.get("description", "")),
        endpoint=normalize_service_url(str(item.get("endpoint") or item.get("documentation_url", ""))),
        url=normalize_service_url(str(item.get("url") or item.get("documentation_url", ""))),
        domain=str(item.get("domain", "")),
        status=str(item.get("status", "Não iniciado")),
        priority=str(item.get("priority", "baixa")),
        implemented=bool(item.get("implemented", False)),
        methods_count=item.get("methods_count") if isinstance(item.get("methods_count"), int) else None,
        documentation_url=normalize_service_url(str(item.get("documentation_url") or item.get("endpoint", ""))),
        output_slug=str(item.get("output_slug", "")),
        depends_on=tuple(str(value) for value in (item.get("depends_on") or [])),
        notes=str(item.get("notes", "")),
    )


def registry_hash(services: list[dict]) -> str:
    raw = json.dumps(services, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def format_services_markdown(services: tuple[DiscoveredService, ...]) -> str:
    if not services:
        return "- Nenhum."
    return "\n".join(f"- `{service.documentation_url}` — {service.name} ({service.category})" for service in services)


def format_removed_markdown(services: tuple[dict, ...]) -> str:
    if not services:
        return "- Nenhum."
    return "\n".join(f"- `{service.get('documentation_url') or service.get('endpoint')}` — {service.get('name', 'Sem nome')}" for service in services)


def format_changed_markdown(changes: tuple[dict, ...]) -> str:
    if not changes:
        return "- Nenhuma."
    lines = []
    for item in changes:
        lines.append(f"- `{item['endpoint']}`")
        for field, values in item["changes"].items():
            lines.append(f"  - {field}: `{values['current']}` -> `{values['discovered']}`")
    return "\n".join(lines)


def normalize_service_url(url: str) -> str:
    return url.split("#", 1)[0].rstrip("/") + "/" if url else ""


def infer_domain(url: str, category: str) -> str:
    parts = [part for part in urlparse(url).path.split("/") if part]
    if "api" in parts:
        index = parts.index("api")
        if len(parts) > index + 2:
            return parts[index + 2]
    return slugify(category)


def infer_priority(name: str, category: str) -> str:
    value = f"{name} {category}".lower()
    if any(token in value for token in ("clientes", "contas a pagar", "contas a receber", "pedidos de venda", "produtos", "categorias", "movimentos financeiros")):
        return "alta"
    if any(token in value for token in ("estoque", "ordens de serviço", "nfs-e", "nf-e", "crm")):
        return "media"
    return "baixa"


def unique_value(base: str, used: dict[str, int]) -> str:
    used[base] = used.get(base, 0) + 1
    if used[base] == 1:
        return base
    return f"{base}_{used[base]}"


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(str(value))).strip()


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    words = re.findall(r"[A-Za-z0-9]+", ascii_value)
    return "_".join(word.lower() for word in words) or "servico"
