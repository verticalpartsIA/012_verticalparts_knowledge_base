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

A arquitetura inicial está em `factory/`. A Factory já possui MVP funcional e agora passa a contar com descoberta dinâmica de serviços públicos da Omie, sem atualizar automaticamente o registry oficial.

### Dynamic Service Discovery

A partir da v0.7.0, a Factory consegue descobrir serviços públicos da Omie diretamente em `https://developer.omie.com.br/service-list/`, gerar `factory/registry/omie_services.generated.yaml` e comparar com o registry oficial sem atualizá-lo automaticamente.

```bash
python factory/scripts/main.py --discover
python factory/scripts/main.py --compare-registry
python factory/scripts/main.py --refresh-registry
```

O relatório de descoberta fica em `factory/reports/discovery_report.md`.

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
