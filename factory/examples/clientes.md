---
title: "Exemplo da Factory: Clientes"
service: "Omie Knowledge Factory"
domain: "factory.examples"
resource: "clientes"
method: "example"
endpoint: "https://app.omie.com.br/api/v1/geral/clientes/"
http_method: "POST"
version: "0.1"
entity: "factory_example"
related_entities:
  - Clientes
  - Fornecedores
  - Transportadoras
related_methods: []
permissions:
  - "Sem credenciais reais"
complexity: "media"
status: "exemplo/a implementar"
source: "https://app.omie.com.br/api/v1/geral/clientes/"
last_review: "2026-07-03"
tags:
  - factory
  - exemplo
  - clientes
keywords:
  - clientes
  - factory
questions:
  - "Como a Factory processaria Clientes?"
use_cases:
  - exemplo_de_pipeline
business_area: "Knowledge Engineering"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# Exemplo: Clientes

## Objetivo

Demonstrar como a Factory deverá receber a URL oficial de Clientes e produzir os artefatos Enterprise.

## Entrada

```yaml
service_url: https://app.omie.com.br/api/v1/geral/clientes/
service_id: clientes
domain: omie.geral
```

## Saída esperada

- `docs/omie/geral/clientes/`
- `schemas/omie/geral/clientes/`
- `graphs/omie/clientes.graph.md`
- `business/omie/clientes.md`
- `datasets/questions/clientes.json`
- `rag/chunks/clientes/`
- `reports/knowledge_score.md`
- PR no GitHub sem merge automático.

## Fluxo esperado

1. Crawler coleta a fonte oficial.
2. Parser normaliza a página.
3. Extractor identifica métodos.
4. Geradores renderizam templates.
5. Quality gate valida.
6. GitHub PR Generator abre a revisão.

