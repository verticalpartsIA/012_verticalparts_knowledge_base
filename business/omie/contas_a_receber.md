# Business Knowledge: Omie Contas a Receber

## Como funciona no ERP

Contas a receber representam direitos financeiros da empresa contra clientes ou outros pagadores. No Omie, o serviço `LancamentoContaReceber` documenta operações para criar, alterar, consultar, listar, excluir, baixar, cancelar baixa, conciliar e ratear títulos.

## Relações principais

- Clientes: identificam o devedor do título.
- Pedidos de Venda: podem originar parcelas a receber.
- Ordem de Serviço: pode originar cobrança de serviço.
- NF-e e NFS-e: documentos fiscais podem gerar ou referenciar títulos.
- Categorias: classificam receitas.
- Bancos: representam conta corrente usada em previsão, baixa ou conciliação.
- Movimentos Financeiros: refletem eventos efetivados de baixa, conciliação e movimentação.

## Regras para LLM

A LLM deve distinguir título a receber de movimento financeiro. O título representa obrigação a receber; o movimento representa evento financeiro efetivado ou conciliado.

## Fonte oficial

- https://app.omie.com.br/api/v1/financas/contareceber/
