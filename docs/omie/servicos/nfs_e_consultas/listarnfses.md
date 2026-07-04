---
title: "ListarNFSEs"
service: "NFS-e Consultas"
domain: "omie.servicos"
resource: "NFS-e Consultas"
method: "ListarNFSEs"
endpoint: "https://app.omie.com.br/api/v1/servicos/nfse/"
http_method: "POST"
version: "v1"
entity: "NFS-e Consultas"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/servicos/nfse/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - listarnfses
keywords:
  - "ListarNFSEs"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# ListarNFSEs

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `ListarNFSEs` do servico `NFS-e Consultas`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- NFS-e Consultas

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/servicos/nfse/`

Descricao extraida:

Lista de NFS-es. Parâmetros: Retorno nfseListarResponse : Exemplo: Teste agora mesmo

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

- Automatizar a operacao `ListarNFSEs` no contexto do servico `NFS-e Consultas`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "nPagina": 1,
  "nRegPorPagina": 20
}
```

## FAQ

### Quando devo usar o metodo ListarNFSEs?

Necessita validacao.
### Quais campos sao obrigatorios para ListarNFSEs?

Necessita validacao.
### Qual endpoint devo chamar para ListarNFSEs?

Necessita validacao.
### Que retorno esperar do metodo ListarNFSEs?

Necessita validacao.
### Como ListarNFSEs se relaciona com NFS-e Consultas?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo ListarNFSEs?
- Quais campos sao obrigatorios para ListarNFSEs?
- Qual endpoint devo chamar para ListarNFSEs?
- Que retorno esperar do metodo ListarNFSEs?
- Como ListarNFSEs se relaciona com NFS-e Consultas?

## Tags para RAG

- omie
- factory-mvp
- listarnfses
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/servicos/nfse/
