---
service: ClientesCadastro
method: UpsertCliente
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: upsert
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - upsert
  - inserir
  - atualizar
---

# UpsertCliente

## Nome oficial do método

`UpsertCliente`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Cadastro de integração
- Código interno
- Sincronização
- Sistemas legados

## Quando usar

Use quando a integração precisa criar ou atualizar um cadastro com base em uma chave estável, evitando decidir manualmente entre inclusão e alteração.

## Quando não usar

- Não use quando o fluxo exige separar claramente criação de atualização.
- Não use sem estratégia de chave única.
- Não use para operação por CPF/CNPJ quando a intenção for usar especificamente `UpsertClienteCpfCnpj`.

## Payload de entrada

Tipo oficial: `clientes_cadastro`.

Campos principais:

- `codigo_cliente_integracao`
- `codigo_cliente_omie`
- `razao_social`
- `cnpj_cpf`
- `nome_fantasia`
- `email`
- campos cadastrais, fiscais, contato, endereço, tags e recomendações

## Campos obrigatórios

- `razao_social` é obrigatório no tipo `clientes_cadastro`.
- A chave usada para upsert deve ser validada no desenho da integração.
- Campos fiscais são obrigatórios quando o cadastro será usado para NF-e/NFS-e.

## Campos opcionais

Demais campos de `clientes_cadastro`, conforme finalidade do cadastro.

## Payload de retorno

Tipo oficial: `clientes_status`.

Campos principais:

- `codigo_cliente_omie`
- `codigo_cliente_integracao`
- `codigo_status`
- `descricao_status`

## Exemplo JSON de requisição

```json
{
  "call": "UpsertCliente",
  "param": [
    {
      "codigo_cliente_integracao": "CLI-EXEMPLO-001",
      "razao_social": "Cliente Exemplo Ltda",
      "nome_fantasia": "Cliente Exemplo",
      "email": "contato@cliente-exemplo.com.br"
    }
  ]
}
```

## Exemplo JSON de resposta

```json
{
  "codigo_cliente_omie": 123456789,
  "codigo_cliente_integracao": "CLI-EXEMPLO-001",
  "codigo_status": "0",
  "descricao_status": "Cadastro processado com sucesso"
}
```

## Erros comuns

- Chave de integração ausente ou duplicada.
- Cadastro atualizado quando o esperado era criação.
- Campos fiscais incompletos para uso posterior.

## Observações importantes

Upsert é conveniente para sincronização, mas exige governança de identidade para não sobrescrever cadastros indevidamente.

## Perguntas que um usuário faria

- Como criar ou atualizar cliente em uma chamada?
- UpsertCliente substitui IncluirCliente?
- Qual chave devo usar no upsert?

## Tags para RAG

`omie`, `clientes`, `upsert`, `sincronizacao`, `incluir ou alterar`, `codigo integracao`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
