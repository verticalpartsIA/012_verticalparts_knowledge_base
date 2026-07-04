# GraphRAG - Lead to Cash

Status: Aguardando modelagem da VerticalParts

```mermaid
graph TD
  Lead["Lead"] --> Proposta["Proposta"]
  Proposta["Proposta"] --> Pedido["Pedido"]
  Pedido["Pedido"] --> Contrato["Contrato"]
  Contrato["Contrato"] --> Faturamento["Faturamento"]
  Faturamento["Faturamento"] --> Recebimento["Recebimento"]
```

> Estrutura conceitual inicial. Relações reais serão preenchidas posteriormente.
