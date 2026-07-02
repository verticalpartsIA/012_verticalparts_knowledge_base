# Ordem de Serviço

## Título

Ordem de serviço

## Domínio

Omie Serviços

## Endpoint

`/servicos/os/`

## Métodos conhecidos

- `ListarOS`
- `ConsultarOS`
- `IncluirOS`
- `AlterarOS`
- `ExcluirOS`

## Quando usar

Use este endpoint para registrar, consultar e manter ordens de serviço, incluindo serviços prestados, clientes, valores e possíveis integrações financeiras ou fiscais.

## Entidades relacionadas

- Cliente
- Serviço
- Conta a receber
- Nota fiscal de serviço
- Categoria financeira
- Projeto

## Exemplos de perguntas que um usuário faria

- Como consultar uma ordem de serviço no Omie?
- Qual endpoint cria uma OS?
- Como relacionar serviço e cliente em uma ordem?
- Ordem de serviço pode gerar conta a receber?

## Observações para RAG

Este documento deve ser priorizado para perguntas sobre OS, serviço, prestação, faturamento de serviço e vínculo com cliente. O agente deve evitar afirmar automações financeiras ou fiscais sem validação.

## Status

inicial/a validar
