# SDD: Desenho Técnico da Base Omie para RAG/LLM

## Visão Geral

A solução proposta transforma documentação e conhecimento operacional da API Omie em uma base versionada, rastreável e indexável. O resultado esperado é um conjunto de documentos em Markdown, enriquecidos com metadados, que pode alimentar pipelines de RAG e agentes LLM da VerticalParts.

## Componentes

- Repositório Git: fonte versionada da verdade documental.
- Crawler: coleta documentação pública e fontes autorizadas.
- Normalizador: converte conteúdo bruto em Markdown padronizado.
- Validador: checa campos obrigatórios, ausência de segredos e status documental.
- Indexador: divide documentos em chunks e gera metadados.
- Banco vetorial: armazena embeddings em Qdrant ou pgvector.
- Camada LLM: consulta a base recuperada e responde com base nas fontes.

## Crawler

O crawler deve:

- Usar `OMIE_BASE_URL` como referência de base quando aplicável.
- Nunca registrar `OMIE_APP_KEY` ou `OMIE_APP_SECRET` em logs.
- Coletar apenas fontes autorizadas.
- Salvar saídas brutas em área ignorada pelo Git quando houver risco de dados sensíveis.
- Gerar documentos intermediários revisáveis antes da publicação em `docs/`.

## Indexação

O processo de indexação deve ler Markdown versionado e gerar registros com:

- Caminho do arquivo.
- Título.
- Domínio.
- Endpoint.
- Status.
- Entidades relacionadas.
- Hash do conteúdo.
- Data de indexação.
- Versão do modelo de embedding.

## Chunking

Recomendações iniciais:

- Preservar cabeçalhos como contexto.
- Evitar chunks que misturem domínios diferentes.
- Priorizar blocos entre 400 e 900 tokens.
- Repetir metadados principais em cada chunk.
- Separar exemplos de perguntas em chunks próprios quando forem numerosos.

## Metadados

Metadados mínimos:

```json
{
  "source_path": "docs/omie/financeiro/contas_a_pagar.md",
  "domain": "omie.financeiro",
  "endpoint": "/financas/contapagar/",
  "status": "inicial/a validar",
  "doc_type": "api_reference"
}
```

## Embeddings

O pipeline deve usar um modelo de embedding compatível com português do Brasil e documentação técnica. A versão do modelo deve ser registrada para permitir reindexação controlada.

## Qdrant e pgvector

A base deve suportar duas opções:

- Qdrant: recomendado para serviço vetorial dedicado, filtros por metadados e coleções independentes.
- pgvector: recomendado quando a VerticalParts desejar manter busca vetorial junto a dados relacionais em PostgreSQL.

O desenho inicial deve manter uma camada de abstração para troca do backend vetorial sem reescrever documentos.

## Integração com LLMs

O agente LLM deve:

- Consultar primeiro a base indexada.
- Responder apenas com informações presentes nos documentos recuperados.
- Informar quando o conteúdo estiver `inicial/a validar`.
- Não inventar endpoints, métodos, campos ou credenciais.
- Solicitar validação humana quando houver lacuna documental.

## Segurança

- Credenciais ficam fora do Git.
- `.env.example` deve conter apenas variáveis vazias ou fictícias.
- Logs não devem expor payloads sensíveis.
- Dados reais de clientes devem ser removidos ou anonimizados.
