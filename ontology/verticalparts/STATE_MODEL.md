---
title: "State Model VerticalParts"
layer: "VerticalParts Enterprise Ontology"
doc_type: "state_model"
status: "Aguardando modelagem da VerticalParts"
last_review: "2026-07-04"
llm_ready: false
rag_ready: false
graph_ready: false
---

# State Model VerticalParts

## Status

Aguardando modelagem da VerticalParts.

## Máquinas de estado genéricas

### Proposta

`Rascunho` -> `Enviada` -> `Negociação` -> `Aprovada` -> `Cancelada` -> `Convertida`
### PedidoVenda

`Rascunho` -> `Aberto` -> `Aprovado` -> `Faturado` -> `Cancelado` -> `Concluído`
### PedidoCompra

`Rascunho` -> `Aberto` -> `Aprovado` -> `Recebido` -> `Cancelado` -> `Concluído`
### Contrato

`Rascunho` -> `Em análise` -> `Assinado` -> `Vigente` -> `Suspenso` -> `Encerrado`
### OrdemServico

`Aberta` -> `Planejada` -> `Em execução` -> `Concluída` -> `Cancelada` -> `Faturada`
### Compra

`Solicitada` -> `Cotada` -> `Aprovada` -> `Emitida` -> `Recebida` -> `Encerrada`
### Projeto

`Rascunho` -> `Em engenharia` -> `Aprovado` -> `Em implantação` -> `Entregue` -> `Encerrado`
### Equipamento

`Planejado` -> `Em instalação` -> `Ativo` -> `Em manutenção` -> `Modernização` -> `Desativado`
