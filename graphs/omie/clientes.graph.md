# GraphRAG: Omie Clientes

## Objetivo

Representar relacoes entre o cadastro central de clientes/fornecedores/transportadoras e dominios operacionais do ERP.

```mermaid
graph TD
  Cliente["Cliente"] --> Pedido["Pedido"]
  Cliente --> NF_e["NF-e"]
  Cliente --> ContaReceber["Conta a Receber"]
  Cliente --> CRM["CRM"]
  Cliente --> Projeto["Projeto"]
  Cliente --> Servico["Serviço"]
  Fornecedor["Fornecedor"] --> ContaPagar["Conta a Pagar"]
  Fornecedor --> Compras["Compras"]
  Transportadora["Transportadora"] --> Pedido
  Transportadora --> NF_e
  Pedido --> Produtos["Produtos"]
  Pedido --> Categorias["Categorias"]
  Pedido --> Anexos["Anexos"]
  Servico --> ContaReceber
  Projeto --> Categorias
  NF_e --> Fiscal["Fiscal"]
  ContaReceber --> Financeiro["Financeiro"]
  ContaPagar --> Financeiro
  Cliente --- Cadastro["ClientesCadastro"]
  Fornecedor --- Cadastro
  Transportadora --- Cadastro
```

## Leitura para LLM

A mesma entidade cadastral pode assumir papel de cliente, fornecedor ou transportadora. O papel operacional depende do fluxo em que o cadastro e usado: vendas, compras, financeiro, fiscal, servicos ou CRM.
