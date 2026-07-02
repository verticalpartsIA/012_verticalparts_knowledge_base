# Omie Geral: Clientes, Fornecedores e Transportadoras

## O que representa este serviço

O serviço `ClientesCadastro` representa o cadastro central de participantes comerciais no Omie. Ele é usado para manter dados cadastrais de clientes, fornecedores, transportadoras e outros agentes que participam de fluxos financeiros, comerciais, fiscais, logísticos e de serviços.

## Por que clientes, fornecedores e transportadoras usam o mesmo cadastro

Na Omie, o cadastro concentra dados de identificação, endereço, contato, inscrições fiscais, tags, recomendações e vínculos operacionais em uma mesma entidade base de cliente/fornecedor. Essa modelagem evita duplicidade quando a mesma pessoa física ou jurídica atua em mais de um papel, por exemplo como cliente em vendas e fornecedor em compras.

## Endpoint oficial

`https://app.omie.com.br/api/v1/geral/clientes/`

## Métodos existentes

| Método | Uso principal | Status documental |
| --- | --- | --- |
| `AlterarCliente` | Alterar um cadastro existente. | oficial/a validar em integração |
| `AssociarCodIntCliente` | Associar código interno a um cadastro Omie. | oficial/a validar em integração |
| `ConsultarCliente` | Consultar um cadastro por chave. | oficial/a validar em integração |
| `ExcluirCliente` | Excluir um cadastro da base. | oficial/a validar em integração |
| `IncluirCliente` | Criar um novo cadastro. | oficial/a validar em integração |
| `IncluirClientesPorLote` | Incluir lote de cadastros. | deprecated/oficial |
| `ListarClientes` | Listar cadastros com retorno completo. | oficial/a validar em integração |
| `ListarClientesResumido` | Pesquisar/listar cadastros em formato resumido. | oficial/a validar em integração |
| `UpsertCliente` | Criar ou atualizar cadastro por chave de integração. | oficial/a validar em integração |
| `UpsertClienteCpfCnpj` | Criar ou atualizar cadastro por CPF/CNPJ. | oficial/a validar em integração |
| `UpsertClientesPorLote` | Criar ou atualizar lote de cadastros. | deprecated/oficial |

## Relação com outros domínios

- Financeiro: contas a pagar e contas a receber dependem do cadastro correto de cliente/fornecedor.
- Vendas: pedidos de venda usam o cadastro para identificar comprador, endereço, contato e dados fiscais.
- Compras: fornecedores usam a mesma base para obrigações, documentos e histórico operacional.
- NF-e e NFS-e: emissão fiscal exige dados como CPF/CNPJ, razão social, endereço, cidade, estado, CEP, e-mail e informações fiscais.
- Serviços: ordens de serviço podem usar o cadastro como tomador, pagador ou contato operacional.

## Como uma LLM deve escolher o método correto

- Para buscar um cadastro específico, use `ConsultarCliente`.
- Para criar um cadastro novo, use `IncluirCliente`.
- Para alterar cadastro existente, use `AlterarCliente`.
- Para criar ou atualizar sem decidir previamente se existe, avalie `UpsertCliente` ou `UpsertClienteCpfCnpj`.
- Para páginas de resultados ou sincronização, use `ListarClientes` ou `ListarClientesResumido`.
- Para associação de código interno legado, use `AssociarCodIntCliente`.
- Para exclusão, use `ExcluirCliente` com cuidado operacional.
- Evite métodos por lote quando a fonte oficial indicar `DEPRECATED`, salvo se houver decisão técnica validada.

## Fonte oficial consultada

- https://app.omie.com.br/api/v1/geral/clientes/
