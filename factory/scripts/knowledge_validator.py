"""Knowledge Validation Engine deterministico da Autonomous Knowledge Factory."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(".")
DEFAULT_CONFIG = Path("factory/config/validation.yaml")
DEFAULT_REPORT = Path("factory/reports/validation_report.md")
DEFAULT_IMPROVEMENT = Path("factory/reports/improvement_report.md")
DEFAULT_RANKING = Path("factory/reports/document_quality_ranking.md")
KNOWLEDGE_SCORE = Path("reports/knowledge_score.md")


@dataclass(frozen=True)
class DocumentValidation:
    path: Path
    service_key: str
    score: int
    checks: dict[str, bool]
    issues: tuple[str, ...]
    suggestions: tuple[str, ...]
    previous_score: int | None = None
    regression: str = "sem baseline"


@dataclass(frozen=True)
class ValidationResult:
    documents: tuple[DocumentValidation, ...]
    average_score: float
    report_path: Path
    improvement_path: Path
    ranking_path: Path


def load_config(path: Path = DEFAULT_CONFIG) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate(
    *,
    service_id: str | None = None,
    docs_root: Path = Path("docs/omie"),
    config_path: Path = DEFAULT_CONFIG,
    write_reports: bool = True,
) -> ValidationResult:
    config = load_config(config_path)
    docs = select_documents(docs_root, service_id)
    previous_scores = load_previous_scores()
    documents = tuple(validate_document(path, config, previous_scores) for path in docs)
    average = round(sum(item.score for item in documents) / len(documents), 2) if documents else 0.0
    result = ValidationResult(documents, average, DEFAULT_REPORT, DEFAULT_IMPROVEMENT, DEFAULT_RANKING)
    if write_reports:
        write_validation_report(result)
        write_improvement_report(result)
        write_quality_ranking(result)
    return result


def select_documents(docs_root: Path, service_id: str | None = None) -> list[Path]:
    docs = sorted(path for path in docs_root.rglob("*.md") if path.name != "README.md")
    if not service_id:
        return docs
    candidates = {normalize(value) for value in resolve_service_filters(service_id)}
    return [
        path
        for path in docs
        if candidates
        & {normalize(path.stem), normalize(service_key_for(path)), normalize(path.parent.name), normalize(path.as_posix())}
        or any(candidate in normalize(path.as_posix()) for candidate in candidates)
    ]


def resolve_service_filters(service_id: str) -> set[str]:
    values = {service_id}
    registry = Path("factory/registry/omie_services.yaml")
    if not registry.exists():
        return values
    data = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
    for service in data.get("services", []):
        if service.get("id") == service_id:
            values.add(str(service.get("output_slug") or service_id))
            endpoint = str(service.get("endpoint") or "").strip("/")
            if endpoint:
                values.add(endpoint.rsplit("/", 1)[-1])
    return values


def validate_document(path: Path, config: dict, previous_scores: dict[str, int]) -> DocumentValidation:
    text = path.read_text(encoding="utf-8")
    metadata, yaml_ok = parse_front_matter(text)
    service_key = service_key_for(path, metadata)
    checks = {
        "completude": has_required_sections(text, config),
        "consistencia": is_consistent(path, metadata),
        "referencias": has_official_reference(metadata, text, config),
        "estrutura": has_valid_structure(text),
        "metadados": has_required_metadata(metadata, config),
        "rag": has_rag(text, metadata),
        "graphrag": has_graph(service_key, text, metadata),
        "schemas": has_schema(path, service_key),
        "faq": has_faq(text, int(config["faq_minimum_items"])),
        "questions": has_questions(text, int(config["questions_minimum_items"])),
        "business_knowledge": has_business_knowledge(service_key, text),
        "markdown": yaml_ok and has_valid_markdown(text) and links_are_valid(path, text),
    }
    issues, suggestions = build_issues(path, checks, metadata)
    score = score_document(checks, config["weights"])
    previous = previous_scores.get(path.as_posix())
    regression = compare_scores(previous, score)
    return DocumentValidation(path, service_key, score, checks, tuple(issues), tuple(suggestions), previous, regression)


def parse_front_matter(text: str) -> tuple[dict, bool]:
    if not text.startswith("---\n"):
        return {}, False
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, False
    try:
        data = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}, False
    return data if isinstance(data, dict) else {}, True


def has_required_sections(text: str, config: dict) -> bool:
    return all(section in text for section in config["required_sections"])


def is_consistent(path: Path, metadata: dict) -> bool:
    method = str(metadata.get("method", "") or "")
    endpoint = str(metadata.get("endpoint", "") or "")
    if path.name == "README.md":
        return True
    return bool(method and endpoint and endpoint.startswith("https://"))


def has_official_reference(metadata: dict, text: str, config: dict) -> bool:
    source = str(metadata.get("source", "") or "")
    endpoint = str(metadata.get("endpoint", "") or "")
    prefixes = tuple(config["official_source_prefixes"])
    return (source.startswith(prefixes) or endpoint.startswith(prefixes)) and "## Fonte oficial consultada" in text


def has_valid_structure(text: str) -> bool:
    h1_count = len(re.findall(r"^# ", text, re.MULTILINE))
    indented_heading = bool(re.search(r"^[ \t]+#", text, re.MULTILINE))
    return h1_count == 1 and not indented_heading


def has_required_metadata(metadata: dict, config: dict) -> bool:
    required = config["required_metadata"]
    return all(key in metadata for key in required)


def has_rag(text: str, metadata: dict) -> bool:
    tags = metadata.get("tags", [])
    return bool(metadata.get("rag_ready") is True and tags and "## Tags para RAG" in text)


def has_graph(service_key: str, text: str, metadata: dict) -> bool:
    return metadata.get("graph_ready") is True and graph_path(service_key).exists()


def has_schema(path: Path, service_key: str) -> bool:
    stem = path.stem
    schema_matches = list(Path("schemas").rglob(f"{stem}.schema.json"))
    return bool(schema_matches or list(Path("schemas").rglob(f"{service_key}.schema.json")))


def has_faq(text: str, minimum: int) -> bool:
    if "## FAQ" not in text:
        return False
    numbered = len(re.findall(r"^###\s+\d+\.", text, re.MULTILINE))
    headings = len(re.findall(r"^###\s+", text, re.MULTILINE))
    return max(numbered, headings) >= minimum


def has_questions(text: str, minimum: int) -> bool:
    match = re.search(r"## Perguntas naturais\s+(.*?)(?:\n## |\Z)", text, re.DOTALL)
    if not match:
        return False
    return len(re.findall(r"^\s*[-*]\s+", match.group(1), re.MULTILINE)) >= minimum


def has_business_knowledge(service_key: str, text: str) -> bool:
    return business_path(service_key).exists() and ("Fluxo de negócio" in text or "## Fluxo de negocio" in text)


def has_valid_markdown(text: str) -> bool:
    return "```" not in text or text.count("```") % 2 == 0


def links_are_valid(path: Path, text: str) -> bool:
    for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if link.startswith(("#", "http://", "https://", "mailto:")):
            if link.startswith(("http://", "https://")) and not urlparse(link).netloc:
                return False
            continue
        target = (path.parent / link.split("#", 1)[0]).resolve()
        if link.split("#", 1)[0] and not target.exists():
            return False
    return True


def score_document(checks: dict[str, bool], weights: dict[str, int]) -> int:
    total = sum(int(value) for value in weights.values())
    achieved = sum(int(weights[name]) for name, ok in checks.items() if ok)
    return round((achieved / total) * 100) if total else 0


def build_issues(path: Path, checks: dict[str, bool], metadata: dict) -> tuple[list[str], list[str]]:
    labels = {
        "completude": ("Seções obrigatórias incompletas", "Adicionar seções ausentes do LLM_DOCUMENT_STANDARD.md."),
        "consistencia": ("Endpoint ou método inconsistente", "Conferir method, endpoint e título do documento."),
        "referencias": ("Fonte oficial ausente ou inválida", "Adicionar fonte oficial Omie validada."),
        "estrutura": ("Estrutura Markdown inválida", "Corrigir H1 único e headings sem indentação."),
        "metadados": ("Metadados YAML incompletos", "Preencher campos obrigatórios de front matter."),
        "rag": ("Tags ou metadados RAG insuficientes", "Adicionar tags e rag_ready: true quando aplicável."),
        "graphrag": ("GraphRAG ausente", "Criar ou revisar grafo Mermaid relacionado ao serviço."),
        "schemas": ("Schema ausente", "Criar schema JSON do método ou serviço."),
        "faq": ("FAQ insuficiente", "Adicionar no mínimo 20 perguntas e respostas."),
        "questions": ("Perguntas naturais insuficientes", "Adicionar perguntas naturais úteis para usuários."),
        "business_knowledge": ("Business Knowledge insuficiente", "Criar documento business/omie do serviço."),
        "markdown": ("YAML, Markdown ou links inválidos", "Validar front matter, blocos de código e links internos."),
    }
    issues: list[str] = []
    suggestions: list[str] = []
    for key, ok in checks.items():
        if not ok:
            issue, suggestion = labels[key]
            issues.append(issue)
            suggestions.append(suggestion)
    if not metadata:
        issues.append("Front matter YAML ausente ou inválido")
        suggestions.append("Inserir YAML front matter válido no início do arquivo.")
    return issues, suggestions


def load_previous_scores(path: Path = KNOWLEDGE_SCORE) -> dict[str, int]:
    if not path.exists():
        return {}
    scores = {}
    for match in re.finditer(r"\| `([^`]+)` \| (\d+) \|", path.read_text(encoding="utf-8")):
        scores[match.group(1)] = int(match.group(2))
    return scores


def compare_scores(previous: int | None, current: int) -> str:
    if previous is None:
        return "sem baseline"
    if current > previous:
        return "melhorou"
    if current < previous:
        return "piorou"
    return "igual"


def write_validation_report(result: ValidationResult) -> Path:
    DEFAULT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Knowledge Validation Report",
        "",
        f"Documentos avaliados: {len(result.documents)}",
        f"Score médio: {result.average_score:.2f}",
        "",
        "| Documento | Serviço | Score | Regressão | Issues |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for item in result.documents:
        issues = "; ".join(item.issues) if item.issues else "Nenhuma"
        lines.append(f"| `{item.path.as_posix()}` | `{item.service_key}` | {item.score} | {item.regression} | {issues} |")
    DEFAULT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return DEFAULT_REPORT


def write_improvement_report(result: ValidationResult) -> Path:
    lines = ["# Knowledge Improvement Report", ""]
    incomplete = [item for item in result.documents if item.issues]
    lines.append(f"Documentos incompletos: {len(incomplete)}")
    lines.append("")
    for item in incomplete:
        lines.append(f"## {item.path.as_posix()}")
        lines.append("")
        lines.append(f"Score: {item.score}")
        lines.append("")
        lines.append("### Campos ausentes ou problemas")
        lines.extend(f"- {issue}" for issue in item.issues)
        lines.append("")
        lines.append("### Sugestões objetivas de melhoria")
        lines.extend(f"- {suggestion}" for suggestion in item.suggestions)
        lines.append("")
    if not incomplete:
        lines.append("Nenhuma melhoria obrigatória identificada.")
    DEFAULT_IMPROVEMENT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return DEFAULT_IMPROVEMENT


def write_quality_ranking(result: ValidationResult) -> Path:
    service_scores: dict[str, list[int]] = {}
    for item in result.documents:
        service_scores.setdefault(item.service_key, []).append(item.score)
    rows = sorted(
        ((service, round(sum(scores) / len(scores), 2), len(scores)) for service, scores in service_scores.items()),
        key=lambda row: (-row[1], row[0]),
    )
    lines = [
        "# Document Quality Ranking",
        "",
        "| Posição | Serviço | Score médio | Documentos |",
        "| ---: | --- | ---: | ---: |",
    ]
    for index, (service, score, count) in enumerate(rows, start=1):
        lines.append(f"| {index} | `{service}` | {score:.2f} | {count} |")
    DEFAULT_RANKING.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return DEFAULT_RANKING


def format_summary(result: ValidationResult) -> str:
    return (
        f"Knowledge Validation concluído. Documentos: {len(result.documents)} | "
        f"Score médio: {result.average_score:.2f} | Relatório: {result.report_path}"
    )


def service_key_for(path: Path, metadata: dict | None = None) -> str:
    if path.parent.name in {"clientes", "contas_a_receber", "contas_a_pagar_lancamentos"}:
        return path.parent.name
    if metadata and metadata.get("service"):
        return normalize(str(metadata["service"]))
    return path.stem


def business_path(service_key: str) -> Path:
    return Path("business/omie") / f"{service_key}.md"


def graph_path(service_key: str) -> Path:
    return Path("graphs/omie") / f"{service_key}.graph.md"


def normalize(value: str) -> str:
    import unicodedata

    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()
    return value


def main() -> None:
    result = validate()
    print(format_summary(result))


if __name__ == "__main__":
    main()
