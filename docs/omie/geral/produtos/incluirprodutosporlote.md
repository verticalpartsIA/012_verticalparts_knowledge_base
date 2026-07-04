---
title: "IncluirProdutosPorLote"
service: "Produtos"
domain: "omie.geral"
resource: "Produtos"
method: "IncluirProdutosPorLote"
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
  - incluirprodutosporlote
keywords:
  - "IncluirProdutosPorLote"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# IncluirProdutosPorLote

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `IncluirProdutosPorLote` do servico `Produtos`.

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

DEPRECATED Parâmetros: Retorno produto_servico_lote_response : Resposta do processamento do lote de produto importados. Exemplo: Teste agora mesmo

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

- Automatizar a operacao `IncluirProdutosPorLote` no contexto do servico `Produtos`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "lote": 123,
  "produto_servico_cadastro": [
    {
      "codigo_produto_integracao": "1628097039",
      "codigo": "teste1235",
      "descricao": "Produto de teste",
      "unidade": "UN",
      "ncm": "9504.50.00"
    },
    {
      "codigo_produto_integracao": "1628097040",
      "codigo": "teste1234",
      "descricao": "Produto de teste",
      "unidade": "UN",
      "ncm": "9504.50.00"
    }
  ]
}
```

## FAQ

### Quando devo usar o metodo IncluirProdutosPorLote?

Necessita validacao.
### Quais campos sao obrigatorios para IncluirProdutosPorLote?

Necessita validacao.
### Qual endpoint devo chamar para IncluirProdutosPorLote?

Necessita validacao.
### Que retorno esperar do metodo IncluirProdutosPorLote?

Necessita validacao.
### Como IncluirProdutosPorLote se relaciona com Produtos?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo IncluirProdutosPorLote?
- Quais campos sao obrigatorios para IncluirProdutosPorLote?
- Qual endpoint devo chamar para IncluirProdutosPorLote?
- Que retorno esperar do metodo IncluirProdutosPorLote?
- Como IncluirProdutosPorLote se relaciona com Produtos?

## Tags para RAG

- omie
- factory-mvp
- incluirprodutosporlote
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/produtos/
