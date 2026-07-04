---
title: "ListarPedidos"
service: "Pedidos de Venda"
domain: "omie.produtos"
resource: "Pedidos de Venda"
method: "ListarPedidos"
endpoint: "https://app.omie.com.br/api/v1/produtos/pedido/"
http_method: "POST"
version: "v1"
entity: "Pedidos de Venda"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/produtos/pedido/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - listarpedidos
keywords:
  - "ListarPedidos"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ListarPedidos

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ListarPedidos` do servico `Pedidos de Venda`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- Pedidos de Venda

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/produtos/pedido/`

Descricao extraida:

Listar os pedidos de venda de produto Parâmetros: Retorno pvpListarResponse : Exemplo: Teste agora mesmo

## Campos obrigatorios

Necessita validacao.

## Campos opcionais

Necessita validacao.

## Regras de negocio

Necessita validacao contra a documentacao oficial e regras operacionais da VerticalParts.

## Validacoes

- Conferir campos obrigatorios antes da chamada.
- Conferir tipos informados pela documentacao oficial.

## Restricoes

- Exemplos sao ficticios.
- Credenciais foram omitidas por seguranca.

## Resposta esperada

Necessita validacao.

## Erros comuns

Necessita validacao.

## Como resolver os erros

- Validar payload contra a documentacao oficial.
- Conferir credenciais no ambiente seguro de execucao, sem registrar valores neste repositorio.

## Casos de uso

- Automatizar a operacao `ListarPedidos` no contexto do servico `Pedidos de Venda`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "pagina": 1,
  "registros_por_pagina": 100,
  "apenas_importado_api": "N"
}
```

## FAQ

### Quando devo usar o metodo ListarPedidos?

Necessita validacao.
### Quais campos sao obrigatorios para ListarPedidos?

Necessita validacao.
### Qual endpoint devo chamar para ListarPedidos?

Necessita validacao.
### Que retorno esperar do metodo ListarPedidos?

Necessita validacao.
### Como ListarPedidos se relaciona com Pedidos de Venda?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ListarPedidos?
- Quais campos sao obrigatorios para ListarPedidos?
- Qual endpoint devo chamar para ListarPedidos?
- Que retorno esperar do metodo ListarPedidos?
- Como ListarPedidos se relaciona com Pedidos de Venda?

## Tags para RAG

- omie
- factory-mvp
- listarpedidos
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/pedido/
