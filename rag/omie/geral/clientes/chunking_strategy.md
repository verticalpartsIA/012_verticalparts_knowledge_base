# Estratégia de Chunking: Omie Geral Clientes

## Objetivo

Preparar os documentos de `docs/omie/geral/clientes/` para indexação RAG com preservação de contexto técnico, método oficial, endpoint, status e tipo de operação.

## Unidade principal de chunk

A unidade principal deve ser o arquivo de método. Cada arquivo descreve um método oficial do serviço `ClientesCadastro`.

## Metadados obrigatórios por chunk

- `source_path`
- `service`
- `method`
- `endpoint`
- `domain`
- `entity`
- `operation`
- `status`
- `source`
- `rag_tags`

## Divisão recomendada

1. Chunk de identidade do método: YAML, título, nome oficial, endpoint, domínio e entidade.
2. Chunk de decisão de uso: quando usar, quando não usar e entidades relacionadas.
3. Chunk de contrato de entrada: payload de entrada, campos obrigatórios e campos opcionais.
4. Chunk de contrato de saída: payload de retorno e exemplos JSON.
5. Chunk operacional: erros comuns, observações importantes e perguntas de usuário.

## Regras para LLM

- Responder perguntas sobre payload priorizando chunks de contrato de entrada e saída.
- Responder perguntas de escolha de método priorizando README do serviço e chunks de decisão de uso.
- Sempre preservar `status`, principalmente em métodos `deprecated/oficial`.
- Não inferir obrigatoriedade de campos além do que está documentado; quando houver dúvida, indicar validação contra fonte oficial.

## Tamanho sugerido

- 350 a 900 tokens por chunk.
- Evitar misturar métodos diferentes no mesmo chunk.
- Incluir `method` e `endpoint` no texto expandido de cada chunk.

## Fonte

Documentos em `docs/omie/geral/clientes/`, derivados da fonte oficial:

https://app.omie.com.br/api/v1/geral/clientes/
