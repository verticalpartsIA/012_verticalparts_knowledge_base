"""Parser HTML da Knowledge Factory.

Extrai uma representacao intermediaria sem depender de LLM. O parser usa
heuristicas conservadoras para paginas da Omie e mantem campos ambiguos como
"Necessita validacao".
"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urlparse

from models import FieldInfo, MethodInfo, ServiceInfo


@dataclass
class HtmlSection:
    title: str
    level: int
    text: str
    tables: list[list[list[str]]]
    code_blocks: list[str]


class StructuredHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.sections: list[HtmlSection] = [HtmlSection("Documento", 1, "", [], [])]
        self._tag_stack: list[str] = []
        self._current_text: list[str] = []
        self._table: list[list[str]] | None = None
        self._row: list[str] | None = None
        self._cell: list[str] | None = None
        self._code: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._tag_stack.append(tag)
        if tag in {"h1", "h2", "h3", "h4"}:
            self._current_text = []
        elif tag == "table":
            self._table = []
        elif tag == "tr":
            self._row = []
        elif tag in {"td", "th"}:
            self._cell = []
        elif tag in {"pre", "code"} and self._code is None:
            self._code = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"h1", "h2", "h3", "h4"}:
            title = clean_text(" ".join(self._current_text))
            if title:
                level = int(tag[1])
                if not self.title and tag == "h1":
                    self.title = title
                self.sections.append(HtmlSection(title, level, "", [], []))
            self._current_text = []
        elif tag in {"p", "li", "div"}:
            self.sections[-1].text += " "
        elif tag in {"td", "th"} and self._row is not None and self._cell is not None:
            self._row.append(clean_text(" ".join(self._cell)))
            self._cell = None
        elif tag == "tr" and self._table is not None and self._row:
            self._table.append(self._row)
            self._row = None
        elif tag == "table" and self._table is not None:
            self.sections[-1].tables.append(self._table)
            self._table = None
        elif tag in {"pre", "code"} and self._code is not None:
            code = clean_text("\n".join(self._code))
            if code and len(code) > 2:
                self.sections[-1].code_blocks.append(code)
            self._code = None
        if self._tag_stack:
            self._tag_stack.pop()

    def handle_data(self, data: str) -> None:
        text = html.unescape(data)
        if not text.strip():
            return
        current_tag = self._tag_stack[-1] if self._tag_stack else ""
        if current_tag in {"h1", "h2", "h3", "h4"}:
            self._current_text.append(text)
        elif self._cell is not None:
            self._cell.append(text)
        elif self._code is not None:
            self._code.append(text)
        else:
            self.sections[-1].text += f" {text}"


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def infer_domain(url: str) -> str:
    parts = [part for part in urlparse(url).path.split("/") if part]
    if "api" in parts:
        index = parts.index("api")
        if len(parts) > index + 2:
            return f"omie.{parts[index + 2]}"
    return "omie"


def infer_endpoint(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.rstrip("/") + "/"
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def parse_html(html_text: str, source_url: str, service_name: str | None = None) -> ServiceInfo:
    parser = StructuredHtmlParser()
    parser.feed(html_text)
    endpoint = infer_endpoint(source_url)
    name = service_name or infer_service_name(parser, source_url)
    description = infer_description(parser)
    methods = tuple(extract_methods_from_sections(parser.sections, name, endpoint, source_url))
    return ServiceInfo(
        name=name,
        endpoint=endpoint,
        domain=infer_domain(source_url),
        description=description,
        source_url=source_url,
        methods=methods,
    )


def infer_service_name(parser: StructuredHtmlParser, source_url: str) -> str:
    if parser.title:
        return parser.title
    parts = [part for part in urlparse(source_url).path.split("/") if part]
    return parts[-1].replace("_", " ").replace("-", " ").title() if parts else "Servico Omie"


def infer_description(parser: StructuredHtmlParser) -> str:
    for section in parser.sections:
        text = clean_text(section.text)
        if len(text) > 40:
            return text[:500]
    return "Necessita validacao"


def extract_methods_from_sections(
    sections: list[HtmlSection], service_name: str, endpoint: str, source_url: str
) -> list[MethodInfo]:
    candidates: dict[str, HtmlSection] = {}
    for section in sections:
        title = clean_text(section.title)
        if is_method_name(title):
            candidates.setdefault(title, section)
        for match in re.findall(r"\b[A-Z][A-Za-z0-9_]{3,}\b", section.text):
            if is_method_name(match):
                candidates.setdefault(match, section)

    methods: list[MethodInfo] = []
    for name, section in sorted(candidates.items(), key=lambda item: item[0].lower()):
        request_fields = tuple(fields_from_tables(section.tables))
        examples = tuple(extract_json_examples(section.code_blocks))
        methods.append(
            MethodInfo(
                name=name,
                endpoint=endpoint,
                service=service_name,
                domain=infer_domain(source_url),
                description=clean_text(section.text)[:500] or "Necessita validacao",
                request_fields=request_fields,
                response_fields=(),
                examples=examples,
                errors=tuple(extract_errors(section.text)),
                source_url=source_url,
            )
        )
    return methods


def is_method_name(value: str) -> bool:
    if not re.fullmatch(r"[A-Z][A-Za-z0-9_]{3,}", value):
        return False
    operation_tokens = (
        "listar",
        "consultar",
        "incluir",
        "alterar",
        "excluir",
        "upsert",
        "cancelar",
        "associar",
        "validar",
        "obter",
        "gerar",
        "lancar",
        "baixar",
    )
    return any(token in value.lower() for token in operation_tokens)


def fields_from_tables(tables: list[list[list[str]]]) -> list[FieldInfo]:
    fields: list[FieldInfo] = []
    for table in tables:
        if not table:
            continue
        headers = [cell.lower() for cell in table[0]]
        for row in table[1:]:
            if not row:
                continue
            name = row[0]
            field_type = pick_by_header(headers, row, ("tipo", "type")) or "Necessita validacao"
            required_text = pick_by_header(headers, row, ("obrig", "required")) or ""
            description = pick_by_header(headers, row, ("descr", "observ", "nome")) or "Necessita validacao"
            fields.append(
                FieldInfo(
                    name=name,
                    type=field_type,
                    required=required_text.lower() in {"sim", "s", "true", "obrigatorio", "obrigatório"},
                    description=description,
                )
            )
    return fields


def pick_by_header(headers: list[str], row: list[str], needles: tuple[str, ...]) -> str | None:
    for index, header in enumerate(headers):
        if any(needle in header for needle in needles) and index < len(row):
            return row[index]
    return None


def extract_json_examples(blocks: list[str]) -> list[str]:
    examples: list[str] = []
    for block in blocks:
        candidate = block.strip()
        if "{" not in candidate:
            continue
        start = candidate.find("{")
        end = candidate.rfind("}")
        if start >= 0 and end > start:
            snippet = candidate[start : end + 1]
            try:
                json.loads(snippet)
                examples.append(json.dumps(json.loads(snippet), ensure_ascii=False, indent=2))
            except json.JSONDecodeError:
                examples.append(snippet)
    return examples[:3]


def extract_errors(text: str) -> list[str]:
    matches = re.findall(r"(?:erro|error|fault|string|code)[^.;\n]{0,120}", text, flags=re.IGNORECASE)
    return [clean_text(match) for match in matches[:10]]
