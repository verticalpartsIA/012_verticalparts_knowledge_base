# Clientes, Fornecedores e Transportadoras

## Título

Clientes, fornecedores e transportadoras

## Domínio

Omie Geral

## Endpoint

`/geral/clientes/`

## Métodos conhecidos

- `ListarClientes`
- `ConsultarCliente`
- `IncluirCliente`
- `AlterarCliente`
- `ExcluirCliente`

## Quando usar

Use este grupo de endpoints para consultar, cadastrar e manter entidades cadastrais usadas em operações comerciais, financeiras, logísticas e fiscais. A mesma base cadastral pode representar clientes, fornecedores, transportadoras ou outros participantes relacionados ao fluxo da empresa.

## Entidades relacionadas

- Cliente
- Fornecedor
- Transportadora
- Pedido de venda
- Conta a pagar
- Conta a receber
- Documento fiscal

## Exemplos de perguntas que um usuário faria

- Como consultar um cliente pelo código no Omie?
- Qual endpoint uso para cadastrar um fornecedor?
- Transportadora usa o mesmo cadastro de clientes e fornecedores?
- Quais dados cadastrais preciso validar antes de emitir um pedido?

## Observações para RAG

Este documento deve ser recuperado quando a pergunta mencionar cadastro, cliente, fornecedor, transportadora, participante, código de cliente ou dados mestres. O agente deve sinalizar que métodos e campos precisam ser validados contra fonte oficial antes de implementação.

## Status

inicial/a validar
