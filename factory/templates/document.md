---
title: "{{ title }}"
service: "{{ service }}"
domain: "{{ domain }}"
resource: "{{ resource }}"
method: "{{ method }}"
endpoint: "{{ endpoint }}"
http_method: "POST"
version: "1"
entity: "{{ entity }}"
related_entities: []
related_methods: []
permissions:
  - "Não armazenar credenciais"
complexity: "{{ complexity }}"
status: "{{ status }}"
source: "{{ source }}"
last_review: "{{ last_review }}"
tags: []
keywords: []
questions: []
use_cases: []
business_area: "{{ business_area }}"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
# {{ method }}

## Objetivo

{{ objective }}

## Quando utilizar

{{ when_to_use }}

## Quando NÃO utilizar

{{ when_not_to_use }}

## Fluxo de negócio

{{ business_flow }}

## Fonte oficial consultada

- {{ source }}

