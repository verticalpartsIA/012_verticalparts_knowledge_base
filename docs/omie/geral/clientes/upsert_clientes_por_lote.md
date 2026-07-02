---
service: ClientesCadastro
method: UpsertClientesPorLote
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: batch_upsert
status: deprecated/oficial
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - lote
  - upsert
  - deprecated
---

# UpsertClientesPorLote

## Nome oficial do método

`UpsertClientesPorLote`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Lote de clientes
- Sincronização em massa
- Cadastro de integração

## Quando usar

A fonte oficial lista o método para processamento em lote de upsert de clientes, limitado a 50 ocorrências por requisição.

## Quando não usar

- A própria fonte oficial marca este método como `DEPRECATED`.
- Não use em novas integrações sem validação técnica.
- Não use quando houver risco de sobrescrever cadastros sem auditoria.

## Payload de entrada

Tipo oficial: `clientes_lote_request`.

Campos principais:

- `lote`
- `clientes_cadastro`

## Campos obrigatórios

- `lote`
- `clientes_cadastro`
- Campos obrigatórios e condicionais de cada item seguem `clientes_cadastro`.

## Campos opcionais

Campos opcionais de cada cadastro seguem `clientes_cadastro`.

## Payload de retorno

Tipo oficial: `clientes_lote_response`.

Campos principais:

- `lote`
- `codigo_status`
- `descricao_status`

## Exemplo JSON de requisição

```json
{
  "call": "UpsertClientesPorLote",
  "param": [
    {
      "lote": 1,
      "clientes_cadastro": [
        {
          "codigo_cliente_integracao": "CLI-LOTE-001",
          "razao_social": "Cliente Lote Um Ltda",
          "nome_fantasia": "Cliente Lote Um"
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

- Uso de método depreciado sem justificativa.
- Lote com mais de 50 registros.
- Falha parcial por item inválido.
- Chaves duplicadas em itens do mesmo lote.

## Observações importantes

Para LLMs, sempre apontar o status depreciado e recomendar validação com a Omie antes de qualquer nova implementação.

## Perguntas que um usuário faria

- Existe upsert de clientes por lote?
- O método UpsertClientesPorLote ainda deve ser usado?
- Qual limite de clientes por lote?

## Tags para RAG

`omie`, `clientes`, `upsert lote`, `batch`, `deprecated`, `sincronizacao`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
