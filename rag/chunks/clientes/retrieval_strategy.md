# Estratégia de Recuperação: Clientes

## Busca híbrida

Combine busca vetorial com busca lexical por método oficial, entidade, CPF/CNPJ, código interno, código Omie e status.

## Reranking

Reordene resultados priorizando método exato, status documentado oficialmente, proximidade semântica e presença de payload.

## GraphRAG

Use `graphs/omie/clientes.graph.md` para expandir consultas que envolvem relações entre cliente, fornecedor, transportadora, financeiro, fiscal, vendas, compras e serviços.

## Critério de resposta

A resposta deve citar o documento de origem e declarar se o trecho é "Documentado oficialmente" ou "Necessita validação".
