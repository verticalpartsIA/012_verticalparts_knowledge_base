# Pedidos de Venda

## Título

Pedidos de venda

## Domínio

Omie Vendas

## Endpoint

`/produtos/pedido/`

## Métodos conhecidos

- `ListarPedidos`
- `ConsultarPedido`
- `IncluirPedido`
- `AlterarPedido`
- `ExcluirPedido`

## Quando usar

Use este endpoint para registrar, consultar e acompanhar pedidos de venda de produtos, incluindo vínculo com clientes, itens, condições comerciais e faturamento.

## Entidades relacionadas

- Cliente
- Produto
- Estoque
- Conta a receber
- Documento fiscal
- Transportadora

## Exemplos de perguntas que um usuário faria

- Como consultar um pedido de venda pelo número?
- Qual endpoint inclui pedido de venda de produto?
- Como relacionar itens e cliente em um pedido?
- Pedido de venda gera contas a receber automaticamente?

## Observações para RAG

Recupere este documento quando a pergunta mencionar venda, pedido, produto, cliente, item, faturamento ou integração comercial. Regras de geração financeira e fiscal devem ser validadas por fonte oficial ou teste controlado.

## Status

inicial/a validar
