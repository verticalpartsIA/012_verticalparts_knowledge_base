# Generation Planner

O Generation Planner é o módulo determinístico responsável por calcular a ordem recomendada de documentação dos serviços da API Omie.

Ele não usa IA, LLM ou chamadas externas. A entrada principal é `factory/registry/omie_services.yaml` e a configuração de pesos fica em `factory/config/planner.yaml`.

Saídas principais:

- `factory/reports/planner_report.md`
- `factory/reports/documentation_plan.md`
- `factory/reports/service_dependency_graph.md`
