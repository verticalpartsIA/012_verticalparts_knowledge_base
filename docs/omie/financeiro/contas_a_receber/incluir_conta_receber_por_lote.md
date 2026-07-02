---
title: "IncluirContaReceberPorLote - Omie Financeiro Contas a Receber"
service: "LancamentoContaReceber"
domain: "omie.financeiro"
resource: "contas_a_receber"
method: "IncluirContaReceberPorLote"
endpoint: "https://app.omie.com.br/api/v1/financas/contareceber/"
http_method: "POST"
version: "1"
entity: "conta_a_receber"
related_entities:
  - Cliente
  - Pedido de Venda
  - Ordem de Serviço
  - NF-e
  - NFS-e
  - Categorias
  - Bancos
  - Movimentos Financeiros
related_methods:
  - ConsultarContaReceber
  - IncluirContaReceber
  - AlterarContaReceber
  - ListarContasReceber
permissions:
  - "Necessita credenciais Omie validas fora do repositorio"
  - "Nao documentar chaves, segredos ou senhas"
complexity: "media"
status: "Documentado oficialmente / Necessita validação em integração"
source: "https://app.omie.com.br/api/v1/financas/contareceber/"
last_review: "2026-07-02"
tags:
  - omie
  - financeiro
  - contas-a-receber
  - inclusao_lote
  - enterprise-rag
keywords:
  - LancamentoContaReceber
  - IncluirContaReceberPorLote
  - Contas a Receber
  - RAG
questions:
  - "Como usar IncluirContaReceberPorLote?"
  - "Como documentar Contas a Receber para LLM?"
  - "Quais campos necessitam validação?"
use_cases:
  - conciliacao_financeira
  - baixa_recebimento
  - sincronizacao_financeira
  - assistente_llm
business_area: "ERP / Financeiro / Contas a Receber"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# IncluirContaReceberPorLote

## Objetivo

Inclui contas a receber por lote. O conteúdo é preparado para LLMs, RAG e GraphRAG, com separação clara entre "Documentado oficialmente" e "Necessita validação".

## Quando utilizar

Utilize quando a intenção do usuário estiver ligada à operação `inclusao_lote` em contas a receber do Omie.

## Quando NÃO utilizar

Não utilize para contas a pagar, movimentos financeiros genéricos, cadastro de clientes ou pedidos de venda. Nesses casos, a LLM deve direcionar para o domínio correto.

## Fluxo de negócio

1. Identificar o cliente ou origem do título.
2. Relacionar o título com pedido, ordem de serviço, NF-e, NFS-e ou lançamento manual quando aplicável.
3. Aplicar categoria financeira, conta corrente/banco e datas.
4. Executar a operação `IncluirContaReceberPorLote` com payload fictício em exemplos ou dados autorizados em produção.
5. Interpretar retorno, status e relação com movimentos financeiros.

## Entidades relacionadas

- Cliente
- Pedidos de Venda
- Ordem de Serviço
- NF-e
- NFS-e
- Categorias
- Bancos
- Movimentos Financeiros

## Métodos relacionados

- `IncluirContaReceber`
- `IncluirDistribuicaoDepartamento`

## Pré-requisitos

- Credenciais Omie válidas fora do repositório.
- Cliente/fornecedor cadastrado quando o título exigir vínculo.
- Categoria financeira validada.
- Conta corrente/banco validado para baixa, conciliação ou previsão.
- Fonte oficial consultada antes de produção.

## Payload

- Tipo oficial de entrada: `conta_receber_lote`.
- Tipo oficial de retorno: `conta_receber_lote_response`.
- Endpoint oficial: `https://app.omie.com.br/api/v1/financas/contareceber/`.

## Campos obrigatórios

- `lote`
- `conta_receber_cadastro`

## Campos opcionais

- `numero_documento`
- `numero_documento_fiscal`
- `numero_pedido`
- `chave_nfe`
- `observacao`
- `codigo_projeto`
- `categorias`
- `distribuicao`
- `nCodPedido`
- `nCodOS`
- Campos adicionais devem ser tratados como "Necessita validação" quando não houver confirmação no fluxo.

## Regras de negócio

- Contas a receber representam direitos financeiros a receber de clientes ou fontes operacionais.
- Podem nascer de pedido de venda, ordem de serviço, NF-e, NFS-e ou lançamento manual.
- Categorias e bancos influenciam relatórios, conciliação, baixa e movimentos financeiros.
- Baixa e conciliação devem preservar rastreabilidade financeira.

## Validações

