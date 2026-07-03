"""Gerador de relatorios minimos da Factory."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from models import ServiceInfo


def generate_reports(service: ServiceInfo, output_dir: Path, generated_files: list[Path], dry_run: bool = False) -> list[Path]:
    files = [
        output_dir / "reports" / "dashboard.md",
        output_dir / "coverage" / "omie_api_coverage.md",
        output_dir / "reports" / "knowledge_score.md",
    ]
    if dry_run:
        return files

    for path in files:
        path.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    files[0].write_text(
        f"""# Factory Dashboard

Atualizado em: {now}

Servico processado: {service.name}

Endpoint: {service.endpoint}

Metodos extraidos: {len(service.methods)}

Arquivos previstos/gerados: {len(generated_files)}
""",
        encoding="utf-8",
    )
    files[1].write_text(
        f"""# Factory Coverage

| Servico | Endpoint | Metodos | Status |
|---|---|---:|---|
| {service.name} | {service.endpoint} | {len(service.methods)} | MVP gerado/a validar |
""",
        encoding="utf-8",
    )
    files[2].write_text(
        f"""# Factory Knowledge Score

Score MVP: 1.0

Critérios avaliados:

- HTML coletado
- Metodos extraidos
- Documentos planejados ou gerados
- Perguntas geradas deterministicamente
- Chunks gerados
""",
        encoding="utf-8",
    )
    return files
