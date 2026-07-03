---
title: "SDD da Omie Knowledge Factory"
service: "Omie Knowledge Factory"
domain: "factory"
resource: "sdd"
method: "factory_sdd"
endpoint: "N/A"
http_method: "N/A"
version: "0.1"
entity: "factory_design"
related_entities:
  - Pipeline
  - Templates
  - Quality Gate
related_methods: []
permissions:
  - "Sem execução de scraping nesta etapa"
complexity: "alta"
status: "arquitetura/a implementar"
source: "standards/LLM_DOCUMENT_STANDARD.md"
last_review: "2026-07-03"
tags:
  - sdd
  - factory
  - pipeline
keywords:
  - desenho técnico
questions:
  - "Como a Factory será implementada?"
use_cases:
  - desenho_tecnico
business_area: "Knowledge Engineering"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# FACTORY SDD

## Objetivo

Descrever o desenho técnico da Factory sem implementar crawler ou geração automática nesta fase.

## Desenho técnico

A Factory deve usar uma estrutura intermediária canônica:

```json
{
  "service": "LancamentoContaReceber",
  "domain": "omie.financeiro",
  "endpoint": "https://app.omie.com.br/api/v1/financas/contareceber/",
  "methods": []
}
```

## Estratégia

1. Normalizar fonte oficial.
2. Extrair métodos.
3. Validar contratos.
4. Renderizar templates.
5. Gerar artefatos.
6. Rodar quality gate.
7. Abrir PR.

## Falhas esperadas

- HTML da Omie alterado.
- Método sem tipo de retorno explícito.
- Campos condicionais não documentados.
- Duplicidade de perguntas.
- Chunk fora da faixa de tokens.

## Recuperação

- Salvar snapshot bruto em diretório ignorado.
- Registrar lacunas como `Necessita validação`.
- Falhar o quality gate em caso de ambiguidade estrutural.

