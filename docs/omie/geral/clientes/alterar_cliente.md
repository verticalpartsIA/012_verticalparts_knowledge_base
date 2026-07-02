---
title: "AlterarCliente - Omie Geral Clientes"
service: "ClientesCadastro"
domain: "omie.geral"
resource: "clientes"
method: "AlterarCliente"
endpoint: "https://app.omie.com.br/api/v1/geral/clientes/"
http_method: "POST"
version: "1"
entity: "cliente_fornecedor_transportadora"
related_entities:
  - Cliente
  - Fornecedor
  - Transportadora
  - Pedido
  - NF-e
  - Conta a Receber
  - Conta a Pagar
  - CRM
  - Projeto
  - Serviço
  - Produtos
  - Categorias
  - Anexos
related_methods:
  - ConsultarCliente
  - IncluirCliente
  - UpsertCliente
  - AssociarCodIntCliente
permissions:
  - "Necessita credenciais Omie validas fora do repositorio"
  - "Nao documentar chaves, segredos ou senhas"
complexity: "media"
status: "Documentado oficialmente / Necessita validacao em integracao"
source: "https://app.omie.com.br/api/v1/geral/clientes/"
last_review: "2026-07-02"
tags:
  - omie
  - clientes
  - fornecedores
  - transportadoras
  - alteracao
  - enterprise-rag
keywords:
  - "ClientesCadastro"
  - "AlterarCliente"
  - "cadastro Omie"
  - "RAG"
  - "LLM"
questions:
  - "Como usar AlterarCliente?"
  - "Como escolher o metodo correto para clientes?"
  - "Quais campos precisam ser validados?"
use_cases:
  - integracao_erp
  - sincronizacao_cadastral
  - assistente_llm
  - rag_operacional
business_area: "ERP / Cadastros / Geral"
llm_ready: true
rag_ready: true
graph_ready: true
embedding_version: 1
---
        # AlterarCliente

        ## Objetivo

        Altera dados de um cliente, fornecedor ou transportadora ja cadastrado. Este documento foi estruturado para LLMs, RAG e GraphRAG, nao como tutorial humano isolado.

        ## Quando utilizar

        Utilize `AlterarCliente` para atualizar dados cadastrais existentes, como razao social, nome fantasia, contato, endereco, tags, recomendacoes e dados fiscais.

        ## Quando NÃO utilizar

        Nao utilize `AlterarCliente` para criar novos cadastros, excluir registros ou associar apenas codigo interno. Quando houver duvida, a LLM deve responder que a decisao necessita validacao.

        ## Fluxo de negócio

        1. A integracao identifica a necessidade cadastral.
        2. A LLM seleciona o metodo com base na intencao: consulta, inclusao, alteracao, exclusao, listagem, associacao ou upsert.
        3. O payload e montado com dados ficticios em exemplos ou com dados autorizados em ambiente real.
        4. O retorno deve ser interpretado por `codigo_status` e `descricao_status` quando o tipo de retorno for status.
        5. A resposta deve citar a fonte oficial e indicar se ha pontos que necessitam validacao.

        ## Entidades relacionadas

        - Cliente
        - Fornecedor
        - Transportadora
        - Pedido
        - NF-e
        - Conta a Receber
        - Conta a Pagar
        - CRM
        - Projeto
        - Serviço
        - Produtos
        - Categorias
        - Anexos

        ## Métodos relacionados

        - `ConsultarCliente`
- `IncluirCliente`
- `UpsertCliente`
- `AssociarCodIntCliente`

        ## Pré-requisitos

        - Acesso autorizado ao ambiente Omie.
        - Credenciais mantidas fora do repositorio.
        - Decisao clara sobre chave de identificacao: codigo Omie, codigo de integracao ou CPF/CNPJ.
        - Validacao de campos obrigatorios conforme finalidade: cadastro simples, fiscal, vendas, compras ou financeiro.

        ## Payload

        - Tipo oficial de entrada: `clientes_cadastro`.
        - Tipo oficial de retorno: `clientes_status`.
        - Metodo documentado oficialmente: `AlterarCliente`.
        - Endpoint oficial: `https://app.omie.com.br/api/v1/geral/clientes/`.

        ## Campos obrigatórios

        - razao_social: Documentado oficialmente como preenchimento obrigatorio.
- cnpj_cpf: Necessario para emissao de NF-e/NFS-e.
- nome_fantasia: Necessario para emissao de NF-e/NFS-e.

        ## Campos opcionais

        - `codigo_cliente_omie`
