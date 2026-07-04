---
title: "ListarProdutosResumido"
service: "Produtos"
domain: "omie.geral"
resource: "Produtos"
method: "ListarProdutosResumido"
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
  - listarprodutosresumido
keywords:
  - "ListarProdutosResumido"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ListarProdutosResumido

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ListarProdutosResumido` do servico `Produtos`.

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

Lista os produtos cadastrados Parâmetros: Retorno produto_servico_list_response : Lista de produtos encontrados no omie. Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ListarProdutosResumido` no contexto do servico `Produtos`.

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

### Quando devo usar o metodo ListarProdutosResumido?

Necessita validacao.
### Quais campos sao obrigatorios para ListarProdutosResumido?

Necessita validacao.
### Qual endpoint devo chamar para ListarProdutosResumido?

Necessita validacao.
### Que retorno esperar do metodo ListarProdutosResumido?

Necessita validacao.
### Como ListarProdutosResumido se relaciona com Produtos?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ListarProdutosResumido?
- Quais campos sao obrigatorios para ListarProdutosResumido?
- Qual endpoint devo chamar para ListarProdutosResumido?
- Que retorno esperar do metodo ListarProdutosResumido?
- Como ListarProdutosResumido se relaciona com Produtos?

## Tags para RAG

- omie
- factory-mvp
- listarprodutosresumido
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/produtos/
