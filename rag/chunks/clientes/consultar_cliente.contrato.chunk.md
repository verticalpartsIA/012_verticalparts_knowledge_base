---
source_path: "docs/omie/geral/clientes/consultar_cliente.md"
chunk_id: "ConsultarCliente.contrato"
service: "ClientesCadastro"
method: "ConsultarCliente"
endpoint: "https://app.omie.com.br/api/v1/geral/clientes/"
focus: "payload, campos obrigatorios, campos opcionais e retorno"
status: "Documentado oficialmente / Necessita validacao em integracao"
embedding_version: 1
---

# Chunk ConsultarCliente - contrato

Este chunk concentra payload, campos obrigatorios, campos opcionais e retorno para o metodo `ConsultarCliente` do servico `ClientesCadastro`.

Metodo oficial: `ConsultarCliente`.
Endpoint oficial: `https://app.omie.com.br/api/v1/geral/clientes/`.
Entrada oficial: `clientes_cadastro_chave`.
Retorno oficial: `clientes_cadastro`.
Status: Documentado oficialmente / Necessita validacao em integracao.

Uso recomendado: recuperar um cliente, fornecedor ou transportadora especifico antes de leitura, auditoria, alteracao ou decisao de integracao.

Nao usar para: listar muitos cadastros ou sincronizar paginas de registros.

Relacionamentos de negocio: cliente, fornecedor, transportadora, pedido, NF-e, conta a receber, conta a pagar, CRM, projeto, servico, produtos, categorias e anexos.

Regra para LLM: responder apenas com base no documento fonte, declarar exemplos como ficticios e indicar "Necessita validacao" quando o comportamento depender de credenciais, ambiente, regra fiscal ou campos condicionais.

Contexto expandido para recuperacao: o servico `ClientesCadastro` e o ponto central de cadastro de participantes no Omie. A mesma base pode representar cliente, fornecedor ou transportadora, e a interpretacao correta depende do fluxo de negocio. Em vendas, o cadastro se conecta a pedido, faturamento, conta a receber, CRM e emissao fiscal. Em compras, o mesmo cadastro pode atuar como fornecedor e alimentar conta a pagar, categorias, projetos e documentos de entrada. Em logistica, a transportadora pode aparecer vinculada a pedidos, entrega e NF-e. Em servicos, o cadastro pode representar tomador, pagador ou contato operacional. Portanto, a recuperacao nao deve olhar apenas para o nome do metodo; deve considerar intencao, entidade, operacao, chave de busca e status documental.

Criterios de escolha: quando o usuario quer localizar um registro especifico, priorizar metodos de consulta por chave. Quando deseja criar, priorizar inclusao ou upsert conforme a idempotencia esperada. Quando deseja mudar dados, priorizar alteracao. Quando deseja percorrer a base, priorizar listagem paginada. Quando o metodo estiver marcado como DEPRECATED, a resposta deve avisar antes de sugerir qualquer uso. Quando o usuario perguntar por CPF, CNPJ, codigo interno ou codigo Omie, a LLM deve diferenciar chave documentada oficialmente de comportamento que necessita validacao.

Campos e validacoes: `razao_social` e documentado oficialmente como obrigatorio no cadastro. A fonte oficial tambem sinaliza campos condicionais para NF-e/NFS-e, como CPF/CNPJ, nome fantasia, endereco, estado, CEP, e-mail e informacoes fiscais. Esses campos nao devem ser tratados como universalmente obrigatorios para todos os cenarios sem confirmar o uso pretendido. Exemplos de payload sao ficticios, incompletos por seguranca e nao representam contrato oficial integral. A autenticacao foi omitida de proposito.

Estrategia RAG: indexar este chunk com filtros por `service`, `method`, `operation`, `status`, `entity` e `embedding_version`. Para reranking, priorizar match exato do metodo, presenca de endpoint oficial, compatibilidade com a intencao do usuario e status nao depreciado. Para GraphRAG, expandir vizinhos como Cliente, Fornecedor, Transportadora, Pedido, NF-e, Conta a Receber, Conta a Pagar, CRM, Projeto, Servico, Produtos, Categorias e Anexos.
