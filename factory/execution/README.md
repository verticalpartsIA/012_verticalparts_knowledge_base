# Execution Engine

O Execution Engine executa de forma determinística o próximo serviço recomendado pelo Generation Planner.

Ele não usa IA, LLM, GitHub automático, commits automáticos ou credenciais. O modo `--dry-run` valida o fluxo e registra estado/histórico sem gerar documentação final.

Comandos principais:

```bash
python factory/scripts/main.py --execute-next --dry-run
python factory/scripts/main.py --execute-service financas_contas_a_pagar_lancamentos --dry-run
python factory/scripts/main.py --status
python factory/scripts/main.py --history
```
