from __future__ import annotations

from pathlib import Path


ROOT = Path(".")
DOCS = [
    path
    for path in (ROOT / "docs").rglob("*.md")
    if path.as_posix() != "docs/INDEX.md"
]
REPORT = ROOT / "reports" / "knowledge_score.md"


CHECKS = {
    "Completude": ["## Objetivo", "## Quando utilizar", "## Quando NÃO utilizar"],
    "Metadados": ["---", "llm_ready: true", "rag_ready: true", "graph_ready: true"],
    "Exemplos": ["## Exemplos completos", "### curl", "### Python", "### JavaScript"],
    "FAQ": ["## FAQ"],
    "Relacionamentos": ["## Entidades relacionadas", "## Métodos relacionados"],
    "Perguntas naturais": ["## Perguntas naturais"],
    "Business Knowledge": ["Fluxo de negócio", "Casos de uso"],
    "RAG": ["Tags para RAG", "rag_ready: true"],
    "GraphRAG": ["graph_ready: true", "GraphRAG"],
    "Embeddings": ["embedding_version"],
}


def score(text: str) -> tuple[int, dict[str, bool]]:
    results = {}
    hits = 0
    total = len(CHECKS)
    for name, needles in CHECKS.items():
        ok = all(needle in text for needle in needles)
        results[name] = ok
        hits += int(ok)
    return round((hits / total) * 100), results


def main() -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Knowledge Score", "", "| Arquivo | Nota | Lacunas |", "| --- | ---: | --- |"]
    for path in DOCS:
        text = path.read_text(encoding="utf-8")
        note, checks = score(text)
        gaps = [name for name, ok in checks.items() if not ok]
        lines.append(f"| `{path.as_posix()}` | {note} | {', '.join(gaps) if gaps else 'Nenhuma'} |")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Relatorio gerado em {REPORT}")


if __name__ == "__main__":
    main()