- Validar cliente antes de criar título.
- Validar vencimento, previsão e valor.
- Validar categoria e conta corrente.
- Validar relação com NF-e/NFS-e quando houver documento fiscal.
- Validar se o lançamento pode ser alterado, excluído, baixado ou conciliado.

## Restrições

- Não armazenar `app_key`, `app_secret`, token, senha ou bearer.
- Não usar dados reais em exemplos.
- Não assumir regra fiscal sem validação.
- Não confundir contas a receber com movimentos financeiros já efetivados.

## Resposta esperada

Retorno oficial: `conta_receber_lote_response`. A interpretação de códigos e mensagens deve ser validada em integração.

## Erros comuns

- Cliente inexistente.
- Categoria inválida.
- Conta corrente inexistente.
- Valor ou data ausente.
- Baixa já realizada.
- Tentativa de conciliar sem baixa válida.

## Como resolver os erros

- Consultar o título antes da operação.
- Validar cliente, categoria e banco.
- Conferir se há baixa ou conciliação anterior.
- Revisar campos obrigatórios do tipo `conta_receber_lote`.
- Marcar lacunas como "Necessita validação".

## Casos de uso

- Assistente financeiro respondendo dúvidas sobre títulos a receber.
- Integração entre vendas, serviços e financeiro.
- Sincronização de contas a receber para BI financeiro.
- Auditoria de baixas, conciliações e vínculos fiscais.
- GraphRAG conectando clientes, pedidos, documentos fiscais e movimentos.

## Exemplos completos

> Exemplos fictícios. Credenciais Omie foram omitidas de propósito.

### JSON base

```json
{
  "call": "IncluirContaReceberPorLote",
  "param": [
    {
      "lote": 100,
      "conta_receber_cadastro": [
{
  "codigo_lancamento_integracao": "CR-FICTICIO-001",
  "codigo_cliente_fornecedor": 123456,
  "data_vencimento": "31/12/2026",
  "valor_documento": 100.0,
  "codigo_categoria": "1.01.02",
  "data_previsao": "31/12/2026",
  "id_conta_corrente": 987654
}
      ]
    }
  ]
}
```

### curl

```bash
curl -X POST "https://app.omie.com.br/api/v1/financas/contareceber/" -H "Content-Type: application/json" -d '{"call": "IncluirContaReceberPorLote", "param": [{"lote": 100, "conta_receber_cadastro": [{"codigo_lancamento_integracao": "CR-FICTICIO-001", "codigo_cliente_fornecedor": 123456, "data_vencimento": "31/12/2026", "valor_documento": 100.0, "codigo_categoria": "1.01.02", "data_previsao": "31/12/2026", "id_conta_corrente": 987654}]}]}'
```

### Python

```python
import requests

payload = {'call': 'IncluirContaReceberPorLote', 'param': [{'lote': 100, 'conta_receber_cadastro': [{'codigo_lancamento_integracao': 'CR-FICTICIO-001', 'codigo_cliente_fornecedor': 123456, 'data_vencimento': '31/12/2026', 'valor_documento': 100.0, 'codigo_categoria': '1.01.02', 'data_previsao': '31/12/2026', 'id_conta_corrente': 987654}]}]}
response = requests.post("https://app.omie.com.br/api/v1/financas/contareceber/", json=payload, timeout=30)
print(response.json())
```

### JavaScript

```javascript
const payload = {
  "call": "IncluirContaReceberPorLote",
  "param": [
    {
      "lote": 100,
      "conta_receber_cadastro": [
{
  "codigo_lancamento_integracao": "CR-FICTICIO-001",
  "codigo_cliente_fornecedor": 123456,
  "data_vencimento": "31/12/2026",
  "valor_documento": 100.0,
  "codigo_categoria": "1.01.02",
  "data_previsao": "31/12/2026",
  "id_conta_corrente": 987654
}
      ]
    }
  ]
};
const response = await fetch("https://app.omie.com.br/api/v1/financas/contareceber/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload)
});
console.log(await response.json());
```

### TypeScript

```typescript
type OmieRequest = { call: string; param: Array<Record<string, unknown>> };
const payload: OmieRequest = {
  "call": "IncluirContaReceberPorLote",
  "param": [
    {
      "lote": 100,
      "conta_receber_cadastro": [
{
  "codigo_lancamento_integracao": "CR-FICTICIO-001",
  "codigo_cliente_fornecedor": 123456,
  "data_vencimento": "31/12/2026",
  "valor_documento": 100.0,
  "codigo_categoria": "1.01.02",
  "data_previsao": "31/12/2026",
  "id_conta_corrente": 987654
}
      ]
    }
  ]
};
const response = await fetch("https://app.omie.com.br/api/v1/financas/contareceber/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload)
});
const data: unknown = await response.json();
console.log(data);
```

