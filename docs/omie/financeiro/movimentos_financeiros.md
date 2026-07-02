---
title: "Movimentos Financeiros"
service: "Necessita validação contra documentação oficial Omie"
domain: "omie.financeiro"
resource: "movimentos_financeiros"
method: "indice"
endpoint: "Necessita validação contra documentação oficial Omie"
http_method: "Necessita validação"
version: "1"
entity: "movimento_financeiro"
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
  - movimentos_financeiros
  - inicial
keywords:
  - Movimentos Financeiros
questions:
  - "Como validar oficialmente Movimentos Financeiros na Omie?"
use_cases:
  - triagem_documental
business_area: "ERP / Necessita validação"
llm_ready: false
rag_ready: false
graph_ready: false
embedding_version: 1
---
# Movimentos Financeiros

## Título

Movimentos financeiros

## Domínio

Omie Financeiro

## Endpoint

`/financas/mf/`

## Métodos conhecidos

- `ListarMovimentos`
- `ConsultarMovimento`

## Quando usar

Use este endpoint para consultar movimentações financeiras efetivadas ou registradas no Omie, especialmente em cenários de conciliação, auditoria e rastreio de baixas.

## Entidades relacionadas

- Conta a pagar
- Conta a receber
- Conta corrente
- Categoria financeira
- Lançamento financeiro
- Baixa

## Exemplos de perguntas que um usuário faria

- Como consultar movimentos financeiros por período?
- Como identificar a baixa de uma conta a receber?
- Qual endpoint uso para auditar movimentações financeiras?
- Como relacionar movimento financeiro com título de origem?

## Observações para RAG

Este documento deve aparecer para perguntas sobre extrato, baixa, conciliação, movimento, conta corrente e auditoria financeira. Métodos disponíveis e filtros devem ser confirmados antes de implementação.

## Status

inicial/a validar

## Objetivo

Organizar conhecimento sobre Movimentos Financeiros em formato reutilizavel por LLMs, RAG e GraphRAG.

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
