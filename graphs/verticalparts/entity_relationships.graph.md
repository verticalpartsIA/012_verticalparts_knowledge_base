# GraphRAG - Entity Relationships VerticalParts

Status: Aguardando modelagem da VerticalParts

```mermaid
graph LR
  Cliente -->|solicita_ou_recebe| Proposta
  Proposta -->|converte_em| PedidoVenda
  PedidoVenda -->|formaliza| Contrato
  Contrato -->|origina| Projeto
  Projeto -->|demanda| PedidoCompra
  PedidoCompra -->|gera| Recebimento
  Recebimento -->|atualiza| Estoque
  Estoque -->|abastece| Instalação
  Instalação -->|resulta_em| Entrega
  Entrega -->|habilita| Faturamento
  Faturamento -->|gera| ContaReceber
  ContaReceber -->|liquida_por| RecebimentoFinanceiro
  Equipamento -->|recebe| Preventiva
  Equipamento -->|recebe| Corretiva
  Equipamento -->|pode_receber| Modernização
```
