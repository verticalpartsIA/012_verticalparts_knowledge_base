---
title: "Upsert"
service: "Contas a Pagar - Lançamentos"
domain: "omie.financas"
resource: "Contas a Pagar - Lançamentos"
method: "Upsert"
endpoint: "https://app.omie.com.br/api/v1/financas/contapagar/"
http_method: "POST"
version: "v1"
entity: "Contas a Pagar - Lançamentos"
related_entities:
  - Fornecedores
  - Categorias
  - Bancos
  - Movimentos Financeiros
related_methods: []
permissions: "Credenciais Omie validas fora deste repositorio"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/financas/contapagar/"
last_review: "2026-07-03"
tags:
  - omie
  - financeiro
  - contas-a-pagar
  - upsert_cadastro
keywords:
  - "Upsert"
  - "contas a pagar"
questions: 20
use_cases:
  - "Automatizar Upsert em Contas a Pagar"
business_area: "Financeiro"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---

# Upsert

## Objetivo

Documentar o metodo oficial `Upsert` do servico `Contas a Pagar - Lançamentos` para consulta por LLMs, RAG e automacoes da VerticalParts.

## Quando utilizar

Use este metodo quando a operacao financeira desejada corresponder ao metodo oficial `Upsert` no endpoint de Contas a Pagar.

## Quando NÃO utilizar

Nao utilize este metodo para Contas a Receber, cadastro de clientes, movimentos financeiros ja baixados ou regras de negocio nao confirmadas na fonte oficial.

## Fluxo de negocio

Fluxo de negócio: fornecedor ou documento financeiro -> titulo a pagar -> classificacao por categoria -> baixa ou manutencao do titulo -> conciliacao ou movimento financeiro relacionado.

## Entidades relacionadas

- Fornecedores
- Categorias
- Bancos
- Contas correntes
- Movimentos Financeiros
- Compras
- Notas de entrada

## Métodos relacionados

- Metodos de consulta e listagem de Contas a Pagar
- Metodos de baixa/cancelamento quando aplicavel
- Movimentos Financeiros
- Categorias
- Bancos

## Pre-requisitos

- Possuir credenciais Omie validas no ambiente seguro de execucao.
- Nao registrar `app_key`, `app_secret`, tokens, senhas ou dados reais neste repositorio.
- Validar payload contra a documentacao oficial antes de uso em producao.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/financas/contapagar/`

Descricao extraida da fonte oficial:

Upsert do Contas a Pagar Parâmetros: Retorno conta_pagar_cadastro_response : Resposta do Cadastro de Contas a Pagar Exemplo: Teste agora mesmo

## Campos obrigatorios

Necessita validacao.

## Campos opcionais

Necessita validacao.

## Regras de negocio

- Contas a Pagar representa obrigacoes financeiras da empresa com fornecedores ou despesas.
- O metodo deve ser escolhido conforme a intencao: incluir, alterar, consultar, listar, excluir, baixar, cancelar ou fazer upsert.
- Regras especificas de validacao fiscal, centro de custo, categoria e vencimento necessitam validacao operacional.

## Validacoes

- Confirmar campos obrigatorios.
- Confirmar tipos e formatos aceitos pela Omie.
- Conferir se o titulo ainda pode ser alterado, excluido, baixado ou cancelado.
- Validar se a operacao se aplica a lote quando o metodo mencionar lote.

## Restricoes

- Exemplos sao ficticios.
- Credenciais foram omitidas por seguranca.
- Campos nao extraidos com seguranca devem ser tratados como "Necessita validacao".

## Resposta esperada

Necessita validacao.

## Erros comuns

- Necessita validacao.

## Como resolver os erros

- Revisar campos obrigatorios e estrutura do `param`.
- Conferir codigo interno, codigo Omie e identificadores financeiros.
- Validar credenciais apenas em ambiente seguro.
- Consultar a fonte oficial quando o parser marcar algum detalhe como pendente.

## Casos de uso

- Automatizar a operacao `Upsert` em rotinas financeiras.
- Apoiar uma LLM na escolha do metodo correto para duvidas sobre Contas a Pagar.
- Preparar payloads ficticios para testes sem dados reais.

## Exemplos completos

### curl

```bash
curl -X POST "https://app.omie.com.br/api/v1/financas/contapagar/" \
  -H "Content-Type: application/json" \
  -d '{
  "call": "Upsert",
  "param": [
    {
      "codigo_lancamento_integracao": "PAG-FICTICIO-001",
      "codigo_cliente_fornecedor": 123456,
      "data_vencimento": "31/12/2026",
      "valor_documento": 100.0,
      "codigo_categoria": "9.99.99",
      "observacao": "Exemplo ficticio gerado pela Factory"
    }
  ]
}'
```

### Python

```python
import requests

