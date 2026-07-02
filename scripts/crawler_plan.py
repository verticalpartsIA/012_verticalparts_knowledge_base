"""Plano inicial de crawler para a base Omie.

Este arquivo nao executa chamadas reais na API Omie. Ele documenta uma
estrutura segura para futura implementacao de coleta, normalizacao e validacao.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CrawlerConfig:
    base_url: str
    output_dir: Path


def load_config() -> CrawlerConfig:
    return CrawlerConfig(
        base_url=os.getenv("OMIE_BASE_URL", "https://app.omie.com.br/api/v1"),
        output_dir=Path("datasets/raw/omie"),
    )


def planned_steps() -> list[str]:
    return [
        "Carregar configuracao por variaveis de ambiente.",
        "Coletar somente fontes autorizadas e documentacao publica.",
        "Salvar conteudo bruto em datasets/raw/omie, ignorado pelo Git.",
        "Normalizar documentos para Markdown padronizado.",
        "Validar campos obrigatorios e ausencia de credenciais.",
        "Gerar relatorio de pendencias para revisao humana.",
    ]


def main() -> None:
    config = load_config()
    print("Plano de crawler Omie")
    print(f"Base URL configurada: {config.base_url}")
    print(f"Diretorio de saida planejado: {config.output_dir}")
    for index, step in enumerate(planned_steps(), start=1):
        print(f"{index}. {step}")


if __name__ == "__main__":
    main()
