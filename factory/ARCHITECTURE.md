---
title: "Arquitetura da Omie Knowledge Factory"
service: "Omie Knowledge Factory"
domain: "factory"
resource: "architecture"
method: "architecture"
endpoint: "N/A"
http_method: "N/A"
version: "0.1"
entity: "knowledge_factory"
related_entities:
  - Crawler
  - Parser
  - Method Extractor
  - Schema Generator
  - Graph Generator
related_methods: []
permissions:
  - "Executar somente sobre fontes oficiais públicas ou autorizadas"
complexity: "alta"
status: "arquitetura/a implementar"
source: "standards/LLM_DOCUMENT_STANDARD.md"
last_review: "2026-07-03"
tags:
  - architecture
  - omie
  - factory
keywords:
  - pipeline
  - módulos
questions:
  - "Quais módulos compõem a Factory?"
use_cases:
  - arquitetura_software
business_area: "Knowledge Engineering"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# Arquitetura

## Objetivo

Definir uma arquitetura modular para gerar automaticamente conhecimento Enterprise a partir de documentação oficial da Omie.

## Módulos

```mermaid
flowchart TD
  A["URL oficial Omie"] --> B["Crawler"]
  B --> C["Parser"]
  C --> D["Method Extractor"]
  D --> E["Schema Generator"]
  D --> F["Document Generator"]
  F --> G["FAQ Generator"]
  F --> H["Question Generator"]
  F --> I["Business Generator"]
  F --> J["Graph Generator"]
  F --> K["Chunk Generator"]
  K --> L["Embedding Metadata Generator"]
  F --> M["Coverage Generator"]
  F --> N["Dashboard Generator"]
  F --> O["Knowledge Score"]
  O --> P["Quality Gate"]
  P --> Q["GitHub PR Generator"]
```

## Contratos

- Entrada mínima: URL oficial Omie.
- Saída mínima: documentos Markdown, schemas, GraphRAG, business knowledge, perguntas, chunks, coverage, dashboard e relatório de score.
- Toda saída deve distinguir `Documentado oficialmente` de `Necessita validação`.

## Módulos independentes

- Crawler: captura conteúdo bruto autorizado.
- Parser: converte HTML/documentação em estrutura intermediária.
- Method Extractor: identifica métodos, tipos de entrada e retorno.
- Schema Generator: cria JSON Schemas iniciais.
- Business Generator: escreve contexto operacional.
- Graph Generator: cria Mermaid/GraphRAG.
- Question Generator: produz perguntas naturais.
- FAQ Generator: produz FAQ por método.
- Chunk Generator: cria chunks RAG.
- Embedding Metadata Generator: adiciona metadados de embeddings.
- Coverage Generator: atualiza matriz de cobertura.
- Dashboard Generator: atualiza métricas.
- Knowledge Score: avalia qualidade.
- GitHub PR Generator: abre PR sem merge automático.

