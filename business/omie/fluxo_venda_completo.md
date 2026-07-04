# Fluxo Venda Completo - Omie

Status: Documentado automaticamente/a validar
Fonte principal: https://developer.omie.com.br/service-list/
Última atualização: 2026-07-04

## Objetivo

Representar o fluxo comercial de venda da VerticalParts na Omie, conectando cadastro, pedido, itens, aprovação de negócio, faturamento, NF-e e financeiro.

## Fluxo operacional

Cliente -> Pedido -> Itens -> Aprovação -> Faturamento -> NF-e -> Financeiro -> Contas a Receber -> Movimentos Financeiros.

## Endpoints oficiais envolvidos

- Clientes/fornecedores/transportadoras: https://app.omie.com.br/api/v1/geral/clientes/
- Pedido de Venda: https://app.omie.com.br/api/v1/produtos/pedido/
- Pedido de Venda - Faturamento: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
- Etapas de Pedido/Faturamento: https://app.omie.com.br/api/v1/produtos/pedidoetapas/ e https://app.omie.com.br/api/v1/produtos/etapafat/
- NF-e Consultas: https://app.omie.com.br/api/v1/produtos/nfconsultar/
- NF-e Importar: https://app.omie.com.br/api/v1/produtos/nfe/
- Contas a Receber: https://app.omie.com.br/api/v1/financas/contareceber/
- Movimentos Financeiros: https://app.omie.com.br/api/v1/financas/mf/

## Observações para LLM/RAG

- Itens do pedido fazem parte das estruturas do pedido de venda; não foi identificado endpoint oficial separado chamado Itens do Pedido.
- Aprovação de venda não foi identificada como endpoint oficial específico; tratar como regra de negócio ou etapa operacional.
- Não inferir emissão fiscal sem confirmar retorno do faturamento e documentos fiscais.
