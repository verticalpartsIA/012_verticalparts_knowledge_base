---
title: "ListarProdutos"
service: "Produtos"
domain: "omie.geral"
resource: "Produtos"
method: "ListarProdutos"
endpoint: "https://app.omie.com.br/api/v1/geral/produtos/"
http_method: "POST"
version: "v1"
entity: "Produtos"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/geral/produtos/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - listarprodutos
keywords:
  - "ListarProdutos"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ListarProdutos

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ListarProdutos` do servico `Produtos`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- Produtos

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/geral/produtos/`

Descricao extraida:

Lista completa do cadastro de produtos Parâmetros: Retorno produto_servico_listfull_response : Lista completa de produtos encontrados no omie. Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ListarProdutos` no contexto do servico `Produtos`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "pagina": 1,
  "registros_por_pagina": 50,
  "apenas_importado_api": "N",
  "filtrar_apenas_omiepdv": "N"
}
```

## FAQ

### Quando devo usar o metodo ListarProdutos?

Necessita validacao.
### Quais campos sao obrigatorios para ListarProdutos?

Necessita validacao.
### Qual endpoint devo chamar para ListarProdutos?

Necessita validacao.
### Que retorno esperar do metodo ListarProdutos?

Necessita validacao.
### Como ListarProdutos se relaciona com Produtos?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ListarProdutos?
- Quais campos sao obrigatorios para ListarProdutos?
- Qual endpoint devo chamar para ListarProdutos?
- Que retorno esperar do metodo ListarProdutos?
- Como ListarProdutos se relaciona com Produtos?

## Tags para RAG

- omie
- factory-mvp
- listarprodutos
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/produtos/
