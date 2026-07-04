# Knowledge Validation Engine

O Knowledge Validation Engine executa validações determinísticas sobre a documentação produzida pela Omie Knowledge Factory.

Ele não usa IA, não usa LLM e não altera documentos. A saída oficial são relatórios em `factory/reports/`.

Comandos principais:

- `python factory/scripts/main.py --validate`
- `python factory/scripts/main.py --validate-service <service_id>`
- `python factory/scripts/main.py --validate-all`
- `python factory/scripts/main.py --improvement-report`
- `python factory/scripts/main.py --quality-ranking`
