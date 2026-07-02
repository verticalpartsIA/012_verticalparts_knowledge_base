---
service: ClientesCadastro
method: ListarClientesResumido
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: list_summary
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - listar
  - resumido
---

# ListarClientesResumido

## Nome oficial do método

`ListarClientesResumido`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Pesquisa de clientes
- Listagem resumida
- Sincronização leve

## Quando usar

Use para pesquisar ou listar cadastros com retorno resumido, quando a integração não precisa de todos os campos do cadastro completo.

## Quando não usar

- Não use quando precisar de todos os campos cadastrais; use `ListarClientes`.
- Não use para buscar um único cadastro por chave; use `ConsultarCliente`.

## Payload de entrada

Tipo oficial: `clientes_list_request`.

Campos principais:

- `pagina`
- `registros_por_pagina`
- `apenas_importado_api`
- filtros de cliente, data e ordenação a validar

## Campos obrigatórios

- `pagina`
- `registros_por_pagina`

## Campos opcionais

- `apenas_importado_api`
- Filtros adicionais da estrutura `clientes_list_request`, a validar em uso real.

## Payload de retorno

Tipo oficial: `clientes_list_response`.

Campos principais esperados:

- Dados de paginação.
- Lista resumida de clientes.
- Campos da estrutura resumida devem ser validados contra a documentação oficial antes de contrato final.

## Exemplo JSON de requisição

```json
{
  "call": "ListarClientesResumido",
  "param": [
    {
      "pagina": 1,
      "registros_por_pagina": 50,
      "apenas_importado_api": "N"
    }
  ]
}
```

## Exemplo JSON de resposta

```json
{
  "pagina": 1,
  "total_de_paginas": 1,
  "registros": 1,
  "total_de_registros": 1,
  "clientes_cadastro_resumido": [
    {
      "codigo_cliente": 123456789,
      "codigo_cliente_integracao": "CLI-EXEMPLO-001",
      "razao_social": "Cliente Exemplo Ltda"
    }
  ]
}
```

## Erros comuns

- Usar retorno resumido quando a aplicação depende de dados fiscais completos.
- Não tratar paginação.
- Assumir nomes de campos de retorno sem validar o client oficial.

## Observações importantes

A fonte oficial diferencia o retorno resumido de `ListarClientes`. Valide o shape exato do retorno antes de mapear em produção.

## Perguntas que um usuário faria

- Existe listagem resumida de clientes?
- Qual método uso para pesquisar clientes de forma leve?
- ListarClientesResumido traz todos os dados fiscais?

## Tags para RAG

`omie`, `clientes`, `listar resumido`, `pesquisa`, `paginacao`, `cadastro resumido`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
