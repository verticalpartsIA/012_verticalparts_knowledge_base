"""Gerador de Markdown Enterprise para metodos extraidos."""

from __future__ import annotations

import json
from pathlib import Path

from models import MethodInfo, ServiceInfo, slugify, unique_method_slug_map


LANGUAGES = ("curl", "Python", "JavaScript", "TypeScript", "PHP", "C#", "Java", "Delphi", "n8n")


def generate_documents(service: ServiceInfo, output_dir: Path, dry_run: bool = False) -> list[Path]:
    target_dir = output_dir / "docs" / path_for_service(service)
    files: list[Path] = [target_dir / "README.md"]
    slugs = unique_method_slug_map(service.methods)
    files.extend(target_dir / f"{slugs[method]}.md" for method in service.methods)

    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)
        files[0].write_text(render_service_readme(service, slugs), encoding="utf-8")
        for method in service.methods:
            (target_dir / f"{slugs[method]}.md").write_text(
                render_method_document(method, method_slug=slugs[method]),
                encoding="utf-8",
            )

    files.extend(generate_service_artifacts(service, output_dir, dry_run=dry_run, slugs=slugs))
    return files


def generate_service_artifacts(
    service: ServiceInfo,
    output_dir: Path,
    *,
    dry_run: bool = False,
    slugs: dict[MethodInfo, str] | None = None,
) -> list[Path]:
    service_slug = slugify(service.name)
    slugs = slugs or unique_method_slug_map(service.methods)
    schema_dir = output_dir / "schemas" / "omie" / "financeiro" / service_slug
    files = [schema_dir / f"{slugs[method]}.schema.json" for method in service.methods]
    files.extend(
        [
            schema_dir / f"{service_slug}.schema.json",
            output_dir / "business" / "omie" / f"{service_slug}.md",
            output_dir / "graphs" / "omie" / f"{service_slug}.graph.md",
        ]
    )
    if dry_run:
        return files

    for path in files:
        path.parent.mkdir(parents=True, exist_ok=True)

    for method in service.methods:
        (schema_dir / f"{slugs[method]}.schema.json").write_text(render_method_schema(method), encoding="utf-8")
    (schema_dir / f"{service_slug}.schema.json").write_text(render_schema(service), encoding="utf-8")
    (output_dir / "business" / "omie" / f"{service_slug}.md").write_text(render_business(service), encoding="utf-8")
    (output_dir / "graphs" / "omie" / f"{service_slug}.graph.md").write_text(render_graph(service), encoding="utf-8")
    return files


def path_for_service(service: ServiceInfo) -> Path:
    parts = service.domain.split(".")
    domain = parts[-1] if parts else "omie"
    if slugify(domain) == "financas":
        domain = "financeiro"
    return Path("omie") / slugify(domain) / slugify(service.name)


def render_service_readme(service: ServiceInfo, slugs: dict[MethodInfo, str]) -> str:
    method_links = "\n".join(f"- [{method.name}]({slugs[method]}.md)" for method in service.methods)
    return f"""---
title: "{service.name}"
service: "{service.name}"
domain: "{service.domain}"
endpoint: "{service.endpoint}"
status: "Documentado automaticamente/a validar"
source: "{service.source_url}"
llm_ready: true
rag_ready: true
graph_ready: true
---

# {service.name}

## Objetivo

Documentar automaticamente o servico `{service.name}` da API Omie para uso em LLM, RAG, GraphRAG e automacoes internas da VerticalParts.

## Fonte oficial consultada

{service.source_url}

## Metodos documentados

{method_links}

## Observacoes para curadoria

- Conteudo produzido pela Autonomous Knowledge Factory sem uso de IA/LLM.
- Campos, retornos e erros extraidos por parsing deterministico devem ser validados contra a documentacao oficial antes de uso operacional critico.
- Credenciais foram omitidas por seguranca.
"""


def render_method_document(method: MethodInfo, method_slug: str | None = None) -> str:
    required_fields = [field for field in method.request_fields if field.required]
    optional_fields = [field for field in method.request_fields if not field.required]
    questions = natural_questions(method, minimum=20)
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
related_entities:
  - Fornecedores
  - Categorias
  - Bancos
  - Movimentos Financeiros
related_methods: []
permissions: "Credenciais Omie validas fora deste repositorio"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "{method.source_url}"
last_review: "2026-07-03"
tags:
  - omie
  - financeiro
  - contas-a-pagar
  - {slug}
keywords:
  - "{method.name}"
  - "contas a pagar"
questions: {len(questions)}
use_cases:
  - "Automatizar {method.name} em Contas a Pagar"
business_area: "Financeiro"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---

# {method.name}

## Objetivo

