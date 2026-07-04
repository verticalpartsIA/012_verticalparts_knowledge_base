---
title: "ListarNFe"
service: "NF-e Importar"
domain: "omie.produtos"
resource: "NF-e Importar"
method: "ListarNFe"
endpoint: "https://app.omie.com.br/api/v1/produtos/nfe/"
http_method: "POST"
version: "v1"
entity: "NF-e Importar"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/produtos/nfe/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - listarnfe
keywords:
  - "ListarNFe"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ListarNFe

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ListarNFe` do servico `NF-e Importar`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- NF-e Importar

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/produtos/nfe/`

Descricao extraida:

Lista as NFes importadas. Parâmetros: Retorno nfeListarResponse : Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ListarNFe` no contexto do servico `NF-e Importar`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "nPagina": 1,
  "nRegPorPagina": 50,
  "dDataEmissaoInicial": "04/07/2026",
  "dDataEmissaoFinal": "04/07/2026"
}
```

## FAQ

### Quando devo usar o metodo ListarNFe?

Necessita validacao.
### Quais campos sao obrigatorios para ListarNFe?

Necessita validacao.
### Qual endpoint devo chamar para ListarNFe?

Necessita validacao.
### Que retorno esperar do metodo ListarNFe?

Necessita validacao.
### Como ListarNFe se relaciona com NF-e Importar?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ListarNFe?
- Quais campos sao obrigatorios para ListarNFe?
- Qual endpoint devo chamar para ListarNFe?
- Que retorno esperar do metodo ListarNFe?
- Como ListarNFe se relaciona com NF-e Importar?

## Tags para RAG

- omie
- factory-mvp
- listarnfe
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/nfe/
