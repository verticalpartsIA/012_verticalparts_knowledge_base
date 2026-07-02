---
service: ClientesCadastro
method: IncluirClientesPorLote
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: batch_create
status: deprecated/oficial
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - lote
  - deprecated
---

# IncluirClientesPorLote

## Nome oficial do método

`IncluirClientesPorLote`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Lote de clientes
- Cadastro de integração
- Processamento assíncrono ou agrupado

## Quando usar

A fonte oficial lista o método para inclusão de lote de cadastros, limitado a 50 ocorrências por requisição.

## Quando não usar

- A própria fonte oficial marca este método como `DEPRECATED`.
- Não use em novas integrações sem validação técnica e decisão explícita.
- Prefira inclusão individual ou estratégia atual recomendada pela Omie.

## Payload de entrada

Tipo oficial: `clientes_lote_request`.

Campos principais:

- `lote`
- `clientes_cadastro`

## Campos obrigatórios

- `lote`
- `clientes_cadastro`
- Campos obrigatórios de cada item seguem o tipo `clientes_cadastro`, incluindo `razao_social` e campos condicionais para emissão fiscal.

## Campos opcionais

Campos opcionais de cada cliente seguem `clientes_cadastro`.

## Payload de retorno

Tipo oficial: `clientes_lote_response`.

Campos principais:

- `lote`
- `codigo_status`
- `descricao_status`

## Exemplo JSON de requisição

```json
{
  "call": "IncluirClientesPorLote",
  "param": [
    {
      "lote": 1,
      "clientes_cadastro": [
        {
          "codigo_cliente_integracao": "CLI-LOTE-001",
          "razao_social": "Cliente Lote Um Ltda",
          "nome_fantasia": "Cliente Lote Um",
          "email": "contato1@exemplo.com.br"
        },
        {
          "codigo_cliente_integracao": "CLI-LOTE-002",
          "razao_social": "Cliente Lote Dois Ltda",
          "nome_fantasia": "Cliente Lote Dois",
          "email": "contato2@exemplo.com.br"
        }
      ]
    }
  ]
}
```

## Exemplo JSON de resposta

```json
{
  "lote": 1,
  "codigo_status": "0",
  "descricao_status": "Lote processado"
}
```

## Erros comuns

- Mais de 50 registros em uma requisição.
- Item do lote com campo obrigatório ausente.
- Duplicidade de CPF/CNPJ ou código de integração.
- Uso de método depreciado em fluxo novo.

## Observações importantes

Documento mantido porque o método existe na página oficial, mas a LLM deve destacar o status depreciado antes de recomendar uso.

## Perguntas que um usuário faria

- Existe inclusão de clientes por lote na Omie?
- Quantos clientes posso enviar por lote?
- O método de lote ainda é recomendado?

## Tags para RAG

`omie`, `clientes`, `incluir lote`, `batch`, `deprecated`, `cadastro`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
