---
title: "Workflow da Omie Knowledge Factory"
service: "Omie Knowledge Factory"
domain: "factory.workflow"
resource: "workflow"
method: "pipeline"
endpoint: "N/A"
http_method: "N/A"
version: "0.1"
entity: "factory_workflow"
related_entities:
  - Pipeline
  - Quality Gate
related_methods: []
permissions: []
complexity: "alta"
status: "arquitetura/a implementar"
source: "factory/ARCHITECTURE.md"
last_review: "2026-07-03"
tags:
  - workflow
  - factory
keywords:
  - pipeline
questions:
  - "Quais etapas a Factory executa?"
use_cases:
  - implementacao_futura
business_area: "Knowledge Engineering"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# Workflow

| Etapa | Entrada | Saída | Dependências | Tempo esperado | Erros possíveis | Recuperação |
| --- | --- | --- | --- | --- | --- | --- |
| Crawler | URL oficial | Snapshot bruto | Rede, fonte oficial | 5-30s | Timeout, 404, HTML alterado | Cache, retry, marcar lacuna |
| Parser | Snapshot | AST/document model | Crawler | 1-5s | Estrutura inesperada | Fallback por seletores alternativos |
| Method Extractor | AST | Lista de métodos | Parser | 1-5s | Método ambíguo | Falhar e pedir validação |
| Schema Generator | Métodos/tipos | JSON Schemas | Extractor | 1-10s | Tipo ausente | Schema inicial permissivo |
| Document Generator | Métodos + templates | Markdown | Templates | 5-30s | Campo obrigatório ausente | Marcar Necessita validação |
| Business Generator | Entidades | Business doc | Config/domínio | 5-15s | Relação desconhecida | Usar relação planejada |
| Graph Generator | Entidades/relações | Mermaid | Business | 1-5s | Grafo desconexo | Alertar no quality gate |
| Question Generator | Métodos | Dataset | Config questions | 5-20s | Duplicação | Deduplicar e regenerar |
| FAQ Generator | Métodos | FAQ | Templates | 5-20s | Resposta especulativa | Marcar validação |
| Chunk Generator | Markdown | Chunks | RAG config | 5-20s | Chunk curto/longo | Rechunk automático |
| Embedding Metadata | Chunks | Metadados | Embeddings config | 1-5s | Versão ausente | Falhar quality gate |
| Coverage Generator | Serviço | Matriz cobertura | Service list | 1-10s | Serviço duplicado | Normalizar endpoint |
| Dashboard Generator | Métricas | Dashboard | Reports | 1-5s | Contagem divergente | Recontar arquivos |
| Knowledge Score | Docs | Score | Scripts | 1-5s | Lacunas | Falhar quality gate |
| GitHub PR Generator | Branch | PR | gh/GitHub | 5-30s | Auth/permissão | Parar sem merge |