### PHP

```php
<?php
$payload = {"call": "IncluirContaReceberPorLote", "param": [{"lote": 100, "conta_receber_cadastro": [{"codigo_lancamento_integracao": "CR-FICTICIO-001", "codigo_cliente_fornecedor": 123456, "data_vencimento": "31/12/2026", "valor_documento": 100.0, "codigo_categoria": "1.01.02", "data_previsao": "31/12/2026", "id_conta_corrente": 987654}]}]};
$ch = curl_init("https://app.omie.com.br/api/v1/financas/contareceber/");
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/json"]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
echo curl_exec($ch);
curl_close($ch);
```

### C#

```csharp
using System.Net.Http.Json;
var payload = new { call = "IncluirContaReceberPorLote", param = new object[] { new { codigo_lancamento_integracao = "CR-FICTICIO-001" } } };
using var client = new HttpClient();
var response = await client.PostAsJsonAsync("https://app.omie.com.br/api/v1/financas/contareceber/", payload);
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

### Java

```java
var client = java.net.http.HttpClient.newHttpClient();
var request = java.net.http.HttpRequest.newBuilder()
    .uri(java.net.URI.create("https://app.omie.com.br/api/v1/financas/contareceber/"))
    .header("Content-Type", "application/json")
    .POST(java.net.http.HttpRequest.BodyPublishers.ofString("""{
  "call": "IncluirContaReceberPorLote",
  "param": [
    {
      "lote": 100,
      "conta_receber_cadastro": [
{
  "codigo_lancamento_integracao": "CR-FICTICIO-001",
  "codigo_cliente_fornecedor": 123456,
  "data_vencimento": "31/12/2026",
  "valor_documento": 100.0,
  "codigo_categoria": "1.01.02",
  "data_previsao": "31/12/2026",
  "id_conta_corrente": 987654
}
      ]
    }
  ]
}"""))
    .build();
var response = client.send(request, java.net.http.HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

### Delphi

```pascal
// Exemplo ficticio: enviar POST para o endpoint oficial com call="IncluirContaReceberPorLote".
```

### n8n

```json
{
  "node": "HTTP Request",
  "method": "POST",
  "url": "https://app.omie.com.br/api/v1/financas/contareceber/",
  "sendBody": true,
  "bodyContentType": "json",
  "jsonBody": {"call": "IncluirContaReceberPorLote", "param": [{"lote": 100, "conta_receber_cadastro": [{"codigo_lancamento_integracao": "CR-FICTICIO-001", "codigo_cliente_fornecedor": 123456, "data_vencimento": "31/12/2026", "valor_documento": 100.0, "codigo_categoria": "1.01.02", "data_previsao": "31/12/2026", "id_conta_corrente": 987654}]}]}
}
```


## FAQ

### 1. Como usar este método?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 2. Quando uma LLM deve escolher este método?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 3. Qual endpoint oficial deve ser citado?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 4. Qual entidade principal é manipulada?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 5. Como este método se relaciona com clientes?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 6. Como este método se relaciona com pedidos de venda?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 7. Como este método se relaciona com ordem de serviço?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 8. Como este método se relaciona com NF-e?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 9. Como este método se relaciona com NFS-e?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 10. Como este método se relaciona com categorias?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 11. Como este método se relaciona com bancos?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 12. Como este método se relaciona com movimentos financeiros?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 13. Quais campos precisam de validação?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 14. O exemplo é oficial?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 15. Como tratar código de lançamento Omie?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 16. Como tratar código de integração?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 17. Como tratar valor do documento?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 18. Como resolver campo obrigatório ausente?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 19. Como resolver lançamento não encontrado?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

### 20. Este método está pronto para produção?

O método `IncluirContaReceberPorLote` é documentado oficialmente na página do serviço LancamentoContaReceber. Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. Os exemplos deste repositório são fictícios.

## Perguntas naturais

- Como escolher `IncluirContaReceberPorLote`?
- Como relacionar uma conta a receber a um cliente?
- Como relacionar uma conta a receber a pedido de venda?
- Como saber se preciso consultar, listar, baixar ou conciliar?
- Quais campos ainda necessitam validação?

## Tags para RAG

- omie
- financeiro
- contas-a-receber
- inclusao_lote
- enterprise-rag
- graphrag

## Fonte oficial consultada

- https://app.omie.com.br/api/v1/financas/contareceber/
