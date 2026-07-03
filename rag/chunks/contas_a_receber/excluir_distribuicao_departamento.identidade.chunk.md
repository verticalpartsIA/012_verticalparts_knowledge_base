---
source_path: "docs/omie/financeiro/contas_a_receber/excluir_distribuicao_departamento.md"
chunk_id: "ExcluirDistribuicaoDepartamento.identidade"
service: "LancamentoContaReceber"
method: "ExcluirDistribuicaoDepartamento"
endpoint: "https://app.omie.com.br/api/v1/financas/contareceber/"
focus: "identidade"
status: "Documentado oficialmente / Necessita validação em integração"
embedding_version: 1
---

# Chunk ExcluirDistribuicaoDepartamento - identidade

Este chunk descreve o método `ExcluirDistribuicaoDepartamento` do serviço `LancamentoContaReceber` para recuperação RAG. Entrada oficial: `conta_receber_cadastro_chave`. Retorno oficial: `conta_receber_cadastro_response`. Operação: `exclusao_rateio_departamento`.

Contas a receber conectam cliente, pedido de venda, ordem de serviço, NF-e, NFS-e, categorias, bancos e movimentos financeiros. A LLM deve usar esse contexto para separar título financeiro, baixa, conciliação e movimento efetivado. Quando a pergunta mencionar vencimento, valor, categoria, conta corrente, pedido, ordem de serviço ou nota fiscal, este chunk pode ser recuperado junto do documento de método.

Critério de resposta: declarar que o método é documentado oficialmente na fonte Omie e marcar comportamento operacional, obrigatoriedade condicional e regras fiscais como "Necessita validação" quando não houver contrato específico validado. Exemplos são fictícios e não incluem credenciais.

Estratégia híbrida: usar busca lexical por `ExcluirDistribuicaoDepartamento`, `conta_receber_cadastro_chave`, código de lançamento, código de integração, baixa, conciliação, categoria e banco; combinar com busca vetorial por intenção de negócio. Reranking deve priorizar método exato, entidade conta a receber, status documentado oficialmente e compatibilidade com a operação solicitada.

GraphRAG: expandir vizinhos Cliente, Pedido de Venda, Ordem de Serviço, NF-e, NFS-e, Categorias, Bancos e Movimentos Financeiros. Para perguntas de baixa e conciliação, expandir também para recebimento, conta corrente e movimento financeiro.

Validações importantes: confirmar cliente, categoria, conta corrente, data de vencimento, valor do documento, estado de baixa e estado de conciliação. Não recomendar exclusão, alteração, cancelamento ou baixa sem checar o estado atual do título.

Contexto de negócio adicional: contas a receber são registros financeiros que normalmente representam expectativa de entrada de caixa. Uma pergunta pode chegar com vocabulário de cobrança, parcela, boleto, título, recebível, faturamento, nota, cliente, baixa ou conciliação. A recuperação deve manter todos esses termos próximos do método para reduzir risco de resposta fora do domínio. Quando o usuário mencionar pedido de venda ou ordem de serviço, a LLM deve explicar que o título pode ter vínculo operacional, mas o vínculo exato precisa ser validado no payload e no ambiente Omie. Quando o usuário mencionar NF-e ou NFS-e, a resposta deve separar documento fiscal de título financeiro. Quando mencionar banco, conta corrente ou conciliação, a resposta deve priorizar métodos de baixa, conciliação ou consulta de estado. Quando mencionar categoria, a resposta deve orientar classificação financeira e rateio como pontos de validação. Esse contexto melhora embeddings, reranking e GraphRAG sem substituir a fonte oficial.
