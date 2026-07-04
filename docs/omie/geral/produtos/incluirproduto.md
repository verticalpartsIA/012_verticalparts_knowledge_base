---
title: "IncluirProduto"
service: "Produtos"
domain: "omie.geral"
resource: "Produtos"
method: "IncluirProduto"
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
  - incluirproduto
keywords:
  - "IncluirProduto"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# IncluirProduto

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `IncluirProduto` do servico `Produtos`.

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

Incluir um produto. Parâmetros: Retorno produto_servico_status : Status de retorno do cadastro de produtos Exemplo: Teste agora mesmo

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

- Automatizar a operacao `IncluirProduto` no contexto do servico `Produtos`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "codigo_produto_integracao": "1783197667",
  "codigo": "teste0001",
  "descricao": "Produto de teste",
  "unidade": "UN"
}
```

## FAQ

### Quando devo usar o metodo IncluirProduto?

Necessita validacao.
### Quais campos sao obrigatorios para IncluirProduto?

Necessita validacao.
### Qual endpoint devo chamar para IncluirProduto?

Necessita validacao.
### Que retorno esperar do metodo IncluirProduto?

Necessita validacao.
### Como IncluirProduto se relaciona com Produtos?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo IncluirProduto?
- Quais campos sao obrigatorios para IncluirProduto?
- Qual endpoint devo chamar para IncluirProduto?
- Que retorno esperar do metodo IncluirProduto?
- Como IncluirProduto se relaciona com Produtos?

## Tags para RAG

- omie
- factory-mvp
- incluirproduto
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/produtos/
