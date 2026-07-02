---
service: ClientesCadastro
method: ExcluirCliente
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: delete
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - excluir
  - cadastro
---

# ExcluirCliente

## Nome oficial do método

`ExcluirCliente`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Contas a pagar
- Contas a receber
- Pedidos de venda
- Ordens de serviço
- Documentos fiscais

## Quando usar

Use para excluir um cadastro de cliente/fornecedor da base, quando houver decisão operacional validada e ausência de impedimentos de relacionamento.

## Quando não usar

- Não use para desativação lógica se o processo exigir manter histórico.
- Não use quando houver títulos financeiros, pedidos ou documentos fiscais dependentes sem validação.
- Não use para corrigir dados; use `AlterarCliente`.

## Payload de entrada

Tipo oficial: `clientes_cadastro_chave`.

Campos principais:

- `codigo_cliente_omie`
- `codigo_cliente_integracao`

## Campos obrigatórios

Informe uma chave que identifique o cadastro. A obrigatoriedade exata entre `codigo_cliente_omie` e `codigo_cliente_integracao` deve ser validada.

## Campos opcionais

Sem campos opcionais relevantes além das chaves aceitas.

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
  "call": "ExcluirCliente",
  "param": [
    {
      "codigo_cliente_integracao": "CLI-EXEMPLO-001"
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
  "descricao_status": "Cadastro excluído com sucesso"
}
```

## Erros comuns

- Cadastro não encontrado.
- Cadastro vinculado a documentos, títulos ou movimentos.
- Chave de exclusão ausente.

## Observações importantes

Exclusão é uma operação destrutiva. Para LLMs, sempre sugerir validação humana antes de recomendar execução.

## Perguntas que um usuário faria

- Como excluir um cliente no Omie?
- Posso excluir fornecedor com contas a pagar?
- Qual chave uso para remover um cadastro?

## Tags para RAG

`omie`, `clientes`, `excluir cliente`, `remover cadastro`, `delete`, `cadastro`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
