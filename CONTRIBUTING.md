# Contribuindo

Este repositório deve preservar qualidade documental, rastreabilidade e segurança. Antes de contribuir, confirme que a alteração não inclui credenciais reais, dados sensíveis, tokens, senhas, chaves de API ou informações pessoais desnecessárias.

## Padrão de Conteúdo

- Escreva em português do Brasil.
- Use tom técnico, profissional e direto.
- Prefira documentos pequenos, coesos e com título claro.
- Inclua metadados úteis para RAG quando o documento descrever APIs.
- Marque explicitamente conteúdos ainda não validados.
- Cite a fonte quando o conteúdo vier de documentação oficial, teste interno ou decisão de arquitetura.

## Revisão

Antes de abrir pull request:

- Verifique se nenhum arquivo `.env` real foi incluído.
- Confirme que novos documentos seguem o padrão definido em `specs/omie_api_knowledge_base_spec.md`.
- Revise links, nomes de endpoints e status de validação.
- Evite alterar estrutura existente sem justificativa.

## Segurança

Este repositório não deve armazenar `app_key`, `app_secret`, tokens, senhas, certificados privados ou dumps de produção. Use `.env.example` apenas com variáveis vazias ou valores fictícios.
