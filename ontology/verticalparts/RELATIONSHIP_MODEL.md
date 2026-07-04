---
title: "Relationship Model VerticalParts"
layer: "VerticalParts Enterprise Ontology"
doc_type: "relationship_model"
status: "Aguardando modelagem da VerticalParts"
last_review: "2026-07-04"
llm_ready: false
rag_ready: false
graph_ready: false
---

# Relationship Model VerticalParts

## Status

Aguardando modelagem da VerticalParts.

## Relações genéricas

- `Cliente` --solicita_ou_recebe--> `Proposta`
- `Proposta` --converte_em--> `PedidoVenda`
- `PedidoVenda` --formaliza--> `Contrato`
- `Contrato` --origina--> `Projeto`
- `Projeto` --demanda--> `PedidoCompra`
- `PedidoCompra` --gera--> `Recebimento`
- `Recebimento` --atualiza--> `Estoque`
- `Estoque` --abastece--> `Instalação`
- `Instalação` --resulta_em--> `Entrega`
- `Entrega` --habilita--> `Faturamento`
- `Faturamento` --gera--> `ContaReceber`
- `ContaReceber` --liquida_por--> `RecebimentoFinanceiro`
- `Equipamento` --recebe--> `Preventiva`
- `Equipamento` --recebe--> `Corretiva`
- `Equipamento` --pode_receber--> `Modernização`

## Observação

As relações indicam estrutura semântica reutilizável e não descrevem processo real validado.
