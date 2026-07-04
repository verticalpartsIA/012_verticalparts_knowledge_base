---
title: "LancarPagamento"
service: "Contas a Pagar Lançamentos"
domain: "omie.financas"
resource: "Contas a Pagar Lançamentos"
method: "LancarPagamento"
endpoint: "https://app.omie.com.br/api/v1/financas/contapagar/"
http_method: "POST"
version: "v1"
entity: "Contas a Pagar Lançamentos"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/financas/contapagar/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - lancarpagamento
keywords:
  - "LancarPagamento"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# LancarPagamento

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `LancarPagamento` do servico `Contas a Pagar Lançamentos`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- Contas a Pagar Lançamentos

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/financas/contapagar/`

Descricao extraida:

Efetua a baixa de um pagamento do contas a pagar. Parâmetros: Retorno conta_pagar_lancar_pagamento_resposta : Exemplo: Teste agora mesmo

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

- Automatizar a operacao `LancarPagamento` no contexto do servico `Contas a Pagar Lançamentos`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "codigo_lancamento": 0,
  "codigo_lancamento_integracao": "",
  "codigo_baixa_integracao": "",
  "codigo_conta_corrente": "",
  "valor": 100.2,
  "desconto": 0,
  "juros": 0,
  "multa": 0,
  "data": "04/07/2026",
  "observacao": "Baixa de documento realizada via API."
}
```

## FAQ

### Quando devo usar o metodo LancarPagamento?

Necessita validacao.
### Quais campos sao obrigatorios para LancarPagamento?

Necessita validacao.
### Qual endpoint devo chamar para LancarPagamento?

Necessita validacao.
### Que retorno esperar do metodo LancarPagamento?

Necessita validacao.
### Como LancarPagamento se relaciona com Contas a Pagar Lançamentos?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo LancarPagamento?
- Quais campos sao obrigatorios para LancarPagamento?
- Qual endpoint devo chamar para LancarPagamento?
- Que retorno esperar do metodo LancarPagamento?
- Como LancarPagamento se relaciona com Contas a Pagar Lançamentos?

## Tags para RAG

- omie
- factory-mvp
- lancarpagamento
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/financas/contapagar/
