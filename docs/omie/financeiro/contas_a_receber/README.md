---
title: "ListarContasReceber - Omie Financeiro Contas a Receber"
service: "LancamentoContaReceber"
domain: "omie.financeiro"
resource: "contas_a_receber"
method: "ListarContasReceber"
endpoint: "https://app.omie.com.br/api/v1/financas/contareceber/"
http_method: "POST"
version: "1"
entity: "conta_a_receber"
related_entities:
  - Cliente
  - Pedido de Venda
  - Ordem de Serviço
  - NF-e
  - NFS-e
  - Categorias
  - Bancos
  - Movimentos Financeiros
related_methods:
  - ConsultarContaReceber
  - IncluirContaReceber
  - AlterarContaReceber
  - ListarContasReceber
permissions:
  - "Necessita credenciais Omie validas fora do repositorio"
  - "Nao documentar chaves, segredos ou senhas"
complexity: "media"
status: "Documentado oficialmente / Necessita validação em integração"
source: "https://app.omie.com.br/api/v1/financas/contareceber/"
last_review: "2026-07-02"
tags:
  - omie
  - financeiro
  - contas-a-receber
  - listagem
  - enterprise-rag
keywords:
  - LancamentoContaReceber
  - ListarContasReceber
  - Contas a Receber
  - RAG
questions:
  - "Como usar ListarContasReceber?"
  - "Como documentar Contas a Receber para LLM?"
  - "Quais campos necessitam validação?"
use_cases:
  - conciliacao_financeira
  - baixa_recebimento
  - sincronizacao_financeira
  - assistente_llm
business_area: "ERP / Financeiro / Contas a Receber"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# Omie Financeiro: Contas a Receber

## Objetivo

Documentar o serviço `LancamentoContaReceber` como base Enterprise LLM/RAG para títulos a receber.

## Quando utilizar

Use este índice para escolher o método correto de consulta, inclusão, alteração, exclusão, baixa, conciliação, lote ou rateio por departamento.

## Quando NÃO utilizar

Não utilize como contrato final de payload; use o arquivo do método específico.

## Fluxo de negócio

Contas a receber conectam clientes, pedidos de venda, ordens de serviço, NF-e, NFS-e, categorias, bancos e movimentos financeiros.

## Casos de uso

- Escolha de método por uma LLM financeira.
- Recuperação RAG de contratos de payload.
- Expansão GraphRAG para clientes, pedidos, documentos fiscais, bancos e movimentos.
- Triagem de dúvidas sobre baixa, conciliação e listagem.

## Entidades relacionadas

- Cliente
- Pedidos de Venda
- Ordem de Serviço
- NF-e
- NFS-e
- Categorias
- Bancos
- Movimentos Financeiros

## Métodos relacionados

- `AlterarContaReceber`: Altera uma conta a receber ja cadastrada.
- `AlterarDistribuicaoDepartamento`: Altera a distribuicao por departamento de uma conta a receber.
- `CancelarContaReceber`: Cancela o boleto gerado de uma conta a receber.
- `CancelarRecebimento`: Cancela uma baixa de recebimento de contas a receber.
- `ConciliarRecebimento`: Realiza a conciliacao do recebimento.
- `ConsultarContaReceber`: Consulta uma conta a receber por chave.
- `DesconciliarRecebimento`: Desconcilia um recebimento previamente conciliado.
- `ExcluirContaReceber`: Exclui uma conta a receber.
- `ExcluirDistribuicaoDepartamento`: Exclui a distribuicao por departamento de uma conta a receber.
- `IncluirContaReceber`: Inclui uma nova conta a receber.
- `IncluirContaReceberPorLote`: Inclui contas a receber por lote.
- `IncluirDistribuicaoDepartamento`: Inclui distribuicao por departamento em uma conta a receber.
- `LancarRecebimento`: Lanca a baixa/recebimento de uma conta a receber.
- `ListarContasReceber`: Lista contas a receber cadastradas.
- `UpsertContaReceber`: Inclui ou altera uma conta a receber conforme chave informada.
- `UpsertContaReceberPorLote`: Inclui ou altera contas a receber por lote.

## Exemplos completos

Consulte os arquivos de método para payloads completos. Este índice mantém apenas referências fictícias.

### curl

Exemplo omitido no índice; consulte o método específico.

### Python

Exemplo omitido no índice; consulte o método específico.

### JavaScript

Exemplo omitido no índice; consulte o método específico.

## FAQ

### 1. O que é Contas a Receber no Omie?

É o domínio financeiro de títulos a receber, baixas, conciliações e vínculos com clientes e documentos.

### 2. A documentação está pronta para LLM?

Sim, os métodos desta pasta estão marcados como `llm_ready: true` e `rag_ready: true`.

## Perguntas naturais

- Como listar contas a receber?
- Como baixar um recebimento?
- Como conciliar uma baixa?

## Tags para RAG

- omie
- financeiro
- contas-a-receber
- enterprise-rag

## GraphRAG

Consulte `graphs/omie/contas_a_receber.graph.md` para relações entre contas a receber, clientes, pedidos, ordens de serviço, NF-e, NFS-e, bancos, categorias e movimentos financeiros.

## Fonte oficial consultada

- https://app.omie.com.br/api/v1/financas/contareceber/
