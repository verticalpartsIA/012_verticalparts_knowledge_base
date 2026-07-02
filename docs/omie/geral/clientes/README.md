---
title: "Omie Geral Clientes - Guia do Servico"
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
# Omie Geral: Clientes, Fornecedores e Transportadoras

## Objetivo

Explicar o servico `ClientesCadastro` para LLMs e sistemas RAG, conectando metodos oficiais, entidades, fluxos de negocio e criterios de escolha.

## Quando utilizar

Use este guia quando a pergunta envolver escolha entre consultar, incluir, alterar, excluir, listar, associar codigo interno ou executar upsert de clientes, fornecedores e transportadoras.

## Quando NÃO utilizar

Nao use este guia como contrato final de payload. Para payload, exemplos e FAQ completa, consulte o arquivo do metodo especifico.

## Fluxo de negócio

1. Identificar se a entidade atua como cliente, fornecedor ou transportadora.
2. Identificar se a intencao e consulta, cadastro, alteracao, exclusao, listagem, associacao ou upsert.
3. Selecionar o metodo oficial.
4. Validar campos obrigatorios e condicionais.
5. Responder com fonte oficial e status de validacao.

## Casos de uso

- Selecionar metodo correto para assistente LLM.
- Explicar o relacionamento entre cadastro, financeiro, vendas, compras, fiscal, CRM e servicos.
- Direcionar perguntas para documentos de metodo.
- Apoiar GraphRAG com entidades conectadas.

## O que representa este serviço

O serviço `ClientesCadastro` representa o cadastro central de participantes comerciais no Omie. Ele é usado para manter dados cadastrais de clientes, fornecedores, transportadoras e outros agentes que participam de fluxos financeiros, comerciais, fiscais, logísticos e de serviços.

## Por que clientes, fornecedores e transportadoras usam o mesmo cadastro

Na Omie, o cadastro concentra dados de identificação, endereço, contato, inscrições fiscais, tags, recomendações e vínculos operacionais em uma mesma entidade base. Essa modelagem evita duplicidade quando a mesma pessoa física ou jurídica atua em mais de um papel.

## Entidades relacionadas

- Cliente
- Fornecedor
- Transportadora
- Pedido
- NF-e
- Conta a Receber
- Conta a Pagar
- CRM
- Projeto
- Serviço
- Produtos
- Categorias
- Anexos

## Métodos relacionados

- `AlterarCliente`
- `AssociarCodIntCliente`
- `ConsultarCliente`
- `ExcluirCliente`
- `IncluirCliente`
- `IncluirClientesPorLote` - DEPRECATED na fonte oficial
- `ListarClientes`
- `ListarClientesResumido`
- `UpsertCliente`
- `UpsertClienteCpfCnpj`
- `UpsertClientesPorLote` - DEPRECATED na fonte oficial

## Exemplos completos

### curl

Consulte o documento do metodo escolhido. Este guia nao deve ser usado para montar requisicao final.

### Python

Consulte o documento do metodo escolhido. Este guia nao deve ser usado para montar requisicao final.

### JavaScript

Consulte o documento do metodo escolhido. Este guia nao deve ser usado para montar requisicao final.

## FAQ

### 1. Como uma LLM escolhe o metodo correto?

Ela deve identificar a intencao do usuario e direcionar para consulta, inclusao, alteracao, exclusao, listagem, associacao ou upsert.

### 2. Fornecedor usa o mesmo cadastro?

Sim. A base cadastral e compartilhada; o papel depende do fluxo operacional.

### 3. Transportadora usa o mesmo cadastro?

Sim. Transportadora pode ser representada na mesma base e relacionada a pedidos e documentos fiscais.

## Perguntas naturais

- Como escolher entre ConsultarCliente e ListarClientes?
- Como cadastrar fornecedor?
- Como localizar transportadora?
- Quando usar upsert?

## Tags para RAG

- omie
- clientes
- fornecedores
- transportadoras
- enterprise-rag
- graphrag

## GraphRAG

Consulte `graphs/omie/clientes.graph.md` para o grafo de relacionamento entre cliente, fornecedor, transportadora e dominios operacionais.

## Fonte oficial consultada

- https://app.omie.com.br/api/v1/geral/clientes/
