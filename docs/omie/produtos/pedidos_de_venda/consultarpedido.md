---
title: "ConsultarPedido"
service: "Pedidos de Venda"
domain: "omie.produtos"
resource: "Pedidos de Venda"
method: "ConsultarPedido"
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
  - consultarpedido
keywords:
  - "ConsultarPedido"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ConsultarPedido

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ConsultarPedido` do servico `Pedidos de Venda`.

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

Consulta de Pedido de Venda de Produto Parâmetros: Retorno pvpConsultarResponse : Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ConsultarPedido` no contexto do servico `Pedidos de Venda`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "codigo_pedido": 25953530
}
```

## FAQ

### Quando devo usar o metodo ConsultarPedido?

Necessita validacao.
### Quais campos sao obrigatorios para ConsultarPedido?

Necessita validacao.
### Qual endpoint devo chamar para ConsultarPedido?

Necessita validacao.
### Que retorno esperar do metodo ConsultarPedido?

Necessita validacao.
### Como ConsultarPedido se relaciona com Pedidos de Venda?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ConsultarPedido?
- Quais campos sao obrigatorios para ConsultarPedido?
- Qual endpoint devo chamar para ConsultarPedido?
- Que retorno esperar do metodo ConsultarPedido?
- Como ConsultarPedido se relaciona com Pedidos de Venda?

## Tags para RAG

- omie
- factory-mvp
- consultarpedido
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/pedido/
