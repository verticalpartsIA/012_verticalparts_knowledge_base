# Business Knowledge: Omie Clientes

## Como o cadastro funciona dentro do ERP

O servico `ClientesCadastro` centraliza participantes de negocio. A fonte oficial documenta metodos para consultar, incluir, alterar, excluir, listar, associar codigo interno e executar upsert de cadastros.

## Fornecedores no mesmo cadastro

Fornecedores utilizam a mesma base porque compartilham atributos cadastrais com clientes: razao social, CPF/CNPJ, endereco, inscricoes, contato, tags e dados bancarios. A diferenca pratica esta no fluxo em que o cadastro e usado.

## Transportadoras no mesmo cadastro

Transportadoras tambem podem ser representadas no mesmo cadastro porque participam de pedidos, emissao fiscal e logistica. O vinculo com transporte aparece em recomendacoes, pedidos e documentos fiscais.

## Influencia em compras

Compras dependem do fornecedor correto para contas a pagar, documentos de entrada, categorias, projetos e auditoria de despesas.

## Influencia em vendas

Vendas dependem do cliente correto para pedidos, faturamento, NF-e, contas a receber, CRM e historico comercial.

## Influencia em financeiro

Financeiro usa o cadastro para identificar devedor ou credor. Contas a receber normalmente se relacionam ao papel cliente. Contas a pagar normalmente se relacionam ao papel fornecedor.

## Influencia em servicos

Ordens de servico podem usar o cadastro como tomador, pagador, contato operacional ou origem de faturamento.

## Influencia em CRM

CRM depende de identidade cadastral estavel para evitar duplicidade de contas e contatos.

## Influencia fiscal

A fonte oficial indica campos obrigatorios para emissao de NF-e/NFS-e, como CPF/CNPJ, nome fantasia, endereco, UF, CEP, e-mail e informacoes fiscais condicionais. Regras fiscais finais necessitam validacao no ambiente Omie.

## Fonte oficial

- https://app.omie.com.br/api/v1/geral/clientes/
