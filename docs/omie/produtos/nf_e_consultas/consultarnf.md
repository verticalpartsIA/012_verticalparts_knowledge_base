---
title: "ConsultarNF"
service: "NF-e Consultas"
domain: "omie.produtos"
resource: "NF-e Consultas"
method: "ConsultarNF"
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
  - consultarnf
keywords:
  - "ConsultarNF"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ConsultarNF

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ConsultarNF` do servico `NF-e Consultas`.

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

Consulta um Nota Fiscal Parâmetros: Retorno nfCadastro : Dados da Nota Fiscal Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ConsultarNF` no contexto do servico `NF-e Consultas`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "nCodNF": 0,
  "nNF": "1"
}
```

## FAQ

### Quando devo usar o metodo ConsultarNF?

Necessita validacao.
### Quais campos sao obrigatorios para ConsultarNF?

Necessita validacao.
### Qual endpoint devo chamar para ConsultarNF?

Necessita validacao.
### Que retorno esperar do metodo ConsultarNF?

Necessita validacao.
### Como ConsultarNF se relaciona com NF-e Consultas?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ConsultarNF?
- Quais campos sao obrigatorios para ConsultarNF?
- Qual endpoint devo chamar para ConsultarNF?
- Que retorno esperar do metodo ConsultarNF?
- Como ConsultarNF se relaciona com NF-e Consultas?

## Tags para RAG

- omie
- factory-mvp
- consultarnf
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/nfconsultar/
