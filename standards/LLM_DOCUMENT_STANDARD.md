# LLM Document Standard

## Objetivo

Este padrao define como todos os arquivos Markdown do repositorio devem ser escritos para uso por LLMs, RAG, GraphRAG, embeddings e avaliacao automatizada.

## Estrutura obrigatoria

1. YAML front matter.
2. Titulo H1 unico.
3. Objetivo.
4. Quando utilizar.
5. Quando nao utilizar.
6. Fluxo de negocio.
7. Entidades relacionadas.
8. Metodos relacionados.
9. Pre-requisitos.
10. Payload ou conteudo tecnico principal.
11. Campos obrigatorios.
12. Campos opcionais.
13. Regras de negocio.
14. Validacoes.
15. Restricoes.
16. Resposta esperada.
17. Erros comuns.
18. Como resolver os erros.
19. Casos de uso.
20. Exemplos completos.
21. FAQ.
22. Perguntas naturais.
23. Tags para RAG.
24. Fonte oficial consultada.

## Metadados YAML

Todo Markdown em `docs/omie` deve iniciar com os campos abaixo:

```yaml
---
title:
service:
domain:
resource:
method:
endpoint:
http_method:
version:
entity:
related_entities:
related_methods:
permissions:
complexity:
status:
source:
last_review:
tags:
keywords:
questions:
use_cases:
business_area:
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
```

## Padrao de titulos

Use um unico H1 por documento. Use H2 para secoes obrigatorias. H3 deve ser usado apenas para exemplos, FAQ ou subsecoes tecnicas.

## Padrao de exemplos

Exemplos devem ser ficticios, identificados como ficticios e nao devem registrar credenciais, segredos ou senhas. Quando a autenticacao for necessaria, declarar que foi omitida por seguranca.

## Padrao de JSON

JSON deve ser valido, indentado com dois espacos e limitado ao necessario para demonstrar a estrutura. Campos nao confirmados devem ser marcados como "Necessita validacao".

## Padrao de perguntas naturais

Cada documento de metodo deve conter perguntas que reflitam linguagem real de usuarios, incluindo variacoes sobre cliente, fornecedor, transportadora, codigo interno, codigo Omie, CPF, CNPJ e finalidade operacional.

## Padrao de FAQ

Cada metodo deve ter pelo menos 20 perguntas e respostas. Respostas devem ser curtas, verificaveis e baseadas na fonte ou marcadas como pendencia.

## Padrao de relacionamentos

Relacionamentos devem mencionar entidades de negocio e metodos relacionados. Relacionamentos graficos devem ser espelhados em `graphs/`.

## Padrao de tags

Tags devem incluir dominio, recurso, operacao, entidade e finalidade RAG. Exemplo: `omie`, `clientes`, `fornecedores`, `listagem`, `enterprise-rag`.

## Padrao de casos de uso

Casos de uso devem indicar tarefa, contexto, entrada esperada, metodo recomendado e criterio de sucesso.

## Padrao de chunking

Chunks devem ter metadados completos, preferencialmente entre 500 e 900 tokens, sem misturar metodos diferentes. A unidade minima recomendada e metodo + secao.

## Padrao para embeddings

Registrar `embedding_version`. Ao trocar modelo, reindexar e atualizar estrategia. Preservar idioma portugues do Brasil e termos tecnicos originais.

## Padrao para RAG

RAG deve combinar busca vetorial, busca lexical, filtros por metadados e citacao de fontes. Respostas devem indicar "Documentado oficialmente" ou "Necessita validacao".

## Padrao para GraphRAG

GraphRAG deve mapear entidades, metodos, dominios e documentos. Mermaid pode representar a topologia em Markdown.

## Padrao de nomenclatura

Arquivos devem usar `snake_case`. Metodos oficiais devem preservar capitalizacao original da Omie dentro do conteudo.

## Padrao para links internos

Use caminhos relativos ao repositorio quando apontar para documentos internos. Nao usar links quebrados.

## Padrao para referencias oficiais

Toda informacao oficial deve citar a URL consultada. Toda informacao nao explicitamente confirmada deve ser marcada como "Necessita validacao".

## Padrao para versionamento

Mudancas relevantes devem passar por branch, commit e pull request. Atualize `last_review` quando revisar conteudo contra fonte oficial.
