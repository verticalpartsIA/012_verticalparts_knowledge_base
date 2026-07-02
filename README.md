# VerticalParts Knowledge Base

Este repositório organiza a base de conhecimento técnica da VerticalParts para uso por LLMs, agentes internos e pipelines de RAG. A primeira frente documentada é a API Omie, com foco em transformar conhecimento operacional, documentação técnica e exemplos de uso em documentos rastreáveis, versionados e prontos para indexação.

## Objetivos

- Centralizar documentação técnica validável para APIs, integrações e fluxos de negócio da VerticalParts.
- Criar uma fonte confiável para respostas assistidas por LLMs e sistemas RAG.
- Padronizar documentos com metadados úteis para busca semântica, chunking e auditoria.
- Separar conhecimento de produto, especificações, desenho técnico, prompts, exemplos, schemas, datasets e scripts.
- Evitar armazenamento de credenciais, tokens, senhas ou segredos no repositório.

## Estrutura Inicial

```text
.github/workflows/
docs/
docs/omie/
knowledge/
knowledge/omie/
specs/
sdd/
skills/
skills/omie-api-knowledge/
prompts/
rag/
schemas/
examples/
workflows/
datasets/
scripts/
tests/
```

## API Omie

A documentação inicial da Omie está em `docs/omie/` e está organizada por domínio funcional:

- `geral`: cadastros e entidades base.
- `financeiro`: contas a pagar, contas a receber e movimentos financeiros.
- `vendas`: pedidos de venda e fluxo comercial.
- `estoque`: materiais, produtos e movimentações de estoque.
- `servicos`: ordens de serviço e operações relacionadas.
- `fiscal`: documentos e obrigações fiscais.

Os documentos iniciais estão marcados como `status: inicial/a validar`, pois devem ser refinados com fontes oficiais, testes controlados e validação de especialistas internos.

## Configuração Local

Copie `.env.example` para `.env` apenas no ambiente local e preencha as variáveis fora do Git:

```env
OMIE_APP_KEY=
OMIE_APP_SECRET=
OMIE_BASE_URL=https://app.omie.com.br/api/v1
```

Nunca faça commit de chaves, segredos, tokens, senhas ou arquivos `.env` reais.

## Qualidade Esperada

Todo conteúdo deve ser técnico, objetivo, em português do Brasil e adequado para recuperação por RAG. Sempre que possível, cada documento deve informar domínio, endpoint, métodos conhecidos, quando usar, entidades relacionadas, perguntas prováveis de usuários e observações de indexação.
