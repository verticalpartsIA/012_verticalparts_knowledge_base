---
title: "CancelarPedidoVenda"
service: "Pedidos de Venda Faturamento"
domain: "omie.produtos"
resource: "Pedidos de Venda Faturamento"
method: "CancelarPedidoVenda"
endpoint: "https://app.omie.com.br/api/v1/produtos/pedidovendafat/"
http_method: "POST"
version: "v1"
entity: "Pedidos de Venda Faturamento"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/produtos/pedidovendafat/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - cancelarpedidovenda
keywords:
  - "CancelarPedidoVenda"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# CancelarPedidoVenda

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `CancelarPedidoVenda` do servico `Pedidos de Venda Faturamento`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- Pedidos de Venda Faturamento

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/produtos/pedidovendafat/`

Descricao extraida:

Cancela um pedido de venda de produto. Parâmetros: Retorno pvpCancelarResponse : Exemplo: Teste agora mesmo

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

- Automatizar a operacao `CancelarPedidoVenda` no contexto do servico `Pedidos de Venda Faturamento`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "cCodIntPed": "",
  "nCodPed": 0
}
```

## FAQ

### Quando devo usar o metodo CancelarPedidoVenda?

Necessita validacao.
### Quais campos sao obrigatorios para CancelarPedidoVenda?

Necessita validacao.
### Qual endpoint devo chamar para CancelarPedidoVenda?

Necessita validacao.
### Que retorno esperar do metodo CancelarPedidoVenda?

Necessita validacao.
### Como CancelarPedidoVenda se relaciona com Pedidos de Venda Faturamento?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo CancelarPedidoVenda?
- Quais campos sao obrigatorios para CancelarPedidoVenda?
- Qual endpoint devo chamar para CancelarPedidoVenda?
- Que retorno esperar do metodo CancelarPedidoVenda?
- Como CancelarPedidoVenda se relaciona com Pedidos de Venda Faturamento?

## Tags para RAG

- omie
- factory-mvp
- cancelarpedidovenda
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/pedidovendafat/
