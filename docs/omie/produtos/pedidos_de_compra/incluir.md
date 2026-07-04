---
title: "Incluir"
service: "Pedidos de Compra"
domain: "omie.produtos"
resource: "Pedidos de Compra"
method: "Incluir"
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
  - incluir
keywords:
  - "Incluir"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# Incluir

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `Incluir` do servico `Pedidos de Compra`.

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

Incluir um Pedido de Compra Parâmetros: Retorno com_pedido_incluir_response : Exemplo: Teste agora mesmo

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

- Automatizar a operacao `Incluir` no contexto do servico `Pedidos de Compra`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "cabecalho_incluir": {
    "cCodIntPed": "INT001",
    "dDtPrevisao": "14/09/2026",
    "cCodParc": "",
    "nQtdeParc": 1,
    "nCodFor": "14170458",
    "cCodIntFor": "",
    "cCodCateg": "",
    "nCodCompr": 0,
    "cContato": "",
    "cContrato": "",
    "nCodCC": "1208238",
    "nCodIntCC": 0,
    "nCodProj": 0,
    "cNumPedido": "30048",
    "cObs": "Pedido incluido via API",
    "cObsInt": "Pedido Cadastrado via API"
  },
  "frete_incluir": {
    "nCodTransp": 0,
    "cCodIntTransp": "",
    "cTpFrete": "9",
    "cPlaca": "XXX-9999",
    "cUF": "SP",
    "nQtdVol": 5,
    "cEspVol": "",
    "cMarVol": "",
    "cNumVol": "",
    "nPesoLiq": 0.0,
    "nPesoBruto": 0.0,
    "nValFrete": 0,
    "nValSeguro": 0.0,
    "cLacre": "",
    "nValOutras": 0.0
  },
  "departamentos_incluir": [
    {
      "cCodDepto": "200000002498904",
      "nPerc": 50
    },
    {
      "cCodDepto": "200000002498905",
      "nPerc": 50
    }
  ],
  "produtos_incluir": [
    {
      "cCodIntItem": "ITEM001",
      "cCodIntProd": "",
      "nCodProd": "2037060",
      "cProduto": "",
      "cDescricao": "",
      "cNCM": "",
      "cUnidade": "",
      "cEAN": "",
      "nPesoLiq": 0,
      "nPesoBruto": 0,
      "nQtde": 10,
      "nValUnit": 200,
      "nDesconto": 0.0,
      "nValorIcms": 360.0,
      "nValorSt": 0.0,
      "nValorIpi": 20.0,
      "nValorPis": 33.0,
      "nValorCofins": 152.0,
      "cObs": "",
      "cMkpAtuPv": "N",
      "cMkpAtuSm": "N",
      "nMkpPerc": 0,
      "codigo_local_estoque": "",
      "cCodCateg": ""
    }
  ]
}
```

## FAQ

### Quando devo usar o metodo Incluir?

Necessita validacao.
### Quais campos sao obrigatorios para Incluir?

Necessita validacao.
### Qual endpoint devo chamar para Incluir?

Necessita validacao.
### Que retorno esperar do metodo Incluir?

Necessita validacao.
### Como Incluir se relaciona com Pedidos de Compra?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo Incluir?
- Quais campos sao obrigatorios para Incluir?
- Qual endpoint devo chamar para Incluir?
- Que retorno esperar do metodo Incluir?
- Como Incluir se relaciona com Pedidos de Compra?

## Tags para RAG

- omie
- factory-mvp
- incluir
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/pedidocompra/
