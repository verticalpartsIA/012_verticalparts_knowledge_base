---
service: ClientesCadastro
method: UpsertClienteCpfCnpj
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: upsert_by_tax_id
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - upsert
  - cpf
  - cnpj
---

# UpsertClienteCpfCnpj

## Nome oficial do método

`UpsertClienteCpfCnpj`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- CPF/CNPJ
- Cadastro fiscal
- NF-e / NFS-e
- Sincronização cadastral

## Quando usar

Use quando a identidade principal da integração for o CPF/CNPJ e a operação desejada for criar ou atualizar o cadastro correspondente.

## Quando não usar

- Não use quando a identidade principal for `codigo_cliente_integracao`.
- Não use com CPF/CNPJ ausente, inválido ou compartilhado indevidamente.
- Não use quando for necessário separar inclusão e alteração para auditoria.

## Payload de entrada

Tipo oficial: `clientes_cadastro`.

Campos principais:

- `cnpj_cpf`
- `razao_social`
- `nome_fantasia`
- `email`
- campos cadastrais, fiscais, contato e endereço

## Campos obrigatórios

- `cnpj_cpf` é essencial para este método.
- `razao_social` é obrigatório no tipo `clientes_cadastro`.
- Campos fiscais e de endereço podem ser obrigatórios quando o cadastro for usado em NF-e/NFS-e.

## Campos opcionais

Demais campos de `clientes_cadastro`, conforme uso operacional.

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
  "call": "UpsertClienteCpfCnpj",
  "param": [
    {
      "cnpj_cpf": "00.000.000/0001-00",
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

- CPF/CNPJ inválido.
- CPF/CNPJ ausente.
- Duplicidade cadastral pré-existente.
- Dados fiscais insuficientes para o uso pretendido.

## Observações importantes

Este método deve ser tratado como upsert por documento fiscal. A LLM deve recomendar validação de CPF/CNPJ e política de duplicidade antes de produção.

## Perguntas que um usuário faria

- Como criar ou atualizar cliente pelo CNPJ?
- Qual método usa CPF/CNPJ como chave?
- Posso atualizar fornecedor pelo documento fiscal?

## Tags para RAG

`omie`, `clientes`, `upsert cpf cnpj`, `cnpj_cpf`, `documento fiscal`, `cadastro`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
