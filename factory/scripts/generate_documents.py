"""Gerador de Markdown Enterprise para metodos extraidos."""

from __future__ import annotations

from pathlib import Path

from models import MethodInfo, ServiceInfo, slugify, unique_method_slug_map


def generate_documents(service: ServiceInfo, output_dir: Path, dry_run: bool = False) -> list[Path]:
    target_dir = output_dir / "docs" / path_for_service(service)
    files: list[Path] = []
    slugs = unique_method_slug_map(service.methods)
    for method in service.methods:
        path = target_dir / f"{slugs[method]}.md"
        files.append(path)
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_method_document(method, method_slug=slugs[method]), encoding="utf-8")
    files.extend(generate_service_artifacts(service, output_dir, dry_run=dry_run))
    return files


def generate_service_artifacts(service: ServiceInfo, output_dir: Path, dry_run: bool = False) -> list[Path]:
    service_slug = slugify(service.name)
    files = [
        output_dir / "schemas" / "omie" / service_slug / f"{service_slug}.schema.json",
        output_dir / "business" / "omie" / f"{service_slug}.md",
        output_dir / "graphs" / "omie" / f"{service_slug}.graph.md",
    ]
    if dry_run:
        return files

    for path in files:
        path.parent.mkdir(parents=True, exist_ok=True)

    files[0].write_text(render_schema(service), encoding="utf-8")
    files[1].write_text(render_business(service), encoding="utf-8")
    files[2].write_text(render_graph(service), encoding="utf-8")
    return files


def path_for_service(service: ServiceInfo) -> Path:
    parts = service.domain.split(".")
    domain = parts[-1] if parts else "omie"
    return Path("omie") / slugify(domain) / slugify(service.name)


def render_method_document(method: MethodInfo, method_slug: str | None = None) -> str:
    required_fields = [field for field in method.request_fields if field.required]
    optional_fields = [field for field in method.request_fields if not field.required]
    questions = natural_questions(method)
    slug = method_slug or method.slug
    return f"""---
title: "{method.name}"
service: "{method.service}"
domain: "{method.domain}"
resource: "{method.service}"
method: "{method.name}"
endpoint: "{method.endpoint}"
http_method: "POST"
version: "v1"
entity: "{method.service}"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "{method.source_url}"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - {slug}
keywords:
  - "{method.name}"
questions: {len(questions)}
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# {method.name}

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `{method.name}` do servico `{method.service}`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- {method.service}

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `{method.endpoint}`

Descricao extraida:

{method.description or "Necessita validacao."}

## Campos obrigatorios

{render_fields(required_fields)}

## Campos opcionais

{render_fields(optional_fields)}

## Regras de negocio

Necessita validacao contra a documentacao oficial e regras operacionais da VerticalParts.

## Validacoes

- Conferir campos obrigatorios antes da chamada.
- Conferir tipos informados pela documentacao oficial.

## Restricoes

- Exemplos sao ficticios.
- Credenciais foram omitidas por seguranca.

## Resposta esperada

{render_response(method)}

## Erros comuns

{render_errors(method)}

## Como resolver os erros

- Validar payload contra a documentacao oficial.
- Conferir credenciais no ambiente seguro de execucao, sem registrar valores neste repositorio.

## Casos de uso

- Automatizar a operacao `{method.name}` no contexto do servico `{method.service}`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{render_example(method)}
```

## FAQ

{render_faq(method)}

## Perguntas naturais

{render_questions(questions)}

## Tags para RAG

- omie
- factory-mvp
- {slug}
- enterprise-rag

## Fonte oficial consultada

{method.source_url}
"""


def render_schema(service: ServiceInfo) -> str:
    import json

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": service.name,
        "type": "object",
        "properties": {
            "call": {"type": "string", "enum": [method.name for method in service.methods]},
            "param": {"type": "array"},
        },
        "required": ["call", "param"],
        "additionalProperties": True,
    }
    return json.dumps(schema, ensure_ascii=False, indent=2) + "\n"


def render_business(service: ServiceInfo) -> str:
    methods = "\n".join(f"- `{method.name}`" for method in service.methods) or "- Necessita validacao."
    return f"""# Business Knowledge - {service.name}

Fonte oficial: {service.source_url}

## Objetivo

Registrar a visao de negocio minima extraida automaticamente para o servico `{service.name}`.

## Metodos identificados

{methods}

## Observacoes

Conteudo gerado por parsing deterministico. Regras de negocio detalhadas ainda precisam de validacao humana.
"""


def render_graph(service: ServiceInfo) -> str:
    lines = ["```mermaid", "graph TD", f'  S["{service.name}"]']
    slugs = unique_method_slug_map(service.methods)
    for method in service.methods:
        lines.append(f'  S --> {slugs[method]}["{method.name}"]')
    lines.append("```")
    return "# GraphRAG - " + service.name + "\n\n" + "\n".join(lines) + "\n"


def render_fields(fields: list) -> str:
    if not fields:
        return "Necessita validacao."
    lines = ["| Campo | Tipo | Descricao |", "|---|---|---|"]
    lines.extend(f"| `{field.name}` | {field.type} | {field.description} |" for field in fields)
    return "\n".join(lines)


def render_response(method: MethodInfo) -> str:
    if method.response_fields:
        return render_fields(list(method.response_fields))
    return "Necessita validacao."


def render_errors(method: MethodInfo) -> str:
    if not method.errors:
        return "Necessita validacao."
    return "\n".join(f"- {error}" for error in method.errors)


def render_example(method: MethodInfo) -> str:
    if method.examples:
        return method.examples[0]
    return '{\n  "call": "' + method.name + '",\n  "param": []\n}'


def natural_questions(method: MethodInfo) -> list[str]:
    base = method.name
    service = method.service
    return [
        f"Quando devo usar o metodo {base}?",
        f"Quais campos sao obrigatorios para {base}?",
        f"Qual endpoint devo chamar para {base}?",
        f"Que retorno esperar do metodo {base}?",
        f"Como {base} se relaciona com {service}?",
    ]


def render_faq(method: MethodInfo) -> str:
    return "\n".join(f"### {question}\n\nNecessita validacao." for question in natural_questions(method))


def render_questions(questions: list[str]) -> str:
    return "\n".join(f"- {question}" for question in questions)
