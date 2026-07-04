# Fluxo Aprovação de Vendas - Omie / VerticalParts

Status: Business Knowledge sem endpoint oficial específico
Fonte principal: https://developer.omie.com.br/service-list/
Última atualização: 2026-07-04

## Conclusão oficial

Não foi encontrado endpoint oficial de aprovação de pedido no service-list oficial nem no registry local da Factory. A aprovação deve ser tratada como etapa de negócio/configuração do ERP ou camada VerticalParts, usando endpoints oficiais de pedido, etapas, faturamento e financeiro.

## Fluxo recomendado

Pedido de Venda -> Etapa -> Validação interna -> Liberação para faturamento.

## Onde ocorre a aprovação

- Em configuração/processo operacional do ERP quando houver etapa configurável aplicável.
- Na camada de negócio da VerticalParts quando a regra exigir alçadas, limites, centros de custo, margem, estoque, crédito ou compliance.

## Endpoints participantes

- Pedido de Venda: https://app.omie.com.br/api/v1/produtos/pedido/
- Pedido de Compra: https://app.omie.com.br/api/v1/produtos/pedidocompra/
- Etapas de Pedido/Faturamento: https://app.omie.com.br/api/v1/produtos/pedidoetapas/ e https://app.omie.com.br/api/v1/produtos/etapafat/
- Faturamento de venda: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
- Contas a Receber: https://app.omie.com.br/api/v1/financas/contareceber/
- Contas a Pagar: https://app.omie.com.br/api/v1/financas/contapagar/

## Implementação VerticalParts

A VerticalParts pode manter uma tabela própria de aprovação, registrar status interno antes de chamar os endpoints de faturamento/financeiro, e usar os códigos de pedido Omie como chave de rastreabilidade.

## Observações para RAG

Não responder que existe endpoint oficial de aprovação sem citar fonte oficial. Quando perguntado sobre aprovação, explicar que a API pública lista serviços de pedido, etapas, faturamento e financeiro, mas não serviço específico de aprovação.
