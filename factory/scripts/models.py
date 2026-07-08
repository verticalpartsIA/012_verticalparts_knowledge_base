"""Modelos internos da Knowledge Factory."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from collections import Counter


@dataclass(frozen=True)
class FieldInfo:
    """Campo identificado em tabelas ou exemplos da documentacao."""

    name: str
    type: str = "Necessita validacao"
    required: bool = False
    description: str = "Necessita validacao"


@dataclass(frozen=True)
class MethodInfo:
    """Metodo oficial ou candidato extraido de um servico."""

    name: str
    endpoint: str
    service: str
    domain: str
    description: str = "Necessita validacao"
    request_fields: tuple[FieldInfo, ...] = ()
    response_fields: tuple[FieldInfo, ...] = ()
    examples: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()
    source_url: str = ""

    @property
    def slug(self) -> str:
        return slugify(self.name)


@dataclass(frozen=True)
class ServiceInfo:
    """Representacao intermediaria de um servico de API."""

    name: str
    endpoint: str
    domain: str
    description: str
    source_url: str
    methods: tuple[MethodInfo, ...] = ()


@dataclass(frozen=True)
class FactoryResult:
    """Resumo do pipeline executado pela CLI."""

    service: ServiceInfo
    output_dir: Path
    generated_files: tuple[Path, ...] = field(default_factory=tuple)
    dry_run: bool = False


def slugify(value: str) -> str:
    """Converte nomes da Omie para snake_case estavel."""

    import re
    import unicodedata

    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)
    value = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", value)
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    words = re.findall(r"[A-Za-z0-9]+", ascii_value)
    return "_".join(word.lower() for word in words) or "sem_nome"


def unique_method_slug_map(methods: tuple[MethodInfo, ...]) -> dict[MethodInfo, str]:
    """Gera slugs determinísticos e únicos para arquivos de métodos."""

    base_slugs = [slugify(method.name) for method in methods]
    collisions = {slug for slug, count in Counter(base_slugs).items() if count > 1}
    used: set[str] = set()
    result: dict[MethodInfo, str] = {}

    for index, method in enumerate(methods, start=1):
        base = slugify(method.name)
        candidate = base
        if base in collisions or candidate in used:
            suffixes = context_suffixes(method, index)
            for suffix in suffixes:
                candidate = f"{base}_{suffix}"
                if candidate not in used:
                    break
            while candidate in used:
                candidate = f"{base}_{slugify(method.endpoint)}_{index}"
        result[method] = candidate
        used.add(candidate)

    return result


def context_suffixes(method: MethodInfo, index: int) -> tuple[str, ...]:
    """Retorna sufixos estáveis baseados em contexto, tipo e endpoint."""

    description = method.description.lower()
    type_hint = "lote" if "lote" in description or "lote" in method.name.lower() else "cadastro"
    endpoint_hint = slugify(method.endpoint.strip("/").split("/")[-1] or method.endpoint)
    source_hint = slugify(method.source_url.strip("/").split("/")[-1] or method.source_url)
    return (
        type_hint,
        f"{type_hint}_{endpoint_hint}",
        f"{type_hint}_{source_hint}",
        f"{type_hint}_{endpoint_hint}_metodo_{index}",
    )