- `codigo_cliente_integracao`
- `email`
- `telefone1_ddd`
- `telefone1_numero`
- `endereco`
- `endereco_numero`
- `bairro`
- `cidade`
- `cidade_ibge`
- `estado`
- `cep`
- `codigo_pais`
- `tags`
- `recomendacoes`
- `enderecoEntrega`
- `dadosBancarios`
- `caracteristicas`

        ## Regras de negócio

        - O cadastro de cliente, fornecedor e transportadora compartilha a mesma base no servico `ClientesCadastro`.
        - `razao_social` e documentado oficialmente como obrigatorio no cadastro.
        - Dados fiscais e de endereco podem ser obrigatorios quando o cadastro participa de NF-e ou NFS-e.
        - Metodos marcados como DEPRECATED pela fonte oficial nao devem ser recomendados para novas integracoes sem validacao.
        - A LLM deve diferenciar "Documentado oficialmente" de "Necessita validacao".

        ## Validações

        - Validar CPF/CNPJ antes de operacoes fiscais.
        - Validar chave de integracao para evitar duplicidade.
        - Validar pagina e quantidade por pagina em listagens.
        - Validar campos condicionais de NF-e/NFS-e.
        - Validar comportamento real em ambiente autorizado antes de producao.

        ## Restrições

        - Nao registrar credenciais no repositorio.
        - Nao usar exemplos como payload oficial completo.
        - Nao inferir campos obrigatorios alem do que estiver documentado ou validado.
        - Nao ocultar status DEPRECATED quando aplicavel.

        ## Resposta esperada

        Retorno oficial: `clientes_status`. Quando houver `codigo_status`, a fonte oficial indica que `0` representa sucesso e valores maiores que `0` indicam erro descrito em `descricao_status`.

        ## Erros comuns

        - Campo obrigatorio ausente.
        - Cadastro nao localizado.
        - CPF/CNPJ invalido.
        - Codigo de integracao duplicado.
        - Tentativa de usar metodo depreciado sem justificativa.
        - Dados fiscais insuficientes para NF-e/NFS-e.

        ## Como resolver os erros

        - Conferir chave usada no payload.
        - Executar consulta antes de alteracao ou exclusao.
        - Validar CPF/CNPJ e dados fiscais.
        - Conferir `codigo_status` e `descricao_status`.
        - Revisar a fonte oficial e marcar lacunas como "Necessita validacao".

        ## Casos de uso

        - Assistente LLM respondendo duvidas sobre cadastro Omie.
        - Sincronizacao cadastral entre ERP e sistema legado.
        - Preparacao de dados para vendas, compras, financeiro, fiscal e servicos.
        - Auditoria de cadastros importados por API.
        - GraphRAG conectando cliente, fornecedor, transportadora e documentos operacionais.

        ## Exemplos completos

                > Todos os exemplos abaixo usam dados ficticios. A autenticacao Omie foi omitida de proposito para nao registrar segredos no repositorio.

        ### JSON base

        ```json
        {
  "call": "AlterarCliente",
  "param": [
    {
      "codigo_cliente_integracao": "CLI-FICTICIO-001",
      "razao_social": "Cliente Ficticio Ltda",
      "nome_fantasia": "Cliente Ficticio",
      "cnpj_cpf": "00.000.000/0001-00",
      "email": "contato@cliente-ficticio.example"
    }
  ]
}
        ```

        ### curl

        ```bash
        curl -X POST "https://app.omie.com.br/api/v1/geral/clientes/" \
          -H "Content-Type: application/json" \
          -d '{"call": "AlterarCliente", "param": [{"codigo_cliente_integracao": "CLI-FICTICIO-001", "razao_social": "Cliente Ficticio Ltda", "nome_fantasia": "Cliente Ficticio", "cnpj_cpf": "00.000.000/0001-00", "email": "contato@cliente-ficticio.example"}]}'
        ```

        ### Python

        ```python
        import requests

        payload = {'call': 'AlterarCliente', 'param': [{'codigo_cliente_integracao': 'CLI-FICTICIO-001', 'razao_social': 'Cliente Ficticio Ltda', 'nome_fantasia': 'Cliente Ficticio', 'cnpj_cpf': '00.000.000/0001-00', 'email': 'contato@cliente-ficticio.example'}]}
        response = requests.post("https://app.omie.com.br/api/v1/geral/clientes/", json=payload, timeout=30)
        print(response.json())
        ```

        ### JavaScript

        ```javascript
        const payload = {
  "call": "AlterarCliente",
  "param": [
    {
      "codigo_cliente_integracao": "CLI-FICTICIO-001",
      "razao_social": "Cliente Ficticio Ltda",
      "nome_fantasia": "Cliente Ficticio",
      "cnpj_cpf": "00.000.000/0001-00",
      "email": "contato@cliente-ficticio.example"
    }
  ]
};
        const response = await fetch("https://app.omie.com.br/api/v1/geral/clientes/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
        console.log(await response.json());
        ```

        ### TypeScript

        ```typescript
        type OmieRequest = {
          call: string;
          param: Array<Record<string, unknown>>;
        };

        const payload: OmieRequest = {
  "call": "AlterarCliente",
  "param": [
    {
      "codigo_cliente_integracao": "CLI-FICTICIO-001",
      "razao_social": "Cliente Ficticio Ltda",
      "nome_fantasia": "Cliente Ficticio",
      "cnpj_cpf": "00.000.000/0001-00",
      "email": "contato@cliente-ficticio.example"
    }
  ]
};
        const response = await fetch("https://app.omie.com.br/api/v1/geral/clientes/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
        const data: unknown = await response.json();
        console.log(data);
        ```

        ### PHP

        ```php
        <?php
        $payload = {"call": "AlterarCliente", "param": [{"codigo_cliente_integracao": "CLI-FICTICIO-001", "razao_social": "Cliente Ficticio Ltda", "nome_fantasia": "Cliente Ficticio", "cnpj_cpf": "00.000.000/0001-00", "email": "contato@cliente-ficticio.example"}]};
        $ch = curl_init("https://app.omie.com.br/api/v1/geral/clientes/");
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/json"]);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        echo curl_exec($ch);
        curl_close($ch);
        ```

        ### C#

        ```csharp
        using System.Net.Http.Json;

        var payload = new {
            call = "AlterarCliente",
            param = new object[] { new { codigo_cliente_integracao = "CLI-FICTICIO-001" } }
        };
        using var client = new HttpClient();
        var response = await client.PostAsJsonAsync("https://app.omie.com.br/api/v1/geral/clientes/", payload);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
        ```

        ### Java

        ```java
        var client = java.net.http.HttpClient.newHttpClient();
        var request = java.net.http.HttpRequest.newBuilder()
            .uri(java.net.URI.create("https://app.omie.com.br/api/v1/geral/clientes/"))
            .header("Content-Type", "application/json")
            .POST(java.net.http.HttpRequest.BodyPublishers.ofString("""{
  "call": "AlterarCliente",
  "param": [
    {
      "codigo_cliente_integracao": "CLI-FICTICIO-001",
      "razao_social": "Cliente Ficticio Ltda",
      "nome_fantasia": "Cliente Ficticio",
      "cnpj_cpf": "00.000.000/0001-00",
      "email": "contato@cliente-ficticio.example"
    }
  ]
}"""))
            .build();
        var response = client.send(request, java.net.http.HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
        ```

        ### Delphi

        ```pascal
        // Exemplo ficticio: montar o JSON com call="AlterarCliente" e param=[...].
        // Usar o componente HTTP padrao da aplicacao e enviar POST para o endpoint oficial.
        ```

        ### n8n

        ```json
        {
          "node": "HTTP Request",
          "method": "POST",
          "url": "https://app.omie.com.br/api/v1/geral/clientes/",
          "sendBody": true,
          "bodyContentType": "json",
          "jsonBody": {"call": "AlterarCliente", "param": [{"codigo_cliente_integracao": "CLI-FICTICIO-001", "razao_social": "Cliente Ficticio Ltda", "nome_fantasia": "Cliente Ficticio", "cnpj_cpf": "00.000.000/0001-00", "email": "contato@cliente-ficticio.example"}]}
        }
        ```


        ## FAQ

        ### 1. Como usar este metodo em uma integracao?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 2. Quando este metodo deve ser escolhido por uma LLM?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 3. Qual e o endpoint oficial?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 4. Qual entidade principal este metodo manipula?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 5. Ele serve para clientes?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 6. Ele serve para fornecedores?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 7. Ele serve para transportadoras?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 8. Como relacionar este metodo com vendas?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 9. Como relacionar este metodo com compras?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 10. Como relacionar este metodo com financeiro?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 11. Como relacionar este metodo com fiscal?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 12. Como pesquisar pelo codigo interno?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 13. Como pesquisar pelo codigo Omie?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 14. Como tratar CPF ou CNPJ?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 15. Quais campos precisam de validacao?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 16. Quais erros sao comuns?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 17. Como resolver falha de campo obrigatorio?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 18. Como resolver cadastro nao encontrado?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 19. Os exemplos sao oficiais?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 20. Este metodo esta pronto para producao?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

### 21. Como citar a fonte oficial ao responder?

Use as secoes de payload, regras e restricoes deste arquivo para altera dados de um cliente, fornecedor ou transportadora ja cadastrado. A fonte oficial documenta o metodo `AlterarCliente`, mas campos condicionais e comportamento em producao devem ser validados em ambiente autorizado. Exemplos sao ficticios.

        ## Perguntas naturais

        - Como escolher `AlterarCliente`?
        - Quando `AlterarCliente` e melhor que os metodos relacionados?
        - Quais campos desse metodo precisam de validacao?
        - Este metodo pode ser usado para cliente, fornecedor e transportadora?
        - Como uma LLM deve explicar o retorno desse metodo?

        ## Tags para RAG

        - omie
        - clientes
        - fornecedores
        - transportadoras
        - alteracao
        - enterprise-rag
        - graphrag

        ## Fonte oficial consultada

        - https://app.omie.com.br/api/v1/geral/clientes/
