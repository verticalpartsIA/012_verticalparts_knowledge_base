---
title: "Omie API - Indice"
service: "ClientesCadastro"
domain: "omie.geral"
resource: "omie"
method: "indice"
endpoint: "https://app.omie.com.br/api/v1/geral/clientes/"
http_method: "POST"
version: "1"
entity: "cliente_fornecedor_transportadora"
related_entities:
  - Cliente
  - Fornecedor
  - Transportadora
related_methods:
  - ConsultarCliente
  - IncluirCliente
  - AlterarCliente
  - ListarClientes
permissions:
  - "Necessita credenciais Omie validas fora do repositorio"
complexity: "media"
status: "Necessita validacao"
source: "https://app.omie.com.br/api/v1/geral/clientes/"
last_review: "2026-07-02"
tags:
  - omie
  - geral
  - clientes
  - enterprise-rag
keywords:
  - ClientesCadastro
  - VerticalParts Knowledge Base
questions:
  - "Como usar o cadastro de clientes da Omie?"
use_cases:
  - assistente_llm
  - rag_operacional
business_area: "ERP / Cadastros / Geral"
llm_ready: true
rag_ready: true
graph_ready: true
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
