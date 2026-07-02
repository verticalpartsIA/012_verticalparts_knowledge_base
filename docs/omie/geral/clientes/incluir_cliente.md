---
service: ClientesCadastro
method: IncluirCliente
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: create
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - incluir
  - cadastro
---

# IncluirCliente

## Nome oficial do método

`IncluirCliente`

## Endpoint

`https://app.omie.com.br/api/v1/geral/clientes/`

## Domínio

Omie Geral > Clientes, Fornecedores e Transportadoras

## Entidade principal

Cliente / Fornecedor

## Entidades relacionadas

- Transportadora
- Pedido de venda
- Conta a pagar
- Conta a receber
- NF-e / NFS-e
- Ordem de serviço

## Quando usar

Use para incluir um novo cadastro de cliente/fornecedor no Omie.

## Quando não usar

- Não use para atualizar cadastro existente; use `AlterarCliente` ou avalie `UpsertCliente`.
- Não use para lote quando houver necessidade real de processamento em massa; avalie métodos por lote, observando que estão depreciados.
- Não use sem dados mínimos de identificação.

## Payload de entrada

Tipo oficial: `clientes_cadastro`.

Campos principais:

- `codigo_cliente_integracao`
- `razao_social`
- `cnpj_cpf`
- `nome_fantasia`
- `email`
- `telefone1_ddd`
- `telefone1_numero`
- `endereco`
- `endereco_numero`
- `bairro`
- `cidade`
- `cidade_ibge`
- `estado`
- `cep`
- `codigo_pais`
- `inscricao_estadual`
- `inscricao_municipal`
- `optante_simples_nacional`
- `contribuinte`
- `tags`
- `recomendacoes`

## Campos obrigatórios

- `razao_social` é indicado como obrigatório pela fonte oficial.
- Para emissão de NF-e/NFS-e, a fonte oficial marca como necessários campos de CPF/CNPJ, nome fantasia, endereço, estado, CEP, e-mail e dados fiscais específicos.
- Campos obrigatórios finais dependem do uso: cadastro simples, venda, financeiro, NF-e ou NFS-e.

## Campos opcionais

Campos de telefone, contato, homepage, observações, inscrições, recomendações, endereço de entrega, limite de crédito e tags podem ser usados conforme necessidade operacional.

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
  "call": "IncluirCliente",
  "param": [
    {
      "codigo_cliente_integracao": "CLI-EXEMPLO-001",
      "razao_social": "Cliente Exemplo Ltda",
      "nome_fantasia": "Cliente Exemplo",
      "cnpj_cpf": "00.000.000/0001-00",
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
  "descricao_status": "Cadastro incluído com sucesso"
}
```

## Erros comuns

- Razão social ausente.
- CPF/CNPJ duplicado ou inválido.
- Código de integração já existente.
- Dados fiscais insuficientes para emissão de documento.

## Observações importantes

Para integrações, prefira preencher `codigo_cliente_integracao` com identificador estável do sistema de origem.

## Perguntas que um usuário faria

- Como cadastrar cliente novo no Omie?
- Quais campos preciso para incluir fornecedor?
- Posso cadastrar transportadora pelo endpoint de clientes?
- Quais dados preciso para emissão de NF-e?

## Tags para RAG

`omie`, `clientes`, `incluir cliente`, `fornecedor`, `transportadora`, `cadastro novo`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