Documentar o metodo oficial `{method.name}` do servico `{method.service}` para consulta por LLMs, RAG e automacoes da VerticalParts.

## Quando utilizar

Use este metodo quando a operacao financeira desejada corresponder ao metodo oficial `{method.name}` no endpoint de Contas a Pagar.

## Quando NÃO utilizar

Nao utilize este metodo para Contas a Receber, cadastro de clientes, movimentos financeiros ja baixados ou regras de negocio nao confirmadas na fonte oficial.

## Fluxo de negocio

Fluxo de negócio: fornecedor ou documento financeiro -> titulo a pagar -> classificacao por categoria -> baixa ou manutencao do titulo -> conciliacao ou movimento financeiro relacionado.

## Entidades relacionadas

- Fornecedores
- Categorias
- Bancos
- Contas correntes
- Movimentos Financeiros
- Compras
- Notas de entrada

## Métodos relacionados

- Metodos de consulta e listagem de Contas a Pagar
- Metodos de baixa/cancelamento quando aplicavel
- Movimentos Financeiros
- Categorias
- Bancos

## Pre-requisitos

- Possuir credenciais Omie validas no ambiente seguro de execucao.
- Nao registrar `app_key`, `app_secret`, tokens, senhas ou dados reais neste repositorio.
- Validar payload contra a documentacao oficial antes de uso em producao.

## Payload ou conteudo tecnico principal

Endpoint: `{method.endpoint}`

Descricao extraida da fonte oficial:

{method.description or "Necessita validacao."}

## Campos obrigatorios

{render_fields(required_fields)}

## Campos opcionais

{render_fields(optional_fields)}

## Regras de negocio

- Contas a Pagar representa obrigacoes financeiras da empresa com fornecedores ou despesas.
- O metodo deve ser escolhido conforme a intencao: incluir, alterar, consultar, listar, excluir, baixar, cancelar ou fazer upsert.
- Regras especificas de validacao fiscal, centro de custo, categoria e vencimento necessitam validacao operacional.

## Validacoes

- Confirmar campos obrigatorios.
- Confirmar tipos e formatos aceitos pela Omie.
- Conferir se o titulo ainda pode ser alterado, excluido, baixado ou cancelado.
- Validar se a operacao se aplica a lote quando o metodo mencionar lote.

## Restricoes

- Exemplos sao ficticios.
- Credenciais foram omitidas por seguranca.
- Campos nao extraidos com seguranca devem ser tratados como "Necessita validacao".

## Resposta esperada

{render_response(method)}

## Erros comuns

{render_errors(method)}

## Como resolver os erros

- Revisar campos obrigatorios e estrutura do `param`.
- Conferir codigo interno, codigo Omie e identificadores financeiros.
- Validar credenciais apenas em ambiente seguro.
- Consultar a fonte oficial quando o parser marcar algum detalhe como pendente.

## Casos de uso

- Automatizar a operacao `{method.name}` em rotinas financeiras.
- Apoiar uma LLM na escolha do metodo correto para duvidas sobre Contas a Pagar.
- Preparar payloads ficticios para testes sem dados reais.

## Exemplos completos

{render_examples(method)}

## FAQ

{render_faq(method, questions)}

## Perguntas naturais

{render_questions(questions)}

## Tags para RAG

- omie
- financeiro
- contas-a-pagar
- {slug}
- enterprise-rag
- graphrag

## Fonte oficial consultada

{method.source_url}
"""


def render_method_schema(method: MethodInfo) -> str:
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": method.name,
        "type": "object",
        "properties": {
            "call": {"type": "string", "const": method.name},
            "param": {"type": "array", "items": {"type": "object"}},
        },
        "required": ["call", "param"],
        "additionalProperties": True,
    }
    return json.dumps(schema, ensure_ascii=False, indent=2) + "\n"


def render_schema(service: ServiceInfo) -> str:
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": service.name,
        "type": "object",
        "properties": {
            "call": {"type": "string", "enum": [method.name for method in service.methods]},
            "param": {"type": "array", "items": {"type": "object"}},
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

Registrar a visao de negocio extraida automaticamente para o servico `{service.name}`.

## Fluxo financeiro

Contas a Pagar organiza obrigacoes financeiras da empresa, normalmente relacionadas a fornecedores, compras, despesas, categorias, bancos e movimentos financeiros.

## Metodos identificados

{methods}

## Observacoes

Conteudo gerado por parsing deterministico. Regras de negocio detalhadas ainda precisam de validacao humana antes de uso em producao.
"""


