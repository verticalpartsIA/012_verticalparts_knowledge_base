# GraphRAG - Contas a Pagar - Lançamentos

```mermaid
graph TD
  S["Contas a Pagar - Lançamentos"]
  S --> fornecedores["Fornecedores"]
  S --> categorias["Categorias"]
  S --> bancos["Bancos"]
  S --> movimentos_financeiros["Movimentos Financeiros"]
  S --> alterar_conta_pagar["AlterarContaPagar"]
  S --> cancelar_pagamento["CancelarPagamento"]
  S --> consultar_conta_pagar["ConsultarContaPagar"]
  S --> excluir_conta_pagar["ExcluirContaPagar"]
  S --> incluir_conta_pagar["IncluirContaPagar"]
  S --> incluir_conta_pagar_por_lote["IncluirContaPagarPorLote"]
  S --> lancar_pagamento["LancarPagamento"]
  S --> listar["Listar"]
  S --> listar_contas_pagar["ListarContasPagar"]
  S --> upsert_cadastro["Upsert"]
  S --> upsert_lote["UPSERT"]
  S --> upsert_conta_pagar["UpsertContaPagar"]
  S --> upsert_conta_pagar_por_lote["UpsertContaPagarPorLote"]
```
