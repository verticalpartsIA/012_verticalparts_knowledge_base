"""Modelos internos da Knowledge Factory."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


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

    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    words = re.findall(r"[A-Za-z0-9]+", ascii_value)
    return "_".join(word.lower() for word in words) or "sem_nome"
