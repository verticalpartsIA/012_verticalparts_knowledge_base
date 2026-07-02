---
service: ClientesCadastro
method: ListarClientes
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: list_full
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - listar
  - paginacao
---

# ListarClientes

## Nome oficial do método

`ListarClientes`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Cadastro completo
- Sincronização
- Paginação
- Integrações de dados mestres

## Quando usar

Use para listar clientes cadastrados com retorno completo, especialmente em sincronizações, auditorias e cargas de dados mestres.

## Quando não usar

- Não use para consultar um único cadastro conhecido; use `ConsultarCliente`.
- Não use quando bastar retorno resumido; avalie `ListarClientesResumido`.
- Não use sem controle de paginação.

## Payload de entrada

Tipo oficial: `clientes_list_request`.

Campos principais:

- `pagina`
- `registros_por_pagina`
- `apenas_importado_api`
- `clientesFiltro`
- `ordenar_por`
- `ordem_decrescente`
- `filtrar_por_data_de`
- `filtrar_por_data_ate`

Alguns campos de filtro precisam ser validados contra a documentação oficial completa antes de implementação.

## Campos obrigatórios

- `pagina`
- `registros_por_pagina`

## Campos opcionais

- `apenas_importado_api`
- Filtros por cadastro, período e ordenação, a validar conforme necessidade.

## Payload de retorno

Tipo oficial: `clientes_listfull_response`.

Campos principais:

- `pagina`
- `total_de_paginas`
- `registros`
- `total_de_registros`
- `clientes_cadastro`

## Exemplo JSON de requisição

```json
{
  "call": "ListarClientes",
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
  "clientes_cadastro": [
    {
      "codigo_cliente_omie": 123456789,
      "codigo_cliente_integracao": "CLI-EXEMPLO-001",
      "razao_social": "Cliente Exemplo Ltda",
      "nome_fantasia": "Cliente Exemplo"
    }
  ]
}
```

## Erros comuns

- Paginação ausente.
- `registros_por_pagina` fora do limite aceito.
- Interpretação incorreta de `total_de_paginas`.
- Sincronização sem tratar páginas subsequentes.

## Observações importantes

Para RAG, este documento deve responder dúvidas sobre sincronização, listagem completa e paginação.

## Perguntas que um usuário faria

- Como listar todos os clientes do Omie?
- Como paginar o cadastro de clientes?
- Qual método uso para sincronizar clientes?

## Tags para RAG

`omie`, `clientes`, `listar clientes`, `paginacao`, `sincronizacao`, `cadastro completo`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
