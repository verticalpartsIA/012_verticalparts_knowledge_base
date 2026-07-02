---
service: ClientesCadastro
method: AssociarCodIntCliente
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: associate_internal_code
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - codigo-integracao
  - associar
---

# AssociarCodIntCliente

## Nome oficial do método

`AssociarCodIntCliente`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Sistemas legados
- Integrações internas
- Código Omie
- Código de integração

## Quando usar

Use para associar um código interno de integração a um cadastro de cliente/fornecedor já existente no Omie.

## Quando não usar

- Não use para criar cadastro completo.
- Não use para alterar dados cadastrais amplos; use `AlterarCliente`.
- Não use se o cadastro Omie ainda não existir.

## Payload de entrada

Tipo oficial: `clientes_cadastro_chave`.

Campos principais:

- `codigo_cliente_omie`
- `codigo_cliente_integracao`

## Campos obrigatórios

A chave precisa identificar o cadastro Omie e o código interno a associar. A obrigatoriedade exata de combinação dos campos deve ser validada na documentação oficial e em teste controlado.

## Campos opcionais

Não há campos opcionais relevantes além da própria composição da chave informada pela fonte oficial.

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
  "call": "AssociarCodIntCliente",
  "param": [
    {
      "codigo_cliente_omie": 123456789,
      "codigo_cliente_integracao": "CLI-LEGADO-001"
    }
  ]
}
```

## Exemplo JSON de resposta

```json
{
  "codigo_cliente_omie": 123456789,
  "codigo_cliente_integracao": "CLI-LEGADO-001",
  "codigo_status": "0",
  "descricao_status": "Código de integração associado com sucesso"
}
```

## Erros comuns

- Código Omie inexistente.
- Código de integração já associado a outro cadastro.
- Chave incompleta ou inconsistente.

## Observações importantes

Este método é especialmente útil em migrações e integrações com sistemas legados. Não use credenciais reais em exemplos.

## Perguntas que um usuário faria

- Como vincular meu código interno ao cliente Omie?
- Qual método associa o código legado ao cadastro?
- Posso associar código interno sem alterar o cliente?

## Tags para RAG

`omie`, `clientes`, `codigo interno`, `codigo integracao`, `legado`, `associar`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
