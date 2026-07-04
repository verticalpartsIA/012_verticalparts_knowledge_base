---
title: "ListarContasPagar"
service: "Contas a Pagar Lançamentos"
domain: "omie.financas"
resource: "Contas a Pagar Lançamentos"
method: "ListarContasPagar"
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
  - listarcontaspagar
keywords:
  - "ListarContasPagar"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ListarContasPagar

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ListarContasPagar` do servico `Contas a Pagar Lançamentos`.

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

Listar as Contas a Pagar Parâmetros: Retorno lcpListarResponse : Resposta da listagem de Contas a Pagar Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ListarContasPagar` no contexto do servico `Contas a Pagar Lançamentos`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "pagina": 1,
  "registros_por_pagina": 20,
  "apenas_importado_api": "N"
}
```

## FAQ

### Quando devo usar o metodo ListarContasPagar?

Necessita validacao.
### Quais campos sao obrigatorios para ListarContasPagar?

Necessita validacao.
### Qual endpoint devo chamar para ListarContasPagar?

Necessita validacao.
### Que retorno esperar do metodo ListarContasPagar?

Necessita validacao.
### Como ListarContasPagar se relaciona com Contas a Pagar Lançamentos?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ListarContasPagar?
- Quais campos sao obrigatorios para ListarContasPagar?
- Qual endpoint devo chamar para ListarContasPagar?
- Que retorno esperar do metodo ListarContasPagar?
- Como ListarContasPagar se relaciona com Contas a Pagar Lançamentos?

## Tags para RAG

- omie
- factory-mvp
- listarcontaspagar
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/financas/contapagar/
