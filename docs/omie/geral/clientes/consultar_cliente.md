---
service: ClientesCadastro
method: ConsultarCliente
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: read
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - consultar
  - cadastro
---

# ConsultarCliente

## Nome oficial do método

`ConsultarCliente`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Transportadora
- Cadastro de integração
- Pedido de venda
- Conta a pagar
- Conta a receber
- Documento fiscal

## Quando usar

Use para consultar os dados de um cliente/fornecedor específico usando uma chave de pesquisa.

## Quando não usar

- Não use para listagem paginada; use `ListarClientes` ou `ListarClientesResumido`.
- Não use para criar ou alterar cadastro.
- Não use quando houver apenas filtros amplos de pesquisa sem chave clara.

## Payload de entrada

Tipo oficial: `clientes_cadastro_chave`.

Campos principais:

- `codigo_cliente_omie`
- `codigo_cliente_integracao`

## Campos obrigatórios

Informe uma chave capaz de localizar o cadastro, como `codigo_cliente_omie` ou `codigo_cliente_integracao`. A combinação exata aceita deve ser validada contra a documentação oficial e testes controlados.

## Campos opcionais

Não há campos opcionais de consulta além das alternativas de chave listadas na fonte oficial.

## Payload de retorno

Tipo oficial: `clientes_cadastro`.

Retorna o cadastro do cliente/fornecedor com campos cadastrais, fiscais, contato, endereço, tags, recomendações e metadados disponíveis.

## Exemplo JSON de requisição

```json
{
  "call": "ConsultarCliente",
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
  "razao_social": "Cliente Exemplo Ltda",
  "nome_fantasia": "Cliente Exemplo",
  "cnpj_cpf": "00.000.000/0001-00",
  "email": "contato@cliente-exemplo.com.br",
  "inativo": "N"
}
```

## Erros comuns

- Cliente não encontrado.
- Chave de consulta ausente.
- Código de integração divergente do cadastro esperado.

## Observações importantes

Use `ConsultarCliente` antes de alterações sensíveis quando o fluxo exigir confirmar o estado atual do cadastro.

## Perguntas que um usuário faria

- Como consultar cliente pelo código de integração?
- Como saber se um fornecedor já existe no Omie?
- Qual método retorna os dados cadastrais completos?

## Tags para RAG

`omie`, `clientes`, `consultar cliente`, `codigo cliente omie`, `codigo integracao`, `cadastro`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
