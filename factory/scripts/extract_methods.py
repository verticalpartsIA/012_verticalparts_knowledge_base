"""Normalizacao de metodos extraidos pelo parser."""

from __future__ import annotations

from models import MethodInfo, ServiceInfo


class MethodExtractionError(RuntimeError):
    """Erro quando nenhum metodo confiavel e identificado."""


def extract_methods(service: ServiceInfo, allow_empty: bool = False) -> tuple[MethodInfo, ...]:
    """Retorna metodos unicos, ordenados e validados."""

    unique: dict[str, MethodInfo] = {}
    for method in service.methods:
        if method.name not in unique:
            unique[method.name] = method
    methods = tuple(sorted(unique.values(), key=lambda method: method.name.lower()))
    if not methods and not allow_empty:
        raise MethodExtractionError(
            "Nenhum metodo foi extraido da documentacao. Verifique se o HTML contem os nomes oficiais."
        )
    return methods