payload = {
  "call": "Upsert",
  "param": [
    {
      "codigo_lancamento_integracao": "PAG-FICTICIO-001",
      "codigo_cliente_fornecedor": 123456,
      "data_vencimento": "31/12/2026",
      "valor_documento": 100.0,
      "codigo_categoria": "9.99.99",
      "observacao": "Exemplo ficticio gerado pela Factory"
    }
  ]
}
response = requests.post("https://app.omie.com.br/api/v1/financas/contapagar/", json=payload, timeout=30)
print(response.json())
```

### JavaScript

```javascript
const payload = {
  "call": "Upsert",
  "param": [
    {
      "codigo_lancamento_integracao": "PAG-FICTICIO-001",
      "codigo_cliente_fornecedor": 123456,
      "data_vencimento": "31/12/2026",
      "valor_documento": 100.0,
      "codigo_categoria": "9.99.99",
      "observacao": "Exemplo ficticio gerado pela Factory"
    }
  ]
};
const response = await fetch("https://app.omie.com.br/api/v1/financas/contapagar/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload)
});
console.log(await response.json());
```

### TypeScript

```typescript
const payload: Record<string, unknown> = {
  "call": "Upsert",
  "param": [
    {
      "codigo_lancamento_integracao": "PAG-FICTICIO-001",
      "codigo_cliente_fornecedor": 123456,
      "data_vencimento": "31/12/2026",
      "valor_documento": 100.0,
      "codigo_categoria": "9.99.99",
      "observacao": "Exemplo ficticio gerado pela Factory"
    }
  ]
};
const response = await fetch("https://app.omie.com.br/api/v1/financas/contapagar/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload)
});
console.log(await response.json());
```

### PHP

```php
$payload = {"call": "Upsert", "param": [{"exemplo": "ficticio"}]};
// Enviar via cliente HTTP configurado em ambiente seguro.
```

### C#

```csharp
var payload = @"{
  \"call\": \"Upsert\",
  \"param\": [
    {
      \"codigo_lancamento_integracao\": \"PAG-FICTICIO-001\",
      \"codigo_cliente_fornecedor\": 123456,
      \"data_vencimento\": \"31/12/2026\",
      \"valor_documento\": 100.0,
      \"codigo_categoria\": \"9.99.99\",
      \"observacao\": \"Exemplo ficticio gerado pela Factory\"
    }
  ]
}";
// Enviar com HttpClient configurado em ambiente seguro.
```

### Java

```java
String payload = "{   \"call\": \"Upsert\",   \"param\": [     {       \"codigo_lancamento_integracao\": \"PAG-FICTICIO-001\",       \"codigo_cliente_fornecedor\": 123456,       \"data_vencimento\": \"31/12/2026\",       \"valor_documento\": 100.0,       \"codigo_categoria\": \"9.99.99\",       \"observacao\": \"Exemplo ficticio gerado pela Factory\"     }   ] }";
// Enviar com cliente HTTP configurado em ambiente seguro.
```

### Delphi

```pascal
Payload := '{
  "call": "Upsert",
  "param": [
    {
      "codigo_lancamento_integracao": "PAG-FICTICIO-001",
      "codigo_cliente_fornecedor": 123456,
      "data_vencimento": "31/12/2026",
      "valor_documento": 100.0,
      "codigo_categoria": "9.99.99",
      "observacao": "Exemplo ficticio gerado pela Factory"
    }
  ]
}';
// Enviar com componente HTTP configurado em ambiente seguro.
```

### n8n

```json
{
  "node": "HTTP Request",
  "method": "POST",
  "url": "https://app.omie.com.br/api/v1/financas/contapagar/",
  "body": {
  "call": "Upsert",
  "param": [
    {
      "codigo_lancamento_integracao": "PAG-FICTICIO-001",
      "codigo_cliente_fornecedor": 123456,
      "data_vencimento": "31/12/2026",
      "valor_documento": 100.0,
      "codigo_categoria": "9.99.99",
      "observacao": "Exemplo ficticio gerado pela Factory"
    }
  ]
}
}
```

## FAQ

### 1. Quando devo usar o metodo Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 2. Quais campos sao obrigatorios para Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 3. Qual endpoint devo chamar para Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 4. Que retorno esperar do metodo Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 5. Como Upsert se relaciona com Contas a Pagar - Lançamentos?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 6. Upsert serve para fornecedor?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 7. Upsert altera algum movimento financeiro?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 8. Upsert exige categoria financeira?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 9. Posso usar Upsert com dados ficticios em teste?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 10. Quais erros comuns acontecem em Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 11. Como validar payload antes de chamar Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 12. Upsert pode ser usado em lote?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 13. Upsert depende de banco ou conta corrente?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 14. Como uma LLM escolhe Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 15. Quando nao devo usar Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 16. Upsert substitui consulta de movimentos financeiros?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 17. Upsert precisa de codigo Omie?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 18. Upsert precisa de codigo interno?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 19. Onde encontro a fonte oficial de Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

### 20. Quais tags RAG ajudam a recuperar Upsert?

Resposta: Necessita validacao contra a fonte oficial Omie.

## Perguntas naturais

- Quando devo usar o metodo Upsert?
- Quais campos sao obrigatorios para Upsert?
- Qual endpoint devo chamar para Upsert?
- Que retorno esperar do metodo Upsert?
- Como Upsert se relaciona com Contas a Pagar - Lançamentos?
- Upsert serve para fornecedor?
- Upsert altera algum movimento financeiro?
- Upsert exige categoria financeira?
- Posso usar Upsert com dados ficticios em teste?
- Quais erros comuns acontecem em Upsert?
- Como validar payload antes de chamar Upsert?
- Upsert pode ser usado em lote?
- Upsert depende de banco ou conta corrente?
- Como uma LLM escolhe Upsert?
- Quando nao devo usar Upsert?
- Upsert substitui consulta de movimentos financeiros?
- Upsert precisa de codigo Omie?
- Upsert precisa de codigo interno?
- Onde encontro a fonte oficial de Upsert?
- Quais tags RAG ajudam a recuperar Upsert?

## Tags para RAG

- omie
- financeiro
- contas-a-pagar
- upsert_cadastro
- enterprise-rag
- graphrag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/financas/contapagar/
