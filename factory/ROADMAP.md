---
title: "Roadmap da Omie Knowledge Factory"
service: "Omie Knowledge Factory"
domain: "factory"
resource: "roadmap"
method: "factory_roadmap"
endpoint: "N/A"
http_method: "N/A"
version: "0.1"
entity: "factory_roadmap"
related_entities:
  - Pipeline
  - Coverage
related_methods: []
permissions: []
complexity: "media"
status: "arquitetura/a implementar"
source: "ROADMAP.md"
last_review: "2026-07-03"
tags:
  - roadmap
  - factory
keywords:
  - fases
questions:
  - "Qual é o plano de implementação da Factory?"
use_cases:
  - planejamento
business_area: "Knowledge Engineering"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# Roadmap da Factory

## Fase 1 — Arquitetura

- Objetivo: definir módulos, contratos e templates.
- Status: em andamento.

## Fase 2 — Implementação offline

- Objetivo: parser e geradores operando com fixtures locais.
- Status: planejado.

## Fase 3 — Crawler controlado

- Objetivo: coleta de fonte oficial com cache e auditoria.
- Status: planejado.

## Fase 4 — Quality Gate completo

- Objetivo: validar Markdown, YAML, JSON, schemas, chunks e score.
- Status: planejado.

## Fase 5 — PR automático

- Objetivo: criar branches e PRs automaticamente sem merge.
- Status: planejado.

