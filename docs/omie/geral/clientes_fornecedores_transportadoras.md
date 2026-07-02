---
title: "Indice Clientes, Fornecedores e Transportadoras"
service: "ClientesCadastro"
domain: "omie.geral"
resource: "clientes"
method: "indice"
endpoint: "https://app.omie.com.br/api/v1/geral/clientes/"
http_method: "POST"
version: "1"
entity: "cliente_fornecedor_transportadora"
related_entities:
  - Cliente
  - Fornecedor
  - Transportadora
related_methods:
  - ConsultarCliente
  - IncluirCliente
  - AlterarCliente
  - ListarClientes
permissions:
  - "Necessita credenciais Omie validas fora do repositorio"
complexity: "media"
status: "Necessita validacao"
source: "https://app.omie.com.br/api/v1/geral/clientes/"
last_review: "2026-07-02"
tags:
  - omie
  - geral
  - clientes
  - enterprise-rag
keywords:
  - ClientesCadastro
  - VerticalParts Knowledge Base
questions:
  - "Como usar o cadastro de clientes da Omie?"
use_cases:
  - assistente_llm
  - rag_operacional
business_area: "ERP / Cadastros / Geral"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# Índice: Clientes, Fornecedores e Transportadoras

## Visão Geral

Este documento é o índice resumido do serviço Omie `ClientesCadastro`, localizado no domínio `Geral > Clientes, Fornecedores e Transportadoras`.

A documentação detalhada por método está em:

- `docs/omie/geral/clientes/`

## Domínio

Omie Geral

## Endpoint

`/geral/clientes/`

## Métodos conhecidos

- `AlterarCliente`
- `AssociarCodIntCliente`
- `ConsultarCliente`
- `ExcluirCliente`
- `IncluirCliente`
- `IncluirClientesPorLote` - depreciado na fonte oficial
- `ListarClientes`
- `ListarClientesResumido`
- `UpsertCliente`
- `UpsertClienteCpfCnpj`
- `UpsertClientesPorLote` - depreciado na fonte oficial

## Quando usar

Use este grupo de endpoints para consultar, cadastrar e manter entidades cadastrais usadas em operações comerciais, financeiras, logísticas e fiscais. A mesma base cadastral pode representar clientes, fornecedores, transportadoras ou outros participantes relacionados ao fluxo da empresa.

## Documentos Detalhados

- `docs/omie/geral/clientes/alterar_cliente.md`
- `docs/omie/geral/clientes/associar_cod_int_cliente.md`
- `docs/omie/geral/clientes/consultar_cliente.md`
- `docs/omie/geral/clientes/excluir_cliente.md`
- `docs/omie/geral/clientes/incluir_cliente.md`
- `docs/omie/geral/clientes/incluir_clientes_por_lote.md`
- `docs/omie/geral/clientes/listar_clientes.md`
- `docs/omie/geral/clientes/listar_clientes_resumido.md`
- `docs/omie/geral/clientes/upsert_cliente.md`
- `docs/omie/geral/clientes/upsert_cliente_cpf_cnpj.md`
- `docs/omie/geral/clientes/upsert_clientes_por_lote.md`

## Entidades relacionadas

- Cliente
- Fornecedor
- Transportadora
- Pedido de venda
- Conta a pagar
- Conta a receber
- Documento fiscal

## Exemplos de perguntas que um usuário faria

- Como consultar um cliente pelo código no Omie?
- Qual endpoint uso para cadastrar um fornecedor?
- Transportadora usa o mesmo cadastro de clientes e fornecedores?
- Quais dados cadastrais preciso validar antes de emitir um pedido?

## Observações para RAG

Este índice deve ser recuperado quando a pergunta pedir uma visão geral do cadastro de clientes, fornecedores e transportadoras. Para perguntas sobre método específico, payload, retorno ou erro, a LLM deve preferir os documentos detalhados em `docs/omie/geral/clientes/`.

## Status

inicial/expandido com fonte oficial

## Objetivo

Organizar conhecimento sobre Indice Clientes, Fornecedores e Transportadoras em formato reutilizavel por LLMs, RAG e GraphRAG.

## Quando utilizar

Use este documento quando a pergunta exigir contexto geral, indice de navegacao ou ponto de entrada para documentos detalhados.

## Quando NÃO utilizar

Nao use este documento como contrato final de payload quando existir um documento de metodo mais especifico.

## Fluxo de negócio

O usuario formula uma pergunta, a LLM identifica o dominio, consulta este indice e entao navega para o documento detalhado mais adequado.

## Entidades relacionadas

- Cliente
- Fornecedor
- Transportadora

## Métodos relacionados

- `ConsultarCliente`
- `IncluirCliente`
- `AlterarCliente`
- `ListarClientes`

## Exemplos completos

### curl

Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

### Python

Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

### JavaScript

Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

## FAQ

### 1. Este documento substitui os metodos detalhados?

Nao. Ele direciona a LLM para o documento especifico.

### 2. O conteudo e oficial?

Partes derivadas da fonte oficial sao marcadas no documento. Lacunas devem ser tratadas como "Necessita validacao".

## Perguntas naturais

- Onde encontro os metodos de ClientesCadastro?
- Qual documento devo consultar para payload?
- O que ainda necessita validacao?

## Tags para RAG

- omie
- indice
- enterprise-rag
- graphrag

## Casos de uso

- Navegacao por dominio.
- Recuperacao RAG.
- Expansao GraphRAG.
