# Estratégia de Indexação RAG para API Omie

## Objetivo

Definir uma estratégia inicial para transformar a documentação Omie em chunks pesquisáveis por LLMs e agentes internos da VerticalParts.

## Entrada

Arquivos Markdown em:

- `docs/omie/`
- `knowledge/omie/`
- `specs/`
- `sdd/`

## Normalização

Cada documento deve ser lido com preservação de:

- Caminho do arquivo.
- Título principal.
- Cabeçalhos.
- Domínio.
- Endpoint.
- Métodos conhecidos.
- Status.

## Chunking

Regras iniciais:

- Criar chunks por seção.
- Anexar título, domínio e endpoint a cada chunk.
- Manter exemplos de perguntas próximos ao documento de origem.
- Evitar chunks com mais de um endpoint principal.
- Registrar hash do chunk para detectar mudanças.

## Metadados

Campos recomendados:

- `source_path`
- `title`
- `domain`
- `endpoint`
- `methods`
- `status`
- `doc_type`
- `chunk_hash`
- `indexed_at`

## Recuperação

A recuperação deve combinar:

- Busca vetorial por similaridade semântica.
- Filtros por domínio.
- Filtros por status.
- Reforço lexical para nomes de endpoints e entidades.

## Bancos Vetoriais

Qdrant e pgvector são opções suportadas no desenho inicial. A escolha deve considerar operação, custo, integração com a stack existente e necessidade de filtros por metadados.

## Critérios de Qualidade

- Respostas devem citar os documentos recuperados.
- Conteúdo `inicial/a validar` deve ser apresentado com ressalva.
- Perguntas sem cobertura documental devem retornar lacuna explícita.
- A base deve ser reindexada quando arquivos fonte mudarem.
