# Relatório - Omie Commercial Suite Knowledge Base

Data: 2026-07-04
Branch: feature/omie-commercial-suite

## Ciclo obrigatório executado

- Discovery: documentação pública Omie service-list consultada e comparada ao registry local.
- Registry Compare: registry local contém 137 serviços; nenhum endpoint oficial de aprovação foi encontrado por nome/descrição.
- Planner: executado via `python factory/scripts/main.py --plan` e `--next-best-service`.
- Execution Engine: executado em modo `no-write` para Contas a Pagar; demais serviços com dependências pendentes foram registrados como bloqueados pelo estado determinístico.
- Knowledge Factory pipeline: executado para endpoints oficiais selecionados e publicado nas pastas canônicas.
- Knowledge Validation Engine: executado com score médio 84.06 para 98 documentos.

## Serviços documentados/cobertos

1. Pedido de Venda
2. Pedido de Venda - Faturamento
3. Pedido de Compra
4. Produtos
5. Consulta Estoque
6. Movimento Estoque
7. Contas a Pagar Lançamentos
8. NF-e Consultas
9. NF-e Importar
10. NFS-e Consultas
11. Ordens de Serviço Faturamento
12. Contas a Receber existente

## Módulos sem endpoint oficial específico

- Itens do Pedido: estrutura interna de pedidos de venda/compra, sem endpoint separado identificado no service-list.
- Aprovação de Pedido de Venda: sem endpoint oficial específico identificado; documentado em `business/omie/fluxo_aprovacao_vendas.md`.
- Aprovação de Pedido de Compra: sem endpoint oficial específico identificado; documentado em `business/omie/fluxo_aprovacao_compras.md`.

## Métricas preliminares

| Métrica | Valor |
|---|---:|
| Serviços cobertos | 12 |
| Métodos/documentos Omie | 98 |
| Schemas | 21 |
| Arquivos de perguntas | 13 |
| Perguntas | 925 |
| Chunks | 175 |
| Coverage antes | 1.46% |
| Coverage depois estimado | 8.76% |

## Fontes oficiais

- https://developer.omie.com.br/service-list/
- https://app.omie.com.br/api/v1/produtos/pedido/
- https://app.omie.com.br/api/v1/produtos/pedidocompra/
- https://app.omie.com.br/api/v1/produtos/pedidovendafat/
- https://app.omie.com.br/api/v1/geral/produtos/
- https://app.omie.com.br/api/v1/estoque/consulta/
- https://app.omie.com.br/api/v1/estoque/movestoque/
- https://app.omie.com.br/api/v1/financas/contareceber/
- https://app.omie.com.br/api/v1/financas/contapagar/
- https://app.omie.com.br/api/v1/produtos/nfconsultar/
- https://app.omie.com.br/api/v1/produtos/nfe/
- https://app.omie.com.br/api/v1/servicos/nfse/
- https://app.omie.com.br/api/v1/servicos/osp/


## Validações finais

- Knowledge Validation Engine: 98 documentos, score médio 84.06.
- Quality Ranking: `factory/reports/document_quality_ranking.md` atualizado.
- Improvement Report: `factory/reports/improvement_report.md` atualizado.
- Knowledge Score: `reports/knowledge_score.md` atualizado.
- Testes Factory: 25 passed.
- Testes Knowledge: 2 passed.
- py_compile: aprovado para scripts da Factory, knowledge_score e testes.
- JSON/YAML: validação executada.
- Segredos: sem credenciais reais; apenas menções preventivas e `.env.example` vazio.

## Conformidade com LLM_DOCUMENT_STANDARD

A documentação gerada segue a estrutura padrão da Factory com YAML, endpoint, método, fonte oficial, FAQ, perguntas naturais e tags RAG. Campos que exigem validação humana permanecem marcados como `Necessita validacao` ou `Documentado automaticamente/a validar`.
