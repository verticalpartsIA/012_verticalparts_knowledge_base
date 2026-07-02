---
service: ClientesCadastro
method: AlterarCliente
endpoint: https://app.omie.com.br/api/v1/geral/clientes/
domain: omie.geral
entity: cliente_fornecedor_transportadora
operation: update
status: oficial/a validar em integração
source: https://app.omie.com.br/api/v1/geral/clientes/
rag_tags:
  - omie
  - geral
  - clientes
  - fornecedores
  - transportadoras
  - alterar
  - cadastro
---

# AlterarCliente

## Nome oficial do método

`AlterarCliente`

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

Use para alterar dados de um cadastro já existente na base Omie, como razão social, nome fantasia, e-mail, telefone, endereço, tags, recomendações ou dados fiscais.

## Quando não usar

- Não use para criar cadastro novo sem confirmar existência.
- Não use para associação isolada de código interno; nesse caso avalie `AssociarCodIntCliente`.
- Não use para exclusão; use `ExcluirCliente`.

## Payload de entrada

Tipo oficial: `clientes_cadastro`.

Campos principais:

- `codigo_cliente_omie`
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
- `tags`
- `recomendacoes`
- `enderecoEntrega`

## Campos obrigatórios

- A documentação oficial marca `razao_social` como preenchimento obrigatório.
- Para emissão de NF-e/NFS-e, a documentação indica obrigatoriedade de campos como `cnpj_cpf`, `nome_fantasia`, endereço, `estado`, `cep`, `email`, `optante_simples_nacional`, `contribuinte` e outros dados fiscais.
- Valide contra a documentação oficial e contra o fluxo fiscal antes de produção.

## Campos opcionais

Campos como telefones, contato, homepage, inscrições, tags, observações, recomendações, limite de crédito e endereço de entrega aparecem como opcionais ou condicionais na documentação oficial.

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
  "call": "AlterarCliente",
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
  "descricao_status": "Cadastro alterado com sucesso"
}
```

## Erros comuns

- Cadastro não localizado pela chave informada.
- Campo obrigatório ausente.
- CPF/CNPJ inválido ou inconsistente para uso fiscal.
- Alteração de campo que depende de regra fiscal ou relacionamento já existente.

## Observações importantes

Use exemplos fictícios. Não inclua `app_key`, `app_secret`, tokens ou senhas. Campos fiscais e obrigatórios condicionais devem ser validados antes de uso em produção.

## Perguntas que um usuário faria

- Como alterar o e-mail de um cliente no Omie?
- Posso alterar razão social usando o código de integração?
- Quais campos preciso mandar para atualizar um fornecedor?
- AlterarCliente atualiza dados usados na NF-e?

## Tags para RAG

`omie`, `clientes`, `fornecedores`, `transportadoras`, `alterar cliente`, `cadastro`, `dados fiscais`

## Fonte oficial consultada

https://app.omie.com.br/api/v1/geral/clientes/
