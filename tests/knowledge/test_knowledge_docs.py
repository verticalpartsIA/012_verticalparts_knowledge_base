import re
from pathlib import Path


DOCS = list(Path("docs/omie").rglob("*.md"))


def read(path):
    return path.read_text(encoding="utf-8")


def test_all_omie_docs_have_yaml():
    assert DOCS
    for path in DOCS:
        assert read(path).startswith("---\n"), path


def test_method_docs_have_enterprise_sections():
    required = [
        "## FAQ",
        "## Perguntas naturais",
        "## Tags para RAG",
        "## Fonte oficial consultada",
        "llm_ready: true",
        "source:",
        "status:",
    ]
    for path in Path("docs/omie/geral/clientes").glob("*.md"):
        if path.name == "README.md":
            continue
        text = read(path)
        for item in required:
            assert item in text, f"{path}: {item}"
        assert len(re.findall(r"^### \d+\.", text, re.MULTILINE)) >= 20, path
        assert "### curl" in text, path
        assert "### Python" in text, path
        assert "### JavaScript" in text, path
        assert "### TypeScript" in text, path
        assert "### PHP" in text, path
        assert "### C#" in text, path
        assert "### Java" in text, path
        assert "### Delphi" in text, path
        assert "### n8n" in text, path
