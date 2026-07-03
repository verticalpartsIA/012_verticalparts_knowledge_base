# v1.0.0 — Autonomous Knowledge Factory

## Objetivo

Permitir que a Factory receba uma lista de URLs da documentação Omie e gere automaticamente documentação, schemas, perguntas, chunks, graphs, business knowledge, coverage e dashboard.

## Visão

A v1.0.0 deve transformar a Omie Knowledge Factory em um pipeline autônomo, reproduzível e auditável. A Factory deve operar a partir de um service registry, executar processamento em lote, gerar artefatos em saída isolada e preparar mudanças para revisão humana antes do merge.

## Épicos

### 1. Service Registry

- Objetivo: centralizar a lista de serviços Omie, status, prioridades e dependências.
- Entregáveis: `factory/registry/omie_services.yaml`, validador de campos, filtros e recomendação de próximo serviço.
- Critérios de aceite: registry carrega 137 serviços, valida campos obrigatórios e permite filtros por domínio, status e prioridade.
- Riscos: divergência entre registry e coverage; nomes duplicados.
- Dependências: matriz `coverage/omie_api_coverage.md`.

### 2. Batch Runner

- Objetivo: executar a Factory para múltiplos serviços com limite e filtros.
- Entregáveis: `factory/scripts/batch_runner.py`, relatório de execução e modo dry-run.
- Critérios de aceite: batch respeita `--limit`, `--domain`, `--priority` e não processa todos os serviços por acidente.
- Riscos: excesso de chamadas externas; falha parcial interromper lote inteiro.
- Dependências: Service Registry e CLI.

### 3. Parser Robusto

- Objetivo: melhorar extração de métodos, parâmetros, exemplos, retornos e erros.
- Entregáveis: parser resiliente a variações de HTML, fixtures oficiais e testes de regressão.
- Critérios de aceite: extrai métodos dos serviços priorizados sem falsos positivos relevantes.
- Riscos: mudanças no HTML oficial; tabelas inconsistentes.
- Dependências: crawler, fixtures e registry.

### 4. Template Engine

- Objetivo: separar templates de lógica Python e suportar múltiplos padrões de documento.
- Entregáveis: renderização baseada em templates versionados e validação de placeholders.
- Critérios de aceite: documentos gerados seguem `standards/LLM_DOCUMENT_STANDARD.md`.
- Riscos: templates incompletos gerarem docs inconsistentes.
- Dependências: Document Generator e padrões Enterprise.

### 5. Schema Generator avançado

- Objetivo: gerar JSON Schemas mais fiéis aos parâmetros oficiais.
- Entregáveis: schemas por método, inferência de tipos e campos obrigatórios.
- Critérios de aceite: schemas JSON válidos e coerentes com payloads extraídos.
- Riscos: tipos ambíguos na fonte oficial.
- Dependências: Parser Robusto.

### 6. FAQ Generator determinístico

- Objetivo: gerar FAQs úteis sem IA/LLM.
- Entregáveis: perguntas/respostas por método baseadas em campos e operação.
- Critérios de aceite: FAQ presente em todos os documentos gerados.
- Riscos: respostas genéricas demais quando a fonte for incompleta.
- Dependências: Parser Robusto e Template Engine.

### 7. Question Generator avançado

- Objetivo: gerar datasets de perguntas naturais sem repetição.
- Entregáveis: perguntas por método, serviço e entidade, com deduplicação.
- Critérios de aceite: datasets válidos, sem duplicidade e com cobertura das operações.
- Riscos: variações pobres de linguagem.
- Dependências: Method Extractor.

### 8. Graph Generator avançado

- Objetivo: criar GraphRAG com entidades, métodos, domínios e dependências.
- Entregáveis: Mermaid e estrutura intermediária de grafo.
- Critérios de aceite: graphs renderizam e representam relações principais.
- Riscos: relacionamentos inferidos incorretamente.
- Dependências: Registry e Business Knowledge Generator.

### 9. Business Knowledge Generator

- Objetivo: gerar visão de negócio mínima e relações operacionais.
- Entregáveis: documentos em `business/` por serviço.
- Critérios de aceite: business docs indicam fluxo, entidades e dependências a validar.
- Riscos: excesso de inferência sem fonte oficial.
- Dependências: Registry e parser.

### 10. Chunking Engine

- Objetivo: dividir documentos em chunks estáveis para RAG.
- Entregáveis: chunks por método/seção e índice de chunks.
- Critérios de aceite: chunks possuem metadados completos e não misturam métodos diferentes.
- Riscos: chunks curtos ou longos demais.
- Dependências: documentos gerados.

### 11. Coverage Updater

- Objetivo: atualizar cobertura com base no registry e artefatos gerados.
- Entregáveis: atualização automática de `coverage/omie_api_coverage.md`.
- Critérios de aceite: percentuais refletem serviços concluídos.
- Riscos: marcar serviço como concluído sem revisão humana.
- Dependências: Quality Gate.

### 12. Dashboard Updater

- Objetivo: consolidar métricas do projeto após cada execução.
- Entregáveis: atualização automática de `reports/dashboard.md`.
- Critérios de aceite: dashboard informa versão, serviços, métodos, perguntas, chunks e score.
- Riscos: contagem inconsistente entre diretórios.
- Dependências: Coverage Updater e Knowledge Score.

### 13. Quality Gate

- Objetivo: impedir entrada de artefatos inválidos.
- Entregáveis: validação Markdown, YAML, JSON, schemas, chunks, perguntas e segredos.
- Critérios de aceite: pipeline falha em inconsistências críticas.
- Riscos: falso positivo bloquear entrega.
- Dependências: GitHub Actions e testes.

### 14. PR Automation

- Objetivo: preparar branch, commit e PR para cada lote gerado.
- Entregáveis: automação segura com relatório de mudanças.
- Critérios de aceite: PRs são abertos sem merge automático e sem credenciais.
- Riscos: automação commitar saída indevida ou cache.
- Dependências: Quality Gate e Batch Runner.

### 15. Release Automation

- Objetivo: padronizar tags e releases após merges aprovados.
- Entregáveis: notas de release e tags versionadas.
- Critérios de aceite: release resume artefatos, métricas e segurança.
- Riscos: versionamento desalinhado ao conteúdo.
- Dependências: PR Automation e validação humana.
