# Índice: Clientes, Fornecedores e Transportadoras

## Visão Geral

Este documento é o índice resumido do serviço Omie `ClientesCadastro`, localizado no domínio `Geral > Clientes, Fornecedores e Transportadoras`.

A documentação detalhada por método está em:

- `docs/omie/geral/clientes/`

## Domínio

Omie Geral

## Endpoint

`/geral/clientes/`

## Métodos conhecidos

- `AlterarCliente`
- `AssociarCodIntCliente`
- `ConsultarCliente`
- `ExcluirCliente`
- `IncluirCliente`
- `IncluirClientesPorLote` - depreciado na fonte oficial
- `ListarClientes`
- `ListarClientesResumido`
- `UpsertCliente`
- `UpsertClienteCpfCnpj`
- `UpsertClientesPorLote` - depreciado na fonte oficial

## Quando usar

Use este grupo de endpoints para consultar, cadastrar e manter entidades cadastrais usadas em operações comerciais, financeiras, logísticas e fiscais. A mesma base cadastral pode representar clientes, fornecedores, transportadoras ou outros participantes relacionados ao fluxo da empresa.

## Documentos Detalhados

- `docs/omie/geral/clientes/alterar_cliente.md`
- `docs/omie/geral/clientes/associar_cod_int_cliente.md`
- `docs/omie/geral/clientes/consultar_cliente.md`
- `docs/omie/geral/clientes/excluir_cliente.md`
- `docs/omie/geral/clientes/incluir_cliente.md`
- `docs/omie/geral/clientes/incluir_clientes_por_lote.md`
- `docs/omie/geral/clientes/listar_clientes.md`
- `docs/omie/geral/clientes/listar_clientes_resumido.md`
- `docs/omie/geral/clientes/upsert_cliente.md`
- `docs/omie/geral/clientes/upsert_cliente_cpf_cnpj.md`
- `docs/omie/geral/clientes/upsert_clientes_por_lote.md`

## Entidades relacionadas

- Cliente
- Fornecedor
- Transportadora
- Pedido de venda
- Conta a pagar
- Conta a receber
- Documento fiscal

## Exemplos de perguntas que um usuário faria

- Como consultar um cliente pelo código no Omie?
- Qual endpoint uso para cadastrar um fornecedor?
- Transportadora usa o mesmo cadastro de clientes e fornecedores?
- Quais dados cadastrais preciso validar antes de emitir um pedido?

## Observações para RAG

Este índice deve ser recuperado quando a pergunta pedir uma visão geral do cadastro de clientes, fornecedores e transportadoras. Para perguntas sobre método específico, payload, retorno ou erro, a LLM deve preferir os documentos detalhados em `docs/omie/geral/clientes/`.

## Status

inicial/expandido com fonte oficial