def render_graph(service: ServiceInfo) -> str:
    slugs = unique_method_slug_map(service.methods)
    lines = ["```mermaid", "graph TD", f'  S["{service.name}"]']
    for entity in ("Fornecedores", "Categorias", "Bancos", "Movimentos Financeiros"):
        lines.append(f'  S --> {slugify(entity)}["{entity}"]')
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
        return "- Necessita validacao."
    return "\n".join(f"- {error}" for error in method.errors)


def render_examples(method: MethodInfo) -> str:
    payload = render_payload(method)
    sections = []
    for language in LANGUAGES:
        sections.append(f"### {language}\n\n{example_for(language, method, payload)}")
    return "\n\n".join(sections)


def render_payload(method: MethodInfo) -> str:
    return json.dumps(
        {
            "call": method.name,
            "param": [
                {
                    "codigo_lancamento_integracao": "PAG-FICTICIO-001",
                    "codigo_cliente_fornecedor": 123456,
                    "data_vencimento": "31/12/2026",
                    "valor_documento": 100.0,
                    "codigo_categoria": "9.99.99",
                    "observacao": "Exemplo ficticio gerado pela Factory",
                }
            ],
        },
        ensure_ascii=False,
        indent=2,
    )


def example_for(language: str, method: MethodInfo, payload: str) -> str:
    if language == "curl":
        return f"""```bash
curl -X POST "{method.endpoint}" \\
  -H "Content-Type: application/json" \\
  -d '{payload}'
```"""
    if language == "Python":
        return f"""```python
import requests

payload = {payload}
response = requests.post("{method.endpoint}", json=payload, timeout=30)
print(response.json())
```"""
    if language == "JavaScript":
        return f"""```javascript
const payload = {payload};
const response = await fetch("{method.endpoint}", {{
  method: "POST",
  headers: {{ "Content-Type": "application/json" }},
  body: JSON.stringify(payload)
}});
console.log(await response.json());
```"""
    if language == "TypeScript":
        return f"""```typescript
const payload: Record<string, unknown> = {payload};
const response = await fetch("{method.endpoint}", {{
  method: "POST",
  headers: {{ "Content-Type": "application/json" }},
  body: JSON.stringify(payload)
}});
console.log(await response.json());
```"""
    if language == "PHP":
        return f"""```php
$payload = {json.dumps({"call": method.name, "param": [{"exemplo": "ficticio"}]}, ensure_ascii=False)};
// Enviar via cliente HTTP configurado em ambiente seguro.
```"""
    if language == "C#":
        return f"""```csharp
var payload = @"{payload.replace('"', '\\"')}";
// Enviar com HttpClient configurado em ambiente seguro.
```"""
    if language == "Java":
        return f"""```java
String payload = \"{payload.replace('"', '\\"').replace(chr(10), ' ')}\";
// Enviar com cliente HTTP configurado em ambiente seguro.
```"""
    if language == "Delphi":
        return f"""```pascal
Payload := '{payload.replace("'", "''")}';
// Enviar com componente HTTP configurado em ambiente seguro.
```"""
    return f"""```json
{{
  "node": "HTTP Request",
  "method": "POST",
  "url": "{method.endpoint}",
  "body": {payload}
}}
```"""


def natural_questions(method: MethodInfo, minimum: int = 20) -> list[str]:
    base = method.name
    service = method.service
    questions = [
        f"Quando devo usar o metodo {base}?",
        f"Quais campos sao obrigatorios para {base}?",
        f"Qual endpoint devo chamar para {base}?",
        f"Que retorno esperar do metodo {base}?",
        f"Como {base} se relaciona com {service}?",
        f"{base} serve para fornecedor?",
        f"{base} altera algum movimento financeiro?",
        f"{base} exige categoria financeira?",
        f"Posso usar {base} com dados ficticios em teste?",
        f"Quais erros comuns acontecem em {base}?",
        f"Como validar payload antes de chamar {base}?",
        f"{base} pode ser usado em lote?",
        f"{base} depende de banco ou conta corrente?",
        f"Como uma LLM escolhe {base}?",
        f"Quando nao devo usar {base}?",
        f"{base} substitui consulta de movimentos financeiros?",
        f"{base} precisa de codigo Omie?",
        f"{base} precisa de codigo interno?",
        f"Onde encontro a fonte oficial de {base}?",
        f"Quais tags RAG ajudam a recuperar {base}?",
    ]
    while len(questions) < minimum:
        questions.append(f"Pergunta adicional {len(questions) + 1} sobre {base}?")
    return questions[:minimum]


def render_faq(method: MethodInfo, questions: list[str]) -> str:
    return "\n\n".join(
        f"### {index}. {question}\n\nResposta: Necessita validacao contra a fonte oficial Omie."
        for index, question in enumerate(questions, start=1)
    )


def render_questions(questions: list[str]) -> str:
    return "\n".join(f"- {question}" for question in questions)
