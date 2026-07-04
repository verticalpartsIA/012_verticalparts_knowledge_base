---
title: "ConsultarPedCompra"
service: "Pedidos de Compra"
domain: "omie.produtos"
resource: "Pedidos de Compra"
method: "ConsultarPedCompra"
endpoint: "https://app.omie.com.br/api/v1/produtos/pedidocompra/"
http_method: "POST"
version: "v1"
entity: "Pedidos de Compra"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/produtos/pedidocompra/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - consultarpedcompra
keywords:
  - "ConsultarPedCompra"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ConsultarPedCompra

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ConsultarPedCompra` do servico `Pedidos de Compra`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- Pedidos de Compra

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/produtos/pedidocompra/`

Descricao extraida:

Parâmetros: Retorno pedidos_pesquisa : Lista com os pedidos de compra Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ConsultarPedCompra` no contexto do servico `Pedidos de Compra`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "nCodPed": 0,
  "cCodIntPed": "INT001",
  "cNumero": ""
}
```

## FAQ

### Quando devo usar o metodo ConsultarPedCompra?

Necessita validacao.
### Quais campos sao obrigatorios para ConsultarPedCompra?

Necessita validacao.
### Qual endpoint devo chamar para ConsultarPedCompra?

Necessita validacao.
### Que retorno esperar do metodo ConsultarPedCompra?

Necessita validacao.
### Como ConsultarPedCompra se relaciona com Pedidos de Compra?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ConsultarPedCompra?
- Quais campos sao obrigatorios para ConsultarPedCompra?
- Qual endpoint devo chamar para ConsultarPedCompra?
- Que retorno esperar do metodo ConsultarPedCompra?
- Como ConsultarPedCompra se relaciona com Pedidos de Compra?

## Tags para RAG

- omie
- factory-mvp
- consultarpedcompra
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/pedidocompra/
