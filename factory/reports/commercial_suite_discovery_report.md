# Discovery e Registry Compare - Commercial Suite

Fonte oficial: https://developer.omie.com.br/service-list/
Data: 2026-07-04

## Resultado

- Serviços no registry local: 137
- Serviços estratégicos selecionados para esta geração: 12, sendo 11 gerados por endpoint e 1 reaproveitado da base existente (Contas a Receber)
- Endpoint oficial específico para Aprovação de Pedido de Venda: não encontrado no service-list nem no registry
- Endpoint oficial específico para Aprovação de Pedido de Compra: não encontrado no service-list nem no registry

## Serviços utilizados

- compras_estoque_e_producao_pedidos_de_venda - Pedidos de Venda - https://app.omie.com.br/api/v1/produtos/pedido/
- compras_estoque_e_producao_pedidos_de_venda_faturamento - Pedidos de Venda Faturamento - https://app.omie.com.br/api/v1/produtos/pedidovendafat/
- compras_estoque_e_producao_pedidos_de_compra - Pedidos de Compra - https://app.omie.com.br/api/v1/produtos/pedidocompra/
- geral_produtos - Produtos - https://app.omie.com.br/api/v1/geral/produtos/
- compras_estoque_e_producao_consulta_estoque - Consulta Estoque - https://app.omie.com.br/api/v1/estoque/consulta/
- compras_estoque_e_producao_movimento_estoque - Movimento Estoque - https://app.omie.com.br/api/v1/estoque/movestoque/
- financas_contas_a_pagar_lancamentos - Contas a Pagar Lançamentos - https://app.omie.com.br/api/v1/financas/contapagar/
- compras_estoque_e_producao_consultas - NF-e Consultas - https://app.omie.com.br/api/v1/produtos/nfconsultar/
- compras_estoque_e_producao_importar - NF-e Importar - https://app.omie.com.br/api/v1/produtos/nfe/
- servicos_e_nfs_e_consultas - NFS-e Consultas - https://app.omie.com.br/api/v1/servicos/nfse/
- servicos_e_nfs_e_ordens_de_servico_faturamento - Ordens de Serviço Faturamento - https://app.omie.com.br/api/v1/servicos/osp/

## Lacunas oficiais registradas

- Itens do Pedido: tratado como estrutura interna dos endpoints de pedido, sem endpoint separado encontrado.
- Aprovação de Pedido de Venda: Business Knowledge criada sem endpoint oficial inventado.
- Aprovação de Pedido de Compra: Business Knowledge criada sem endpoint oficial inventado.
