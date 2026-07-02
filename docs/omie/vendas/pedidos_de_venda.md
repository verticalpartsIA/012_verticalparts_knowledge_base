---
title: "Pedidos de Venda"
service: "Necessita validação contra documentação oficial Omie"
domain: "omie.vendas"
resource: "pedidos_de_venda"
method: "indice"
endpoint: "Necessita validação contra documentação oficial Omie"
http_method: "Necessita validação"
version: "1"
entity: "pedido_de_venda"
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
  - pedidos_de_venda
  - inicial
keywords:
  - Pedidos de Venda
questions:
  - "Como validar oficialmente Pedidos de Venda na Omie?"
use_cases:
  - triagem_documental
business_area: "ERP / Necessita validação"
llm_ready: false
rag_ready: false
graph_ready: false
embedding_version: 1
---
# Pedidos de Venda

## Título

Pedidos de venda

## Domínio

Omie Vendas

## Endpoint

`/produtos/pedido/`

## Métodos conhecidos

- `ListarPedidos`
- `ConsultarPedido`
- `IncluirPedido`
- `AlterarPedido`
- `ExcluirPedido`

## Quando usar

Use este endpoint para registrar, consultar e acompanhar pedidos de venda de produtos, incluindo vínculo com clientes, itens, condições comerciais e faturamento.

## Entidades relacionadas

- Cliente
- Produto
- Estoque
- Conta a receber
- Documento fiscal
- Transportadora

## Exemplos de perguntas que um usuário faria

- Como consultar um pedido de venda pelo número?
- Qual endpoint inclui pedido de venda de produto?
- Como relacionar itens e cliente em um pedido?
- Pedido de venda gera contas a receber automaticamente?

## Observações para RAG

Recupere este documento quando a pergunta mencionar venda, pedido, produto, cliente, item, faturamento ou integração comercial. Regras de geração financeira e fiscal devem ser validadas por fonte oficial ou teste controlado.

## Status

inicial/a validar

## Objetivo

Organizar conhecimento sobre Pedidos de Venda em formato reutilizavel por LLMs, RAG e GraphRAG.

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
