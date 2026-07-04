# Roadmap VerticalParts Knowledge Base

Última atualização: 2026-07-03

## Infraestrutura — Omie Knowledge Factory

- Objetivo: substituir geração manual por uma Factory capaz de transformar qualquer URL oficial da API Omie em base Enterprise LLM/RAG.
- Prioridade: Alta
- Dependências: padrões Enterprise existentes, quality gate, coverage e dashboard
- Status: MVP funcional entregue / evolução autônoma iniciada

## Autonomous Knowledge Factory v1.0.0

- Objetivo: receber uma lista de URLs oficiais Omie e gerar automaticamente documentação, schemas, perguntas, chunks, graphs, business knowledge, coverage e dashboard.
- Prioridade: Alta
- Dependências: Omie Knowledge Factory MVP, Service Registry, Batch Runner e Quality Gate.
- Status: Em andamento
- Épicos: Service Registry, Batch Runner, Parser Robusto, Template Engine, Schema Generator avançado, FAQ Generator determinístico, Question Generator avançado, Graph Generator avançado, Business Knowledge Generator, Chunking Engine, Coverage Updater, Dashboard Updater, Quality Gate, PR Automation e Release Automation.

### Generation Planner

- Objetivo: decidir automaticamente a ordem recomendada de documentação dos serviços Omie.
- Prioridade: Alta
- Dependências: Service Registry, coverage e documentação existente.
- Status: Em implementação
- Entregáveis: scoring determinístico, classificação Critical/High/Medium/Low, plano de documentação, relatório de prioridade e grafo Mermaid de dependências.

### v0.7.0 — Execution Engine

- Objetivo: executar deterministicamente o próximo serviço recomendado pelo planner, com estado, histórico, relatório e quality gate básico.
- Prioridade: Alta
- Dependências: Generation Planner, crawler, parser, method extractor e generators.
- Status: Implementado
- Entregáveis: `factory/scripts/execution_engine.py`, `factory/state/factory_state.json`, `factory/reports/execution_report.md`, `factory/reports/execution_history.json` e CLI de execução/status/histórico.

### First Autonomous Documentation Cycle

- Objetivo: validar o primeiro ciclo autônomo seguro da Factory sem publicar documentação definitiva.
- Prioridade: Alta
- Dependências: Execution Engine, Generation Planner, registry, crawler, parser e geradores determinísticos.
- Status: Dry run/no-write concluído
- Serviço selecionado: Contas a Pagar - Lançamentos (`financas_contas_a_pagar_lancamentos`)
- Próximo passo: corrigir duplicidade de slug detectada em `Upsert` e preparar geração real em PR separado.

## FASE 1 — Clientes

- Objetivo: Consolidar cadastro base compartilhado entre clientes, fornecedores e transportadoras.
- Prioridade: Alta
- Dependências: Setup inicial
- Status: ✅ Concluído

## FASE 2 — Contas a Receber

- Objetivo: Documentar títulos a receber, baixa, conciliação e vínculos financeiros.
- Prioridade: Alta
- Dependências: Clientes
- Status: ✅ Concluído

## FASE 3 — Contas a Pagar

- Objetivo: Documentar obrigações financeiras, fornecedores, baixa e conciliação de despesas.
- Prioridade: Alta
- Dependências: Clientes, Categorias, Bancos
- Status: Planejado

## FASE 4 — Pedidos de Venda

- Objetivo: Documentar pedido comercial, itens, clientes e faturamento.
- Prioridade: Alta
- Dependências: Clientes, Produtos, Categorias
- Status: Planejado

## FASE 5 — Produtos

- Objetivo: Documentar cadastro de produtos, variações e dados fiscais/logísticos.
- Prioridade: Alta
- Dependências: Categorias, Estoque
- Status: Planejado

## FASE 6 — Categorias

- Objetivo: Documentar classificação financeira e operacional usada em receitas/despesas.
- Prioridade: Alta
- Dependências: Clientes, Financeiro
- Status: Planejado

## FASE 7 — Movimentos Financeiros

- Objetivo: Documentar movimentos efetivados, baixa, extrato e conciliação.
- Prioridade: Alta
- Dependências: Contas a Receber, Contas a Pagar, Bancos
- Status: Planejado

## FASE 8 — NF-e

- Objetivo: Documentar emissão, consulta, XML, DANFE e vínculos fiscais.
- Prioridade: Alta
- Dependências: Clientes, Produtos, Pedidos de Venda
- Status: Planejado

## FASE 9 — NFS-e

- Objetivo: Documentar serviços, emissão, consulta e documentos fiscais de serviço.
- Prioridade: Alta
- Dependências: Clientes, Serviços, Ordens de Serviço
- Status: Planejado

## FASE 10 — Ordens de Serviço

- Objetivo: Documentar OS, serviços, faturamento e vínculos com NFS-e.
- Prioridade: Média
- Dependências: Clientes, Serviços, NFS-e
- Status: Planejado

## FASE 11 — Estoque

- Objetivo: Documentar saldo, movimentações e locais de estoque.
- Prioridade: Média
- Dependências: Produtos
- Status: Planejado

## FASE 12 — Compras

- Objetivo: Documentar pedidos de compra, notas de entrada e fornecedores.
- Prioridade: Média
- Dependências: Fornecedores, Produtos, Contas a Pagar
- Status: Planejado

## FASE 13 — CRM

- Objetivo: Documentar contas, contatos, oportunidades e funil comercial.
- Prioridade: Média
- Dependências: Clientes
- Status: Planejado

## FASE 14 — Cadastros Gerais

- Objetivo: Documentar cadastros auxiliares e listas de apoio.
- Prioridade: Média
- Dependências: Domínios principais
- Status: Planejado

## FASE 15 — Cobertura completa da API Omie

- Objetivo: Completar todos os serviços oficiais da lista Omie.
- Prioridade: Alta
- Dependências: Fases 1 a 14
- Status: Planejado
## Omie Commercial Suite

Status: Em PR
Prioridade: Alta
Data: 2026-07-04

Objetivo: documentar os fluxos estratégicos Venda, Compra, Faturamento, NF-e, NFS-e, Produtos, Estoque e Financeiro usando a Factory existente.

Entregas:

- docs, schemas, datasets/questions, rag/chunks, graphs e business docs para os serviços oficiais selecionados
- fluxos completos de venda, compra, faturamento e aprovações
- coverage estimado de 1.46% para 8.76%
