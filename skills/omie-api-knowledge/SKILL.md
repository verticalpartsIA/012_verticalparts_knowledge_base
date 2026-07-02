# Skill: Omie API Knowledge

## Objetivo

Orientar um agente LLM a responder dúvidas sobre APIs da Omie usando somente a base de conhecimento versionada da VerticalParts.

## Quando Usar

Use esta skill quando a pergunta envolver:

- Endpoints da API Omie.
- Integrações com clientes, fornecedores, transportadoras, financeiro, vendas, serviços, estoque ou fiscal.
- Estratégias de consulta, criação, atualização ou conciliação de dados via Omie.
- Explicação de documentos em `docs/omie/`.

## Fontes Permitidas

O agente deve usar apenas:

- Documentos em `docs/omie/`.
- Conhecimento curado em `knowledge/omie/`.
- Especificações em `specs/`.
- Desenhos técnicos em `sdd/`.
- Estratégias de RAG em `rag/`.

Se a resposta exigir informação ausente nessas fontes, o agente deve declarar a lacuna e recomendar validação contra documentação oficial ou especialista interno.

## Restrições

- Não invente endpoints, métodos, campos, payloads ou regras de negócio.
- Não gere, solicite ou exponha `app_key`, `app_secret`, tokens, senhas ou credenciais.
- Não responda com base em memória externa quando a base local não trouxer evidência.
- Indique quando o documento recuperado estiver com status `inicial/a validar`.
- Diferencie informação validada de hipótese ou pendência.

## Procedimento de Resposta

1. Identifique o domínio da pergunta.
2. Recupere documentos relevantes na base Omie.
3. Verifique endpoint, métodos conhecidos, entidades relacionadas e status.
4. Responda de forma objetiva, citando os caminhos dos documentos usados.
5. Se houver lacunas, liste o que precisa ser validado.

## Formato Recomendado

```text
Resposta:
[explicação objetiva]

Fonte(s):
- docs/omie/...

Status:
- inicial/a validar

Pendências:
- [quando houver]
```
