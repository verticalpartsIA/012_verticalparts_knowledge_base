"""Gerador de chunks Markdown para RAG."""

from __future__ import annotations

import json
from pathlib import Path

from models import ServiceInfo, slugify


def generate_chunks(service: ServiceInfo, output_dir: Path, dry_run: bool = False) -> list[Path]:
    target_dir = output_dir / "rag" / "chunks" / slugify(service.name)
    files: list[Path] = []
    index: list[dict[str, str]] = []
    for method in service.methods:
        chunk_id = f"{slugify(service.name)}-{method.slug}-001"
        path = target_dir / f"{chunk_id}.md"
        content = render_chunk(chunk_id, method.name, service.name, service.source_url, method.description)
        files.append(path)
        index.append({"chunk_id": chunk_id, "method": method.name, "path": str(path).replace("\\", "/")})
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    index_path = target_dir / "index.json"
    files.append(index_path)
    if not dry_run:
        index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    return files


def render_chunk(chunk_id: str, method_name: str, service_name: str, source_url: str, description: str) -> str:
    return f"""---
chunk_id: "{chunk_id}"
service: "{service_name}"
method: "{method_name}"
source: "{source_url}"
rag_ready: true
---

# {method_name}

Servico: {service_name}

Fonte oficial: {source_url}

Resumo extraido automaticamente:

{description or "Necessita validacao."}
"""
