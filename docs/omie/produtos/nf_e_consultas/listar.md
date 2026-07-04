---
title: "Listar"
service: "NF-e Consultas"
domain: "omie.produtos"
resource: "NF-e Consultas"
method: "Listar"
endpoint: "https://app.omie.com.br/api/v1/produtos/nfconsultar/"
http_method: "POST"
version: "v1"
entity: "NF-e Consultas"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/produtos/nfconsultar/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - listar
keywords:
  - "Listar"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# Listar

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `Listar` do servico `NF-e Consultas`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- NF-e Consultas

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/produtos/nfconsultar/`

Descricao extraida:

Listar as Notas Fiscais cadastradas. Parâmetros: Retorno nfListarResponse : Resposta da listagem de Notas Fiscais Exemplo: Teste agora mesmo

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

- Automatizar a operacao `Listar` no contexto do servico `NF-e Consultas`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "pagina": 1,
  "registros_por_pagina": 20,
  "ordenar_por": "CODIGO"
}
```

## FAQ

### Quando devo usar o metodo Listar?

Necessita validacao.
### Quais campos sao obrigatorios para Listar?

Necessita validacao.
### Qual endpoint devo chamar para Listar?

Necessita validacao.
### Que retorno esperar do metodo Listar?

Necessita validacao.
### Como Listar se relaciona com NF-e Consultas?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo Listar?
- Quais campos sao obrigatorios para Listar?
- Qual endpoint devo chamar para Listar?
- Que retorno esperar do metodo Listar?
- Como Listar se relaciona com NF-e Consultas?

## Tags para RAG

- omie
- factory-mvp
- listar
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/nfconsultar/
