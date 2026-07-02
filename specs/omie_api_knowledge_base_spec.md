# SPEC: Base de Conhecimento da API Omie

## Objetivo

Definir a estrutura, o padrão documental e os critérios de qualidade para uma base de conhecimento RAG/LLM da VerticalParts dedicada inicialmente à API Omie.

## Escopo

Inclui:

- Organização de documentos por domínio funcional da API Omie.
- Padronização de metadados para recuperação semântica.
- Critérios para validação, versionamento e revisão documental.
- Diretrizes para uso seguro por agentes LLM.

Não inclui:

- Armazenamento de credenciais reais.
- Execução direta de chamadas de produção.
- Substituição da documentação oficial da Omie.
- Definição final de todos os endpoints da API.

## Arquitetura Documental

A base é organizada em camadas:

- `docs/`: documentação técnica e funcional em linguagem humana.
- `knowledge/`: conhecimento curado e consolidado.
- `specs/`: especificações de escopo e qualidade.
- `sdd/`: desenho técnico da solução.
- `skills/`: instruções para agentes LLM.
- `rag/`: estratégia de indexação e recuperação.
- `schemas/`: modelos estruturais para validação futura.
- `examples/`: exemplos de payloads, consultas e respostas.
- `workflows/`: fluxos operacionais e automações.
- `datasets/`: dados preparados para testes e avaliação.
- `scripts/`: coleta, validação e preparação de documentos.
- `tests/`: testes automatizados e validações documentais.

## Fontes

As fontes aceitas são:

- Documentação oficial da Omie.
- Testes controlados em ambiente autorizado.
- Conhecimento interno validado da VerticalParts.
- Evidências de integrações existentes, desde que sem segredos ou dados sensíveis.

Toda informação que ainda não foi validada deve ser marcada como `inicial/a validar`.

## Padrão de Documentos de API

Documentos de endpoints ou grupos de endpoints devem conter:

- Título.
- Domínio.
- Endpoint.
- Métodos conhecidos.
- Quando usar.
- Entidades relacionadas.
- Exemplos de perguntas que um usuário faria.
- Observações para RAG.
- Status.

## Critérios de Qualidade

- Clareza técnica em português do Brasil.
- Ausência de credenciais, tokens, senhas ou dados sensíveis.
- Metadados consistentes para indexação.
- Status de validação explícito.
- Escopo bem definido por documento.
- Conteúdo fácil de dividir em chunks sem perda de contexto.
- Histórico versionado via Git e revisão por pull request.

## Critérios de Aceite Inicial

- Estrutura de diretórios criada.
- README principal descrevendo o propósito RAG/LLM.
- SPEC, SDD e skill inicial incluídos.
- Documentos Omie iniciais por domínio.
- `.env.example` com variáveis fictícias e sem segredos.
