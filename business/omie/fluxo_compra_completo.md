# Fluxo Compra Completo - Omie

Status: Documentado automaticamente/a validar
Fonte principal: https://developer.omie.com.br/service-list/
Última atualização: 2026-07-04

## Objetivo

Representar o fluxo de compra da VerticalParts na Omie, conectando fornecedor, pedido, itens, aprovação, recebimento, estoque, contas a pagar e movimentos financeiros.

## Fluxo operacional

Fornecedor -> Pedido -> Itens -> Aprovação -> Recebimento -> Estoque -> Contas a Pagar -> Movimentos Financeiros.

## Endpoints oficiais envolvidos

- Fornecedores: https://app.omie.com.br/api/v1/geral/clientes/
- Pedido de Compra: https://app.omie.com.br/api/v1/produtos/pedidocompra/
- Produto x Fornecedor: https://app.omie.com.br/api/v1/estoque/produtofornecedor/
- Nota de Entrada: https://app.omie.com.br/api/v1/produtos/notaentrada/
- Recebimento de NF-e: https://app.omie.com.br/api/v1/produtos/recebimentonfe/
- Consulta Estoque: https://app.omie.com.br/api/v1/estoque/consulta/
- Movimento Estoque: https://app.omie.com.br/api/v1/estoque/movestoque/
- Contas a Pagar: https://app.omie.com.br/api/v1/financas/contapagar/
- Movimentos Financeiros: https://app.omie.com.br/api/v1/financas/mf/

## Observações para LLM/RAG

- Itens de compra são estruturas internas do pedido de compra, não endpoint separado identificado.
- A aprovação de compras não apareceu como serviço oficial na lista pública; implementar aprovação na camada de negócio quando necessário.
