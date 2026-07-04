---
title: "IncluirPedido"
service: "Pedidos de Venda"
domain: "omie.produtos"
resource: "Pedidos de Venda"
method: "IncluirPedido"
endpoint: "https://app.omie.com.br/api/v1/produtos/pedido/"
http_method: "POST"
version: "v1"
entity: "Pedidos de Venda"
related_entities: []
related_methods: []
permissions: "Necessita validacao"
complexity: "media"
status: "Documentado automaticamente/a validar"
source: "https://app.omie.com.br/api/v1/produtos/pedido/"
last_review: "2026-07-03"
tags:
  - omie
  - factory-mvp
  - incluirpedido
keywords:
  - "IncluirPedido"
questions: 5
use_cases: []
business_area: "Necessita validacao"
llm_ready: false
rag_ready: true
graph_ready: false
embedding_version: 1
---

# IncluirPedido

## Objetivo

Documento gerado automaticamente pela Omie Knowledge Factory a partir de parsing da documentacao oficial. Conteudo marcado como a validar quando o parser nao conseguiu confirmar o detalhe com seguranca.

## Quando utilizar

Use este metodo quando a operacao desejada corresponder ao metodo oficial `IncluirPedido` do servico `Pedidos de Venda`.

## Quando nao utilizar

Nao utilize este documento como fonte unica para regras de negocio que nao estejam explicitamente descritas na fonte oficial.

## Fluxo de negocio

Necessita validacao.

## Entidades relacionadas

- Pedidos de Venda

## Metodos relacionados

Necessita validacao.

## Pre-requisitos

- Possuir credenciais Omie validas fora deste repositorio.
- Nao registrar app_key, app_secret, tokens ou senhas em documentos.

## Payload ou conteudo tecnico principal

Endpoint: `https://app.omie.com.br/api/v1/produtos/pedido/`

Descricao extraida:

Inclui um pedido de venda de produto Parâmetros: Retorno pedido_venda_produto_response : Exemplo: Teste agora mesmo

## Campos obrigatorios

Necessita validacao.

## Campos opcionais

Necessita validacao.

## Regras de negocio

Necessita validacao contra a documentacao oficial e regras operacionais da VerticalParts.

## Validacoes

- Conferir campos obrigatorios antes da chamada.
- Conferir tipos informados pela documentacao oficial.

## Restricoes

- Exemplos sao ficticios.
- Credenciais foram omitidas por seguranca.

## Resposta esperada

Necessita validacao.

## Erros comuns

Necessita validacao.

## Como resolver os erros

- Validar payload contra a documentacao oficial.
- Conferir credenciais no ambiente seguro de execucao, sem registrar valores neste repositorio.

## Casos de uso

- Automatizar a operacao `IncluirPedido` no contexto do servico `Pedidos de Venda`.

## Exemplos completos

### Exemplo JSON ficticio de requisicao

```json
{
  "cabecalho": {
    "codigo_cliente": 3792227,
    "codigo_pedido_integracao": "1783199962",
    "data_previsao": "04/07/2026",
    "etapa": "10",
    "numero_pedido": "82548",
    "codigo_parcela": "999",
    "quantidade_itens": 2
  },
  "det": [
    {
      "ide": {
        "codigo_item_integracao": "4422421"
      },
      "inf_adic": {
        "peso_bruto": 150,
        "peso_liquido": 150
      },
      "produto": {
        "cfop": "5.102",
        "codigo_produto": "4422421",
        "descricao": "Telefone Celular X",
        "ncm": "9403.30.00",
        "quantidade": 1,
        "tipo_desconto": "V",
        "unidade": "UN",
        "valor_desconto": 0,
        "valor_unitario": 200
      }
    }
  ],
  "frete": {
    "modalidade": "9"
  },
  "informacoes_adicionais": {
    "codigo_categoria": "1.01.03",
    "codigo_conta_corrente": 11850365,
    "consumidor_final": "S",
    "enviar_email": "N"
  },
  "agropecuario": {
    "cNumReceita": "",
    "cCpfResponsavel": "",
    "nTipoGuia": 1,
    "cUFGuia": "",
    "cSerieGuia": "",
    "nNumGuia": 1
  },
  "lista_parcelas": {
    "parcela": [
      {
        "data_vencimento": "05/07/2026",
        "numero_parcela": 1,
        "percentual": 50,
        "valor": 100
      },
      {
        "data_vencimento": "12/09/2026",
        "numero_parcela": 2,
        "percentual": 50,
        "valor": 100
      }
    ]
  }
}
```

## FAQ

### Quando devo usar o metodo IncluirPedido?

Necessita validacao.
### Quais campos sao obrigatorios para IncluirPedido?

Necessita validacao.
### Qual endpoint devo chamar para IncluirPedido?

Necessita validacao.
### Que retorno esperar do metodo IncluirPedido?

Necessita validacao.
### Como IncluirPedido se relaciona com Pedidos de Venda?

Necessita validacao.

## Perguntas naturais

- Quando devo usar o metodo IncluirPedido?
- Quais campos sao obrigatorios para IncluirPedido?
- Qual endpoint devo chamar para IncluirPedido?
- Que retorno esperar do metodo IncluirPedido?
- Como IncluirPedido se relaciona com Pedidos de Venda?

## Tags para RAG

- omie
- factory-mvp
- incluirpedido
- enterprise-rag

## Fonte oficial consultada

https://app.omie.com.br/api/v1/produtos/pedido/
