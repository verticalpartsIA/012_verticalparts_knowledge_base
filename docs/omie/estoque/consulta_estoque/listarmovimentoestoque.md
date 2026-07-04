---
title: "ListarMovimentoEstoque"
service: "Consulta Estoque"
domain: "omie.estoque"
resource: "Consulta Estoque"
method: "ListarMovimentoEstoque"
endpoint: "https://app.omie.com.br/api/v1/estoque/consulta/"
http_method: "POST"
version: "v1"
entity: "Consulta Estoque"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/estoque/consulta/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - listarmovimentoestoque
keywords:
  - "ListarMovimentoEstoque"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ListarMovimentoEstoque

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ListarMovimentoEstoque` do servico `Consulta Estoque`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- Consulta Estoque

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/estoque/consulta/`

Descricao extraida:

Parâmetros: Retorno ListarMovEstoqueResponse : Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ListarMovimentoEstoque` no contexto do servico `Consulta Estoque`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "nPagina": 1,
  "nRegPorPagina": 50,
  "codigo_local_estoque": 0,
  "idProd": 0,
  "dDtInicial": "04/07/2026",
  "dDtFinal": "04/07/2026",
  "lista_local_estoque": ""
}
```

## FAQ

### Quando devo usar o metodo ListarMovimentoEstoque?

Necessita validacao.
### Quais campos sao obrigatorios para ListarMovimentoEstoque?

Necessita validacao.
### Qual endpoint devo chamar para ListarMovimentoEstoque?

Necessita validacao.
### Que retorno esperar do metodo ListarMovimentoEstoque?

Necessita validacao.
### Como ListarMovimentoEstoque se relaciona com Consulta Estoque?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ListarMovimentoEstoque?
- Quais campos sao obrigatorios para ListarMovimentoEstoque?
- Qual endpoint devo chamar para ListarMovimentoEstoque?
- Que retorno esperar do metodo ListarMovimentoEstoque?
- Como ListarMovimentoEstoque se relaciona com Consulta Estoque?

## Tags para RAG

- omie
- factory-mvp
- listarmovimentoestoque
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/estoque/consulta/
