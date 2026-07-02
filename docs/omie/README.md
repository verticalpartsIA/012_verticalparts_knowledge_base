---
title: "Omie API - Indice"
service: "Necessita validação contra documentação oficial Omie"
domain: "omie"
resource: "omie"
method: "indice"
endpoint: "Necessita validação contra documentação oficial Omie"
http_method: "Necessita validação"
version: "1"
entity: "api"
related_entities: []
related_methods: []
permissions:
  - "Necessita credenciais Omie validas fora do repositorio"
complexity: "inicial"
status: "inicial/a validar"
source: "Necessita validação contra documentação oficial Omie"
last_review: "2026-07-02"
tags:
  - omie
  - omie
  - inicial
keywords:
  - Omie API - Indice
questions:
  - "Como validar oficialmente Omie API - Indice na Omie?"
use_cases:
  - triagem_documental
business_area: "ERP / Necessita validação"
llm_ready: false
rag_ready: false
graph_ready: false
embedding_version: 1
---
# API Omie

Esta área organiza a documentação inicial da API Omie para uso em RAG e por agentes LLM da VerticalParts.

## Domínios

- `geral`: entidades base, como clientes, fornecedores e transportadoras.
- `financeiro`: contas a pagar, contas a receber e movimentos financeiros.
- `vendas`: pedidos, processos comerciais e documentos relacionados.
- `estoque`: produtos, saldos e movimentações.
- `servicos`: ordens de serviço e prestação de serviços.
- `fiscal`: documentos fiscais e obrigações relacionadas.

## Status dos Documentos

Os documentos iniciais usam `status: inicial/a validar`. Esse status indica que o conteúdo serve como ponto de partida e deve ser validado contra documentação oficial da Omie, testes controlados e conhecimento interno.

## Objetivo

Organizar conhecimento sobre Omie API - Indice em formato reutilizavel por LLMs, RAG e GraphRAG.

## Quando utilizar

Use este documento quando a pergunta exigir contexto geral, indice de navegacao ou ponto de entrada para documentos detalhados.

## Quando NÃO utilizar

Nao use este documento como contrato final de payload quando existir um documento de metodo mais especifico.

## Fluxo de negócio

O usuario formula uma pergunta, a LLM identifica o dominio, consulta este indice e entao navega para o documento detalhado mais adequado.

## Entidades relacionadas

- Cliente
- Fornecedor
- Transportadora

## Métodos relacionados

- `ConsultarCliente`
- `IncluirCliente`
- `AlterarCliente`
- `ListarClientes`

## Exemplos completos

### curl

Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

### Python

Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

### JavaScript

Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

## FAQ

### 1. Este documento substitui os metodos detalhados?

Nao. Ele direciona a LLM para o documento especifico.

### 2. O conteudo e oficial?

Partes derivadas da fonte oficial sao marcadas no documento. Lacunas devem ser tratadas como "Necessita validacao".

## Perguntas naturais

- Onde encontro os metodos de ClientesCadastro?
- Qual documento devo consultar para payload?
- O que ainda necessita validacao?

## Tags para RAG

- omie
- indice
- enterprise-rag
- graphrag

## Casos de uso

- Navegacao por dominio.
- Recuperacao RAG.
- Expansao GraphRAG.
