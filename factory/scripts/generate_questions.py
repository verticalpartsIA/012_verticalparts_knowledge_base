"""Gerador deterministico de perguntas naturais."""

from __future__ import annotations

import json
from pathlib import Path

from models import ServiceInfo, slugify


def generate_questions(service: ServiceInfo, output_dir: Path, dry_run: bool = False) -> list[Path]:
    path = output_dir / "datasets" / "questions" / f"{slugify(service.name)}.json"
    questions: list[dict[str, str]] = []
    for method in service.methods:
        for question in questions_for_method(method.name, service.name):
            questions.append({"method": method.name, "question": question, "source": service.source_url})
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")
    return [path]


def questions_for_method(method_name: str, service_name: str) -> list[str]:
    return [
        f"Quando devo usar {method_name} em {service_name}?",
        f"Quais parametros o metodo {method_name} aceita?",
        f"Quais campos sao obrigatorios para chamar {method_name}?",
        f"Qual exemplo de payload ficticio para {method_name}?",
        f"Que resposta o metodo {method_name} retorna?",
        f"{method_name} serve para fornecedor em contas a pagar?",
        f"{method_name} exige categoria financeira?",
        f"{method_name} depende de banco ou conta corrente?",
        f"Como validar o payload de {method_name} antes de enviar?",
        f"Quais erros comuns podem ocorrer em {method_name}?",
        f"Quando nao devo usar {method_name}?",
        f"{method_name} pode ser usado em lote?",
        f"{method_name} gera movimento financeiro?",
        f"{method_name} altera titulo ja baixado?",
        f"Qual fonte oficial valida {method_name}?",
        f"Como uma LLM escolhe {method_name} para uma pergunta do usuario?",
        f"{method_name} usa codigo Omie ou codigo interno?",
        f"Que retorno devo esperar de {method_name}?",
        f"Como testar {method_name} com dados ficticios?",
        f"Quais tags RAG ajudam a recuperar {method_name}?",
    ]
