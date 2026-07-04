# VerticalParts Knowledge Base

Base de conhecimento Enterprise RAG/LLM da VerticalParts para documentar APIs, dominios de negocio, grafos de conhecimento, chunks, embeddings, schemas, testes e estrategias de recuperacao.

## Arquitetura

- `docs/`: conhecimento tecnico fonte, com YAML obrigatorio.
- `standards/`: padroes mestres para documentos LLM-ready.
- `business/`: conhecimento de negocio por dominio.
- `graphs/`: relacoes GraphRAG em Mermaid.
- `rag/`: chunking, retrieval, reranking e estrategias hibridas.
- `embeddings/`: orientacoes de modelos e versionamento.
- `schemas/`: contratos JSON iniciais.
- `datasets/questions/`: perguntas naturais para avaliacao e treinamento.
- `tests/knowledge/`: testes automatizados de qualidade documental.
- `scripts/`: automacoes de geracao, score e suporte.
- `reports/`: saidas geradas por validadores.

## Objetivos

- Criar conhecimento especializado para LLMs, nao apenas documentacao humana.
- Padronizar metadados para RAG, GraphRAG e embeddings.
- Separar informacao documentada oficialmente de conteudo que necessita validacao.
- Evitar credenciais, segredos ou senhas no repositorio.

## Omie Knowledge Factory

A partir da fase v0.3.0, a VerticalParts Knowledge Base passa a ser orientada por uma Factory de geração automática. O objetivo é transformar uma URL oficial da documentação Omie em uma base Enterprise completa para LLMs, incluindo `docs`, `schemas`, `graphs`, `business`, `datasets`, `rag`, `reports`, `coverage` e pull request de revisão.

A arquitetura inicial está em `factory/`. Nesta etapa a Factory ainda não executa crawler, scraping ou geração automática real; ela define módulos, contratos, templates, configurações, quality gate e workflow para implementação posterior.

### Generation Planner

O Generation Planner calcula de forma determinística qual serviço deve ser documentado primeiro, usando domínio, dependências, criticidade financeira, impacto no ERP, cobertura, prioridade de registry e relações entre serviços.

```bash
python factory/scripts/main.py --plan
python factory/scripts/main.py --next-best-service
python factory/scripts/main.py --dependency-graph
```

Relatórios gerados:

- `factory/reports/planner_report.md`
- `factory/reports/documentation_plan.md`
- `factory/reports/service_dependency_graph.md`

### Execution Engine

O Execution Engine executa deterministicamente o próximo serviço recomendado pelo planner, com validação de estado, histórico, quality gate básico e relatório de execução. Ele não abre pull requests, não faz commits automáticos, não usa IA/LLM e não altera documentação Enterprise existente em modo `--dry-run`.

```bash
python factory/scripts/main.py --execute-next --dry-run
python factory/scripts/main.py --execute-service financas_contas_a_pagar_lancamentos --dry-run
python factory/scripts/main.py --status
python factory/scripts/main.py --history
```

Relatórios e estado:

- `factory/reports/execution_report.md`
- `factory/reports/execution_history.json`
- `factory/state/factory_state.json`

## Primeiro domínio documentado em detalhe

O primeiro dominio detalhado e `Omie Geral > Clientes, Fornecedores e Transportadoras`, baseado na fonte oficial `https://app.omie.com.br/api/v1/geral/clientes/`.

## Domínios documentados em detalhe

- Omie Geral > Clientes, Fornecedores e Transportadoras.
- Omie Financeiro > Contas a Receber.

## Estrutura

Consulte `standards/LLM_DOCUMENT_STANDARD.md` para o formato obrigatorio de Markdown, YAML, FAQ, exemplos, tags, chunking, embeddings, RAG e GraphRAG.

## Roadmap

1. Consolidar ClientesCadastro.
2. Expandir Financeiro.
3. Expandir Vendas.
4. Expandir Servicos.
5. Expandir Fiscal.
6. Criar avaliadores automaticos por dominio.

## Como contribuir

- Criar branch por dominio ou padrao.
- Seguir `standards/LLM_DOCUMENT_STANDARD.md`.
- Rodar testes e score antes de abrir PR.
- Marcar lacunas como "Necessita validacao".

## Como gerar documentação

```bash
python scripts/generate_enterprise_omie_clientes.py
```

## Como gerar embeddings

1. Escolha o modelo em `embeddings/README.md`.
2. Leia chunks em `rag/chunks/`.
3. Preserve metadados YAML.
4. Grave `embedding_version`.

## Como indexar no Qdrant

- Criar colecao por dominio.
- Usar filtros por `service`, `method`, `domain`, `status` e `embedding_version`.
- Indexar chunks de `rag/chunks/clientes/`.

## Como indexar no pgvector

- Criar tabela com texto, vetor e metadados JSONB.
- Usar indices vetoriais e filtros JSONB para dominio e metodo.
- Registrar hash do chunk para reindexacao incremental.

## Como integrar com LangChain

- Usar loader Markdown.
- Separar YAML como metadata.
- Aplicar retriever hibrido e reranker.

## Como integrar com LlamaIndex

- Carregar chunks como nodes.
- Mapear YAML para metadata.
- Usar graph store quando consumir `graphs/`.

## Como integrar com Semantic Kernel

- Registrar chunks como memoria semantica.
- Criar plugins por dominio Omie.
- Restringir respostas as fontes recuperadas.

## Como integrar com Haystack

- Usar document store vetorial.
- Aplicar BM25 + embedding retriever.
- Rerankear por metodo e status.

## Qualidade

```bash
pytest tests/knowledge
python scripts/knowledge_score.py
```
## Omie Commercial Suite Knowledge Base

A branch `feature/omie-commercial-suite` usa a Autonomous Knowledge Factory para gerar conhecimento técnico e Business Knowledge dos módulos estratégicos de venda, compra, faturamento, fiscal, produtos, estoque e financeiro.

Serviços cobertos nesta entrega:

- Pedido de Venda
- Pedido de Compra
- Pedido de Venda - Faturamento
- NF-e Consultas
- NF-e Importar
- NFS-e Consultas
- Produtos
- Consulta Estoque
- Movimento Estoque
- Contas a Receber existente
- Contas a Pagar Lançamentos
- Ordens de Serviço Faturamento

Aprovação de pedido de venda e aprovação de pedido de compra foram registradas como Business Knowledge porque não foi identificado endpoint oficial específico na documentação pública Omie.
