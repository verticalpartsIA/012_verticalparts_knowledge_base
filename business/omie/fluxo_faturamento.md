# Fluxo Faturamento - Omie

Status: Documentado automaticamente/a validar
Fonte principal: https://developer.omie.com.br/service-list/
Última atualização: 2026-07-04

## Objetivo

Consolidar como faturamento se relaciona com pedidos de venda, ordens de serviço, documentos fiscais e financeiro.

## Endpoints oficiais envolvidos

- Pedido de Venda - Faturamento: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
- Ordens de Serviço - Faturamento: https://app.omie.com.br/api/v1/servicos/osp/
- NF-e Consultas: https://app.omie.com.br/api/v1/produtos/nfconsultar/
- NFS-e Consultas: https://app.omie.com.br/api/v1/servicos/nfse/
- Contas a Receber: https://app.omie.com.br/api/v1/financas/contareceber/

## Decisão de método para LLM

- Para faturar venda de produto, usar Pedido de Venda - Faturamento.
- Para faturar serviço, usar Ordens de Serviço - Faturamento ou rotinas de contratos quando aplicável.
- Para consultar documentos fiscais emitidos, usar os serviços de consulta NF-e ou NFS-e.
