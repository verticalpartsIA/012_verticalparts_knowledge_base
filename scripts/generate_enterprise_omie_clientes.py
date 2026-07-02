"""Gera a camada Enterprise LLM/RAG para Omie Geral Clientes.

O script usa apenas metadados extraidos da documentacao oficial ja consultada
e marca como "Necessita validacao" qualquer detalhe operacional que nao esteja
explicitamente fechado na fonte.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from textwrap import dedent


TODAY = date.today().isoformat()
SOURCE = "https://app.omie.com.br/api/v1/geral/clientes/"
ROOT = Path(".")


METHODS = [
    {
        "file": "alterar_cliente.md",
        "method": "AlterarCliente",
        "operation": "alteracao",
        "complexity": "media",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Altera dados de um cliente, fornecedor ou transportadora ja cadastrado.",
        "use": "atualizar dados cadastrais existentes, como razao social, nome fantasia, contato, endereco, tags, recomendacoes e dados fiscais.",
        "avoid": "criar novos cadastros, excluir registros ou associar apenas codigo interno.",
        "return_type": "clientes_status",
        "request_type": "clientes_cadastro",
        "related": ["ConsultarCliente", "IncluirCliente", "UpsertCliente", "AssociarCodIntCliente"],
    },
    {
        "file": "associar_cod_int_cliente.md",
        "method": "AssociarCodIntCliente",
        "operation": "associacao_codigo_interno",
        "complexity": "baixa",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Associa um codigo interno de integracao a um cadastro Omie existente.",
        "use": "vincular um identificador legado ou interno ao codigo de cliente/fornecedor do Omie.",
        "avoid": "alterar dados cadastrais amplos ou criar o cadastro completo.",
        "return_type": "clientes_status",
        "request_type": "clientes_cadastro_chave",
        "related": ["ConsultarCliente", "AlterarCliente", "UpsertCliente"],
    },
    {
        "file": "consultar_cliente.md",
        "method": "ConsultarCliente",
        "operation": "consulta",
        "complexity": "baixa",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Consulta um cadastro especifico por chave Omie ou codigo de integracao.",
        "use": "recuperar um cliente, fornecedor ou transportadora especifico antes de leitura, auditoria, alteracao ou decisao de integracao.",
        "avoid": "listar muitos cadastros ou sincronizar paginas de registros.",
        "return_type": "clientes_cadastro",
        "request_type": "clientes_cadastro_chave",
        "related": ["ListarClientes", "ListarClientesResumido", "AlterarCliente", "ExcluirCliente"],
    },
    {
        "file": "excluir_cliente.md",
        "method": "ExcluirCliente",
        "operation": "exclusao",
        "complexity": "alta",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Exclui um cadastro de cliente/fornecedor da base Omie.",
        "use": "remover cadastro quando houver decisao operacional validada e ausencia de bloqueios por vinculos.",
        "avoid": "desativar logicamente, corrigir dados ou remover registros com documentos e titulos relacionados sem avaliacao.",
        "return_type": "clientes_status",
        "request_type": "clientes_cadastro_chave",
        "related": ["ConsultarCliente", "AlterarCliente", "ListarClientes"],
    },
    {
        "file": "incluir_cliente.md",
        "method": "IncluirCliente",
        "operation": "inclusao",
        "complexity": "media",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Inclui um novo cliente, fornecedor ou transportadora no cadastro central do Omie.",
        "use": "criar um novo cadastro quando a integracao sabe que o registro ainda nao existe.",
        "avoid": "atualizar cadastro existente ou executar sincronizacao idempotente sem controle previo.",
        "return_type": "clientes_status",
        "request_type": "clientes_cadastro",
        "related": ["ConsultarCliente", "AlterarCliente", "UpsertCliente", "UpsertClienteCpfCnpj"],
    },
    {
        "file": "incluir_clientes_por_lote.md",
        "method": "IncluirClientesPorLote",
        "operation": "inclusao_lote",
        "complexity": "alta",
        "status": "Documentado oficialmente / DEPRECATED / Necessita validacao antes de uso",
        "summary": "Inclui cadastros por lote, com limite oficial de 50 ocorrencias por requisicao.",
        "use": "entender legado ou fluxo existente que ainda utilize inclusao em lote.",
        "avoid": "novas integracoes sem aprovacao tecnica, pois a fonte oficial marca o metodo como DEPRECATED.",
        "return_type": "clientes_lote_response",
        "request_type": "clientes_lote_request",
        "related": ["IncluirCliente", "UpsertClientesPorLote", "ListarClientes"],
    },
    {
        "file": "listar_clientes.md",
        "method": "ListarClientes",
        "operation": "listagem_completa",
        "complexity": "media",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Lista clientes cadastrados com retorno completo.",
        "use": "sincronizar, auditar ou paginar cadastros com maior riqueza de dados.",
        "avoid": "consultar um unico cadastro conhecido ou usar retorno resumido quando campos completos forem desnecessarios.",
        "return_type": "clientes_listfull_response",
        "request_type": "clientes_list_request",
        "related": ["ConsultarCliente", "ListarClientesResumido"],
    },
    {
        "file": "listar_clientes_resumido.md",
        "method": "ListarClientesResumido",
        "operation": "listagem_resumida",
        "complexity": "media",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Realiza pesquisa/listagem de clientes com retorno resumido.",
        "use": "pesquisar cadastros com menor volume de campos.",
        "avoid": "obter dados fiscais, endereco completo ou payload integral do cadastro.",
        "return_type": "clientes_list_response",
        "request_type": "clientes_list_request",
        "related": ["ConsultarCliente", "ListarClientes"],
    },
    {
        "file": "upsert_cliente.md",
        "method": "UpsertCliente",
        "operation": "upsert",
        "complexity": "media",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Inclui ou altera cadastro conforme chave informada.",
        "use": "sincronizar cadastro de forma idempotente quando existe chave estavel de integracao.",
        "avoid": "fluxos que exigem distinguir explicitamente criacao de alteracao.",
        "return_type": "clientes_status",
        "request_type": "clientes_cadastro",
        "related": ["IncluirCliente", "AlterarCliente", "UpsertClienteCpfCnpj"],
    },
    {
        "file": "upsert_cliente_cpf_cnpj.md",
        "method": "UpsertClienteCpfCnpj",
        "operation": "upsert_por_documento",
        "complexity": "media",
        "status": "Documentado oficialmente / Necessita validacao em integracao",
        "summary": "Inclui ou altera cadastro usando CPF/CNPJ como chave principal.",
        "use": "sincronizar cadastros quando o documento fiscal e a identidade confiavel.",
        "avoid": "ambientes com duplicidade cadastral ou documento fiscal nao confiavel.",
        "return_type": "clientes_status",
        "request_type": "clientes_cadastro",
        "related": ["UpsertCliente", "ConsultarCliente", "IncluirCliente"],
    },
    {
        "file": "upsert_clientes_por_lote.md",
        "method": "UpsertClientesPorLote",
        "operation": "upsert_lote",
        "complexity": "alta",
        "status": "Documentado oficialmente / DEPRECATED / Necessita validacao antes de uso",
        "summary": "Processa upsert de clientes por lote, com limite oficial de 50 ocorrencias por requisicao.",
        "use": "documentar legado ou avaliar fluxo existente de upsert em massa.",
        "avoid": "novas integracoes sem validacao, pois a fonte oficial marca o metodo como DEPRECATED.",
        "return_type": "clientes_lote_response",
        "request_type": "clientes_lote_request",
        "related": ["UpsertCliente", "IncluirClientesPorLote", "ListarClientes"],
    },
]


FIELD_GROUPS = {
    "clientes_cadastro": {
        "required": [
            "razao_social: Documentado oficialmente como preenchimento obrigatorio.",
            "cnpj_cpf: Necessario para emissao de NF-e/NFS-e.",
            "nome_fantasia: Necessario para emissao de NF-e/NFS-e.",
        ],
        "optional": [
            "codigo_cliente_omie",
            "codigo_cliente_integracao",
            "email",
            "telefone1_ddd",
            "telefone1_numero",
            "endereco",
            "endereco_numero",
            "bairro",
            "cidade",
            "cidade_ibge",
            "estado",
            "cep",
            "codigo_pais",
            "tags",
            "recomendacoes",
            "enderecoEntrega",
            "dadosBancarios",
            "caracteristicas",
        ],
    },
    "clientes_cadastro_chave": {
        "required": [
            "codigo_cliente_omie ou codigo_cliente_integracao: a chave exata deve identificar o cadastro.",
        ],
        "optional": ["Nenhum campo opcional relevante foi documentado para a chave."],
    },
    "clientes_list_request": {
        "required": ["pagina", "registros_por_pagina"],
        "optional": [
            "apenas_importado_api",
            "filtrar_por_data_de",
            "filtrar_por_data_ate",
            "filtrar_por_hora_de",
            "filtrar_por_hora_ate",
            "filtrar_apenas_inclusao",
            "filtrar_apenas_alteracao",
            "clientesFiltro",
            "clientesPorCodigo",
            "exibir_caracteristicas",
            "exibir_obs",
        ],
    },
    "clientes_lote_request": {
        "required": ["lote", "clientes_cadastro"],
        "optional": ["Campos opcionais de cada item seguem clientes_cadastro."],
    },
}


def ensure_dirs() -> None:
    for path in [
        "standards",
        "graphs/omie",
        "business/omie",
        "datasets/questions",
        "rag/chunks/clientes",
        "embeddings",
        "tests/knowledge",
        "reports",
        "docs/omie/geral/clientes",
        "schemas/omie/geral/clientes",
    ]:
        (ROOT / path).mkdir(parents=True, exist_ok=True)


def write(path: str, content: str) -> None:
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / path).write_text(content.strip() + "\n", encoding="utf-8")


def yaml_for_method(meta: dict) -> str:
    lines = [
        "---",
        f'title: "{meta["method"]} - Omie Geral Clientes"',
        'service: "ClientesCadastro"',
        'domain: "omie.geral"',
        'resource: "clientes"',
        f'method: "{meta["method"]}"',
        f'endpoint: "{SOURCE}"',
        'http_method: "POST"',
        'version: "1"',
        'entity: "cliente_fornecedor_transportadora"',
        "related_entities:",
        "  - Cliente",
        "  - Fornecedor",
        "  - Transportadora",
        "  - Pedido",
        "  - NF-e",
        "  - Conta a Receber",
        "  - Conta a Pagar",
        "  - CRM",
        "  - Projeto",
        "  - Serviço",
        "  - Produtos",
        "  - Categorias",
        "  - Anexos",
        "related_methods:",
    ]
    lines.extend(f"  - {item}" for item in meta["related"])
    lines.extend(
        [
            "permissions:",
            '  - "Necessita credenciais Omie validas fora do repositorio"',
            '  - "Nao documentar chaves, segredos ou senhas"',
            f'complexity: "{meta["complexity"]}"',
            f'status: "{meta["status"]}"',
            f'source: "{SOURCE}"',
            f'last_review: "{TODAY}"',
            "tags:",
            "  - omie",
            "  - clientes",
            "  - fornecedores",
            "  - transportadoras",
            f"  - {meta['operation']}",
            "  - enterprise-rag",
            "keywords:",
            '  - "ClientesCadastro"',
            f'  - "{meta["method"]}"',
            '  - "cadastro Omie"',
            '  - "RAG"',
            '  - "LLM"',
            "questions:",
            f'  - "Como usar {meta["method"]}?"',
            '  - "Como escolher o metodo correto para clientes?"',
            '  - "Quais campos precisam ser validados?"',
            "use_cases:",
            "  - integracao_erp",
            "  - sincronizacao_cadastral",
            "  - assistente_llm",
            "  - rag_operacional",
            'business_area: "ERP / Cadastros / Geral"',
            "llm_ready: true",
            "rag_ready: true",
            "graph_ready: true",
            "embedding_version: 1",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def code_examples(meta: dict) -> str:
    method = meta["method"]
    sample_param = {
        "clientes_cadastro": {
            "codigo_cliente_integracao": "CLI-FICTICIO-001",
            "razao_social": "Cliente Ficticio Ltda",
            "nome_fantasia": "Cliente Ficticio",
            "cnpj_cpf": "00.000.000/0001-00",
            "email": "contato@cliente-ficticio.example",
        },
        "clientes_cadastro_chave": {"codigo_cliente_integracao": "CLI-FICTICIO-001"},
        "clientes_list_request": {
            "pagina": 1,
            "registros_por_pagina": 50,
            "apenas_importado_api": "N",
        },
        "clientes_lote_request": {
            "lote": 1,
            "clientes_cadastro": [
                {
                    "codigo_cliente_integracao": "CLI-FICTICIO-001",
                    "razao_social": "Cliente Ficticio Ltda",
                    "nome_fantasia": "Cliente Ficticio",
                }
            ],
        },
    }[meta["request_type"]]
    body = {"call": method, "param": [sample_param]}
    body_json = json.dumps(body, indent=2, ensure_ascii=False)
    return dedent(
        f"""\
        > Todos os exemplos abaixo usam dados ficticios. A autenticacao Omie foi omitida de proposito para nao registrar segredos no repositorio.

        ### JSON base

        ```json
        {body_json}
        ```

        ### curl

        ```bash
        curl -X POST "{SOURCE}" \\
          -H "Content-Type: application/json" \\
          -d '{json.dumps(body, ensure_ascii=False)}'
        ```

        ### Python

        ```python
        import requests

        payload = {repr(body)}
        response = requests.post("{SOURCE}", json=payload, timeout=30)
        print(response.json())
        ```

        ### JavaScript

        ```javascript
        const payload = {json.dumps(body, indent=2, ensure_ascii=False)};
        const response = await fetch("{SOURCE}", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload)
        }});
        console.log(await response.json());
        ```

        ### TypeScript

        ```typescript
        type OmieRequest = {{
          call: string;
          param: Array<Record<string, unknown>>;
        }};

        const payload: OmieRequest = {json.dumps(body, indent=2, ensure_ascii=False)};
        const response = await fetch("{SOURCE}", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload)
        }});
        const data: unknown = await response.json();
        console.log(data);
        ```

        ### PHP

        ```php
        <?php
        $payload = {json.dumps(body, ensure_ascii=False)};
        $ch = curl_init("{SOURCE}");
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

        var payload = new {{
            call = "{method}",
            param = new object[] {{ new {{ codigo_cliente_integracao = "CLI-FICTICIO-001" }} }}
        }};
        using var client = new HttpClient();
        var response = await client.PostAsJsonAsync("{SOURCE}", payload);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
        ```

        ### Java

        ```java
        var client = java.net.http.HttpClient.newHttpClient();
        var request = java.net.http.HttpRequest.newBuilder()
            .uri(java.net.URI.create("{SOURCE}"))
            .header("Content-Type", "application/json")
            .POST(java.net.http.HttpRequest.BodyPublishers.ofString(\"\"\"{body_json}\"\"\"))
            .build();
        var response = client.send(request, java.net.http.HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
        ```

        ### Delphi

        ```pascal
        // Exemplo ficticio: montar o JSON com call="{method}" e param=[...].
        // Usar o componente HTTP padrao da aplicacao e enviar POST para o endpoint oficial.
        ```

        ### n8n

        ```json
        {{
          "node": "HTTP Request",
          "method": "POST",
          "url": "{SOURCE}",
          "sendBody": true,
          "bodyContentType": "json",
          "jsonBody": {json.dumps(body, ensure_ascii=False)}
        }}
        ```
        """
    )


FAQ_BASE = [
    "Como usar este metodo em uma integracao?",
    "Quando este metodo deve ser escolhido por uma LLM?",
    "Qual e o endpoint oficial?",
    "Qual entidade principal este metodo manipula?",
    "Ele serve para clientes?",
    "Ele serve para fornecedores?",
    "Ele serve para transportadoras?",
    "Como relacionar este metodo com vendas?",
    "Como relacionar este metodo com compras?",
    "Como relacionar este metodo com financeiro?",
    "Como relacionar este metodo com fiscal?",
    "Como pesquisar pelo codigo interno?",
    "Como pesquisar pelo codigo Omie?",
    "Como tratar CPF ou CNPJ?",
    "Quais campos precisam de validacao?",
    "Quais erros sao comuns?",
    "Como resolver falha de campo obrigatorio?",
    "Como resolver cadastro nao encontrado?",
    "Os exemplos sao oficiais?",
    "Este metodo esta pronto para producao?",
    "Como citar a fonte oficial ao responder?",
]


def faq(meta: dict) -> str:
    lines = []
    for i, question in enumerate(FAQ_BASE, start=1):
        answer = (
            f"Use as secoes de payload, regras e restricoes deste arquivo para {meta['summary'].lower()} "
            f"A fonte oficial documenta o metodo `{meta['method']}`, mas campos condicionais e comportamento em producao "
            "devem ser validados em ambiente autorizado. Exemplos sao ficticios."
        )
        lines.append(f"### {i}. {question}\n\n{answer}")
    return "\n\n".join(lines)


def method_doc(meta: dict) -> str:
    fg = FIELD_GROUPS[meta["request_type"]]
    required = "\n".join(f"- `{item}`" if ":" not in item else f"- {item}" for item in fg["required"])
    optional = "\n".join(f"- `{item}`" if item and item[0].islower() else f"- {item}" for item in fg["optional"])
    related = "\n".join(f"- `{m}`" for m in meta["related"])
    body = dedent(
        f"""\
        # {meta['method']}

        ## Objetivo

        {meta['summary']} Este documento foi estruturado para LLMs, RAG e GraphRAG, nao como tutorial humano isolado.

        ## Quando utilizar

        Utilize `{meta['method']}` para {meta['use']}

        ## Quando NÃO utilizar

        Nao utilize `{meta['method']}` para {meta['avoid']} Quando houver duvida, a LLM deve responder que a decisao necessita validacao.

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

        {related}

        ## Pré-requisitos

        - Acesso autorizado ao ambiente Omie.
        - Credenciais mantidas fora do repositorio.
        - Decisao clara sobre chave de identificacao: codigo Omie, codigo de integracao ou CPF/CNPJ.
        - Validacao de campos obrigatorios conforme finalidade: cadastro simples, fiscal, vendas, compras ou financeiro.

        ## Payload

        - Tipo oficial de entrada: `{meta['request_type']}`.
        - Tipo oficial de retorno: `{meta['return_type']}`.
        - Metodo documentado oficialmente: `{meta['method']}`.
        - Endpoint oficial: `{SOURCE}`.

        ## Campos obrigatórios

        {required}

        ## Campos opcionais

        {optional}

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

        Retorno oficial: `{meta['return_type']}`. Quando houver `codigo_status`, a fonte oficial indica que `0` representa sucesso e valores maiores que `0` indicam erro descrito em `descricao_status`.

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

        {code_examples(meta)}

        ## FAQ

        {faq(meta)}

        ## Perguntas naturais

        - Como escolher `{meta['method']}`?
        - Quando `{meta['method']}` e melhor que os metodos relacionados?
        - Quais campos desse metodo precisam de validacao?
        - Este metodo pode ser usado para cliente, fornecedor e transportadora?
        - Como uma LLM deve explicar o retorno desse metodo?

        ## Tags para RAG

        - omie
        - clientes
        - fornecedores
        - transportadoras
        - {meta['operation']}
        - enterprise-rag
        - graphrag

        ## Fonte oficial consultada

        - {SOURCE}
        """
    )
    return yaml_for_method(meta) + body


def standard_doc() -> str:
    return dedent(
        f"""\
        # LLM Document Standard

        ## Objetivo

        Este padrao define como todos os arquivos Markdown do repositorio devem ser escritos para uso por LLMs, RAG, GraphRAG, embeddings e avaliacao automatizada.

        ## Estrutura obrigatoria

        1. YAML front matter.
        2. Titulo H1 unico.
        3. Objetivo.
        4. Quando utilizar.
        5. Quando nao utilizar.
        6. Fluxo de negocio.
        7. Entidades relacionadas.
        8. Metodos relacionados.
        9. Pre-requisitos.
        10. Payload ou conteudo tecnico principal.
        11. Campos obrigatorios.
        12. Campos opcionais.
        13. Regras de negocio.
        14. Validacoes.
        15. Restricoes.
        16. Resposta esperada.
        17. Erros comuns.
        18. Como resolver os erros.
        19. Casos de uso.
        20. Exemplos completos.
        21. FAQ.
        22. Perguntas naturais.
        23. Tags para RAG.
        24. Fonte oficial consultada.

        ## Metadados YAML

        Todo Markdown em `docs/omie` deve iniciar com os campos abaixo:

        ```yaml
        ---
        title:
        service:
        domain:
        resource:
        method:
        endpoint:
        http_method:
        version:
        entity:
        related_entities:
        related_methods:
        permissions:
        complexity:
        status:
        source:
        last_review:
        tags:
        keywords:
        questions:
        use_cases:
        business_area:
        llm_ready: true
        rag_ready: true
        graph_ready: true
        embedding_version: 1
        ---
        ```

        ## Padrao de titulos

        Use um unico H1 por documento. Use H2 para secoes obrigatorias. H3 deve ser usado apenas para exemplos, FAQ ou subsecoes tecnicas.

        ## Padrao de exemplos

        Exemplos devem ser ficticios, identificados como ficticios e nao devem registrar credenciais, segredos ou senhas. Quando a autenticacao for necessaria, declarar que foi omitida por seguranca.

        ## Padrao de JSON

        JSON deve ser valido, indentado com dois espacos e limitado ao necessario para demonstrar a estrutura. Campos nao confirmados devem ser marcados como "Necessita validacao".

        ## Padrao de perguntas naturais

        Cada documento de metodo deve conter perguntas que reflitam linguagem real de usuarios, incluindo variacoes sobre cliente, fornecedor, transportadora, codigo interno, codigo Omie, CPF, CNPJ e finalidade operacional.

        ## Padrao de FAQ

        Cada metodo deve ter pelo menos 20 perguntas e respostas. Respostas devem ser curtas, verificaveis e baseadas na fonte ou marcadas como pendencia.

        ## Padrao de relacionamentos

        Relacionamentos devem mencionar entidades de negocio e metodos relacionados. Relacionamentos graficos devem ser espelhados em `graphs/`.

        ## Padrao de tags

        Tags devem incluir dominio, recurso, operacao, entidade e finalidade RAG. Exemplo: `omie`, `clientes`, `fornecedores`, `listagem`, `enterprise-rag`.

        ## Padrao de casos de uso

        Casos de uso devem indicar tarefa, contexto, entrada esperada, metodo recomendado e criterio de sucesso.

        ## Padrao de chunking

        Chunks devem ter metadados completos, preferencialmente entre 500 e 900 tokens, sem misturar metodos diferentes. A unidade minima recomendada e metodo + secao.

        ## Padrao para embeddings

        Registrar `embedding_version`. Ao trocar modelo, reindexar e atualizar estrategia. Preservar idioma portugues do Brasil e termos tecnicos originais.

        ## Padrao para RAG

        RAG deve combinar busca vetorial, busca lexical, filtros por metadados e citacao de fontes. Respostas devem indicar "Documentado oficialmente" ou "Necessita validacao".

        ## Padrao para GraphRAG

        GraphRAG deve mapear entidades, metodos, dominios e documentos. Mermaid pode representar a topologia em Markdown.

        ## Padrao de nomenclatura

        Arquivos devem usar `snake_case`. Metodos oficiais devem preservar capitalizacao original da Omie dentro do conteudo.

        ## Padrao para links internos

        Use caminhos relativos ao repositorio quando apontar para documentos internos. Nao usar links quebrados.

        ## Padrao para referencias oficiais

        Toda informacao oficial deve citar a URL consultada. Toda informacao nao explicitamente confirmada deve ser marcada como "Necessita validacao".

        ## Padrao para versionamento

        Mudancas relevantes devem passar por branch, commit e pull request. Atualize `last_review` quando revisar conteudo contra fonte oficial.
        """
    )


def yaml_generic(title: str, resource: str, method: str = "indice") -> str:
    return "\n".join(
        [
            "---",
            f'title: "{title}"',
            'service: "ClientesCadastro"',
            'domain: "omie.geral"',
            f'resource: "{resource}"',
            f'method: "{method}"',
            f'endpoint: "{SOURCE}"',
            'http_method: "POST"',
            'version: "1"',
            'entity: "cliente_fornecedor_transportadora"',
            "related_entities:",
            "  - Cliente",
            "  - Fornecedor",
            "  - Transportadora",
            "related_methods:",
            "  - ConsultarCliente",
            "  - IncluirCliente",
            "  - AlterarCliente",
            "  - ListarClientes",
            "permissions:",
            '  - "Necessita credenciais Omie validas fora do repositorio"',
            'complexity: "media"',
            'status: "Necessita validacao"',
            f'source: "{SOURCE}"',
            f'last_review: "{TODAY}"',
            "tags:",
            "  - omie",
            "  - geral",
            "  - clientes",
            "  - enterprise-rag",
            "keywords:",
            "  - ClientesCadastro",
            "  - VerticalParts Knowledge Base",
            "questions:",
            '  - "Como usar o cadastro de clientes da Omie?"',
            "use_cases:",
            "  - assistente_llm",
            "  - rag_operacional",
            'business_area: "ERP / Cadastros / Geral"',
            "llm_ready: true",
            "rag_ready: true",
            "graph_ready: true",
            "embedding_version: 1",
            "---",
            "",
        ]
    )


def generic_enterprise_sections(title: str) -> str:
    return dedent(
        f"""\

        ## Objetivo

        Organizar conhecimento sobre {title} em formato reutilizavel por LLMs, RAG e GraphRAG.

        ## Quando utilizar

        Use este documento quando a pergunta exigir contexto geral, indice de navegacao ou ponto de entrada para documentos detalhados.

        ## Quando NÃO utilizar

        Nao use este documento como contrato final de payload quando existir um documento de metodo mais especifico.

        ## Fluxo de negócio

        O usuario formula uma pergunta, a LLM identifica o dominio, consulta este indice e entao navega para o documento detalhado mais adequado.

        ## Casos de uso

        - Navegacao por dominio.
        - Recuperacao RAG de documentos detalhados.
        - Expansao GraphRAG por entidade relacionada.
        - Triagem de perguntas naturais.

        ## Entidades relacionadas

        - Cliente
        - Fornecedor
        - Transportadora

        ## Métodos relacionados

        - `ConsultarCliente`
        - `IncluirCliente`
        - `AlterarCliente`
        - `ListarClientes`

        ## Exemplos completos

        ### curl

        Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

        ### Python

        Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

        ### JavaScript

        Exemplo omitido em indice. Consulte documentos de metodo para exemplos ficticios completos.

        ## FAQ

        ### 1. Este documento substitui os metodos detalhados?

        Nao. Ele direciona a LLM para o documento especifico.

        ### 2. O conteudo e oficial?

        Partes derivadas da fonte oficial sao marcadas no documento. Lacunas devem ser tratadas como "Necessita validacao".

        ## Perguntas naturais

        - Onde encontro os metodos de ClientesCadastro?
        - Qual documento devo consultar para payload?
        - O que ainda necessita validacao?

        ## Tags para RAG

        - omie
        - indice
        - enterprise-rag
        - graphrag
        """
    )


def retrofit_docs_omie() -> None:
    targets = {
        "docs/README.md": ("Documentacao Geral", "docs"),
        "docs/omie/README.md": ("Omie API - Indice", "omie"),
        "docs/omie/geral/clientes_fornecedores_transportadoras.md": ("Indice Clientes, Fornecedores e Transportadoras", "clientes"),
        "docs/omie/financeiro/contas_a_pagar.md": ("Contas a Pagar", "financeiro"),
        "docs/omie/financeiro/contas_a_receber.md": ("Contas a Receber", "financeiro"),
        "docs/omie/financeiro/movimentos_financeiros.md": ("Movimentos Financeiros", "financeiro"),
        "docs/omie/vendas/pedidos_de_venda.md": ("Pedidos de Venda", "vendas"),
        "docs/omie/servicos/ordem_de_servico.md": ("Ordem de Servico", "servicos"),
    }
    for path, (title, resource) in targets.items():
        p = ROOT / path
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        body = text
        if text.startswith("---\n"):
            parts = text.split("---\n", 2)
            if len(parts) == 3:
                body = parts[2]
        if "## Objetivo" not in body:
            body = body + generic_enterprise_sections(title)
        elif "## Casos de uso" not in body:
            body = body + "\n## Casos de uso\n\n- Navegacao por dominio.\n- Recuperacao RAG.\n- Expansao GraphRAG.\n"
        write(path, yaml_generic(title, resource) + body)


def clientes_readme() -> str:
    return (
        yaml_generic("Omie Geral Clientes - Guia do Servico", "clientes", "indice")
        + dedent(
            f"""\
            # Omie Geral: Clientes, Fornecedores e Transportadoras

            ## Objetivo

            Explicar o servico `ClientesCadastro` para LLMs e sistemas RAG, conectando metodos oficiais, entidades, fluxos de negocio e criterios de escolha.

            ## Quando utilizar

            Use este guia quando a pergunta envolver escolha entre consultar, incluir, alterar, excluir, listar, associar codigo interno ou executar upsert de clientes, fornecedores e transportadoras.

            ## Quando NÃO utilizar

            Nao use este guia como contrato final de payload. Para payload, exemplos e FAQ completa, consulte o arquivo do metodo especifico.

            ## Fluxo de negócio

            1. Identificar se a entidade atua como cliente, fornecedor ou transportadora.
            2. Identificar se a intencao e consulta, cadastro, alteracao, exclusao, listagem, associacao ou upsert.
            3. Selecionar o metodo oficial.
            4. Validar campos obrigatorios e condicionais.
            5. Responder com fonte oficial e status de validacao.

            ## Casos de uso

            - Selecionar metodo correto para assistente LLM.
            - Explicar o relacionamento entre cadastro, financeiro, vendas, compras, fiscal, CRM e servicos.
            - Direcionar perguntas para documentos de metodo.
            - Apoiar GraphRAG com entidades conectadas.

            ## O que representa este serviço

            O serviço `ClientesCadastro` representa o cadastro central de participantes comerciais no Omie. Ele é usado para manter dados cadastrais de clientes, fornecedores, transportadoras e outros agentes que participam de fluxos financeiros, comerciais, fiscais, logísticos e de serviços.

            ## Por que clientes, fornecedores e transportadoras usam o mesmo cadastro

            Na Omie, o cadastro concentra dados de identificação, endereço, contato, inscrições fiscais, tags, recomendações e vínculos operacionais em uma mesma entidade base. Essa modelagem evita duplicidade quando a mesma pessoa física ou jurídica atua em mais de um papel.

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

            - `AlterarCliente`
            - `AssociarCodIntCliente`
            - `ConsultarCliente`
            - `ExcluirCliente`
            - `IncluirCliente`
            - `IncluirClientesPorLote` - DEPRECATED na fonte oficial
            - `ListarClientes`
            - `ListarClientesResumido`
            - `UpsertCliente`
            - `UpsertClienteCpfCnpj`
            - `UpsertClientesPorLote` - DEPRECATED na fonte oficial

            ## Exemplos completos

            ### curl

            Consulte o documento do metodo escolhido. Este guia nao deve ser usado para montar requisicao final.

            ### Python

            Consulte o documento do metodo escolhido. Este guia nao deve ser usado para montar requisicao final.

            ### JavaScript

            Consulte o documento do metodo escolhido. Este guia nao deve ser usado para montar requisicao final.

            ## FAQ

            ### 1. Como uma LLM escolhe o metodo correto?

            Ela deve identificar a intencao do usuario e direcionar para consulta, inclusao, alteracao, exclusao, listagem, associacao ou upsert.

            ### 2. Fornecedor usa o mesmo cadastro?

            Sim. A base cadastral e compartilhada; o papel depende do fluxo operacional.

            ### 3. Transportadora usa o mesmo cadastro?

            Sim. Transportadora pode ser representada na mesma base e relacionada a pedidos e documentos fiscais.

            ## Perguntas naturais

            - Como escolher entre ConsultarCliente e ListarClientes?
            - Como cadastrar fornecedor?
            - Como localizar transportadora?
            - Quando usar upsert?

            ## Tags para RAG

            - omie
            - clientes
            - fornecedores
            - transportadoras
            - enterprise-rag
            - graphrag

            ## GraphRAG

            Consulte `graphs/omie/clientes.graph.md` para o grafo de relacionamento entre cliente, fornecedor, transportadora e dominios operacionais.

            ## Fonte oficial consultada

            - {SOURCE}
            """
        )
    )


def graph_doc() -> str:
    return dedent(
        """\
        # GraphRAG: Omie Clientes

        ## Objetivo

        Representar relacoes entre o cadastro central de clientes/fornecedores/transportadoras e dominios operacionais do ERP.

        ```mermaid
        graph TD
          Cliente["Cliente"] --> Pedido["Pedido"]
          Cliente --> NF_e["NF-e"]
          Cliente --> ContaReceber["Conta a Receber"]
          Cliente --> CRM["CRM"]
          Cliente --> Projeto["Projeto"]
          Cliente --> Servico["Serviço"]
          Fornecedor["Fornecedor"] --> ContaPagar["Conta a Pagar"]
          Fornecedor --> Compras["Compras"]
          Transportadora["Transportadora"] --> Pedido
          Transportadora --> NF_e
          Pedido --> Produtos["Produtos"]
          Pedido --> Categorias["Categorias"]
          Pedido --> Anexos["Anexos"]
          Servico --> ContaReceber
          Projeto --> Categorias
          NF_e --> Fiscal["Fiscal"]
          ContaReceber --> Financeiro["Financeiro"]
          ContaPagar --> Financeiro
          Cliente --- Cadastro["ClientesCadastro"]
          Fornecedor --- Cadastro
          Transportadora --- Cadastro
        ```

        ## Leitura para LLM

        A mesma entidade cadastral pode assumir papel de cliente, fornecedor ou transportadora. O papel operacional depende do fluxo em que o cadastro e usado: vendas, compras, financeiro, fiscal, servicos ou CRM.
        """
    )


def business_doc() -> str:
    return dedent(
        f"""\
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

        - {SOURCE}
        """
    )


def questions_dataset() -> None:
    intents = [
        "consultar",
        "localizar",
        "alterar",
        "incluir",
        "excluir",
        "listar",
        "sincronizar",
        "validar",
        "pesquisar",
        "atualizar",
    ]
    entities = ["cliente", "fornecedor", "transportadora"]
    fields = [
        "codigo interno",
        "codigo Omie",
        "CNPJ",
        "CPF",
        "email",
        "telefone",
        "endereco",
        "razao social",
        "nome fantasia",
        "tag",
    ]
    templates = [
        "Como {intent} {entity} pelo {field}?",
        "Qual metodo devo usar para {intent} {entity} usando {field}?",
        "A Omie permite {intent} {entity} quando tenho apenas {field}?",
        "Como uma LLM deve responder sobre {intent} {entity} por {field}?",
    ]
    questions = []
    seen = set()
    for template in templates:
        for intent in intents:
            for entity in entities:
                for field in fields:
                    q = template.format(intent=intent, entity=entity, field=field)
                    if q not in seen:
                        seen.add(q)
                        questions.append(
                            {
                                "question": q,
                                "domain": "omie.geral",
                                "resource": "clientes",
                                "expected_source": SOURCE,
                                "status": "Necessita validacao quando depender de campo condicional",
                            }
                        )
                    if len(questions) >= 300:
                        break
                if len(questions) >= 300:
                    break
            if len(questions) >= 300:
                break
        if len(questions) >= 300:
            break
    write("datasets/questions/clientes.json", json.dumps(questions, indent=2, ensure_ascii=False))


def chunks() -> None:
    index = []
    for meta in METHODS:
        for suffix, focus in [
            ("identidade", "identidade, YAML, endpoint, metodo, dominio e status"),
            ("contrato", "payload, campos obrigatorios, campos opcionais e retorno"),
            ("operacao", "quando usar, quando nao usar, regras, validacoes e restricoes"),
            ("faq", "FAQ, perguntas naturais, tags e uso por LLM"),
        ]:
            chunk_name = meta["file"].replace(".md", f".{suffix}.chunk.md")
            content = dedent(
                f"""\
                ---
                source_path: "docs/omie/geral/clientes/{meta['file']}"
                chunk_id: "{meta['method']}.{suffix}"
                service: "ClientesCadastro"
                method: "{meta['method']}"
                endpoint: "{SOURCE}"
                focus: "{focus}"
                status: "{meta['status']}"
                embedding_version: 1
                ---

                # Chunk {meta['method']} - {suffix}

                Este chunk concentra {focus} para o metodo `{meta['method']}` do servico `ClientesCadastro`.

                Metodo oficial: `{meta['method']}`.
                Endpoint oficial: `{SOURCE}`.
                Entrada oficial: `{meta['request_type']}`.
                Retorno oficial: `{meta['return_type']}`.
                Status: {meta['status']}.

                Uso recomendado: {meta['use']}

                Nao usar para: {meta['avoid']}

                Relacionamentos de negocio: cliente, fornecedor, transportadora, pedido, NF-e, conta a receber, conta a pagar, CRM, projeto, servico, produtos, categorias e anexos.

                Regra para LLM: responder apenas com base no documento fonte, declarar exemplos como ficticios e indicar "Necessita validacao" quando o comportamento depender de credenciais, ambiente, regra fiscal ou campos condicionais.

                Contexto expandido para recuperacao: o servico `ClientesCadastro` e o ponto central de cadastro de participantes no Omie. A mesma base pode representar cliente, fornecedor ou transportadora, e a interpretacao correta depende do fluxo de negocio. Em vendas, o cadastro se conecta a pedido, faturamento, conta a receber, CRM e emissao fiscal. Em compras, o mesmo cadastro pode atuar como fornecedor e alimentar conta a pagar, categorias, projetos e documentos de entrada. Em logistica, a transportadora pode aparecer vinculada a pedidos, entrega e NF-e. Em servicos, o cadastro pode representar tomador, pagador ou contato operacional. Portanto, a recuperacao nao deve olhar apenas para o nome do metodo; deve considerar intencao, entidade, operacao, chave de busca e status documental.

                Criterios de escolha: quando o usuario quer localizar um registro especifico, priorizar metodos de consulta por chave. Quando deseja criar, priorizar inclusao ou upsert conforme a idempotencia esperada. Quando deseja mudar dados, priorizar alteracao. Quando deseja percorrer a base, priorizar listagem paginada. Quando o metodo estiver marcado como DEPRECATED, a resposta deve avisar antes de sugerir qualquer uso. Quando o usuario perguntar por CPF, CNPJ, codigo interno ou codigo Omie, a LLM deve diferenciar chave documentada oficialmente de comportamento que necessita validacao.

                Campos e validacoes: `razao_social` e documentado oficialmente como obrigatorio no cadastro. A fonte oficial tambem sinaliza campos condicionais para NF-e/NFS-e, como CPF/CNPJ, nome fantasia, endereco, estado, CEP, e-mail e informacoes fiscais. Esses campos nao devem ser tratados como universalmente obrigatorios para todos os cenarios sem confirmar o uso pretendido. Exemplos de payload sao ficticios, incompletos por seguranca e nao representam contrato oficial integral. A autenticacao foi omitida de proposito.

                Estrategia RAG: indexar este chunk com filtros por `service`, `method`, `operation`, `status`, `entity` e `embedding_version`. Para reranking, priorizar match exato do metodo, presenca de endpoint oficial, compatibilidade com a intencao do usuario e status nao depreciado. Para GraphRAG, expandir vizinhos como Cliente, Fornecedor, Transportadora, Pedido, NF-e, Conta a Receber, Conta a Pagar, CRM, Projeto, Servico, Produtos, Categorias e Anexos.
                """
            )
            write(f"rag/chunks/clientes/{chunk_name}", content)
            index.append(
                {
                    "chunk": f"rag/chunks/clientes/{chunk_name}",
                    "source": f"docs/omie/geral/clientes/{meta['file']}",
                    "method": meta["method"],
                    "focus": focus,
                    "status": meta["status"],
                }
            )
    write("rag/chunks/clientes/index.json", json.dumps(index, indent=2, ensure_ascii=False))
    write(
        "rag/chunks/clientes/retrieval_strategy.md",
        dedent(
            """\
            # Estratégia de Recuperação: Clientes

            ## Busca híbrida

            Combine busca vetorial com busca lexical por método oficial, entidade, CPF/CNPJ, código interno, código Omie e status.

            ## Reranking

            Reordene resultados priorizando método exato, status documentado oficialmente, proximidade semântica e presença de payload.

            ## GraphRAG

            Use `graphs/omie/clientes.graph.md` para expandir consultas que envolvem relações entre cliente, fornecedor, transportadora, financeiro, fiscal, vendas, compras e serviços.

            ## Critério de resposta

            A resposta deve citar o documento de origem e declarar se o trecho é "Documentado oficialmente" ou "Necessita validação".
            """
        ),
    )


def embeddings_doc() -> str:
    return dedent(
        """\
        # Embeddings

        ## Objetivo

        Orientar escolha de modelos de embedding para a VerticalParts Knowledge Base.

        ## OpenAI

        Boa qualidade geral, suporte forte a português e integração simples com pipelines modernos.

        ## Gemini

        Opção útil para ecossistema Google e integrações com Vertex AI.

        ## VoyageAI

        Forte em recuperação semântica e cenários RAG especializados.

        ## BGE

        Família aberta com boa relação custo/controle para hospedagem própria.

        ## E5

        Modelo aberto relevante para busca textual e pares pergunta-documento.

        ## Nomic

        Boa alternativa aberta para embeddings gerais e uso local.

        ## Qwen

        Opção aberta com boa cobertura multilíngue e ecossistema ativo.

        ## Jina

        Opção forte para busca neural, documentos longos e pipelines de recuperação.

        ## Regra de versionamento

        Sempre registrar `embedding_version` e reindexar quando trocar modelo, dimensão ou normalização.
        """
    )


def tests_doc() -> str:
    return dedent(
        """\
        import re
        from pathlib import Path


        DOCS = list(Path("docs/omie").rglob("*.md"))


        def read(path):
            return path.read_text(encoding="utf-8")


        def test_all_omie_docs_have_yaml():
            assert DOCS
            for path in DOCS:
                assert read(path).startswith("---\\n"), path


        def test_method_docs_have_enterprise_sections():
            required = [
                "## FAQ",
                "## Perguntas naturais",
                "## Tags para RAG",
                "## Fonte oficial consultada",
                "llm_ready: true",
                "source:",
                "status:",
            ]
            for path in Path("docs/omie/geral/clientes").glob("*.md"):
                if path.name == "README.md":
                    continue
                text = read(path)
                for item in required:
                    assert item in text, f"{path}: {item}"
                assert len(re.findall(r"^### \\d+\\.", text, re.MULTILINE)) >= 20, path
                assert "### curl" in text, path
                assert "### Python" in text, path
                assert "### JavaScript" in text, path
                assert "### TypeScript" in text, path
                assert "### PHP" in text, path
                assert "### C#" in text, path
                assert "### Java" in text, path
                assert "### Delphi" in text, path
                assert "### n8n" in text, path
        """
    )


def score_script() -> str:
    return dedent(
        """\
        from __future__ import annotations

        from pathlib import Path


        ROOT = Path(".")
        DOCS = list((ROOT / "docs").rglob("*.md"))
        REPORT = ROOT / "reports" / "knowledge_score.md"


        CHECKS = {
            "Completude": ["## Objetivo", "## Quando utilizar", "## Quando NÃO utilizar"],
            "Metadados": ["---", "llm_ready: true", "rag_ready: true", "graph_ready: true"],
            "Exemplos": ["## Exemplos completos", "### curl", "### Python", "### JavaScript"],
            "FAQ": ["## FAQ"],
            "Relacionamentos": ["## Entidades relacionadas", "## Métodos relacionados"],
            "Perguntas naturais": ["## Perguntas naturais"],
            "Business Knowledge": ["Fluxo de negócio", "Casos de uso"],
            "RAG": ["Tags para RAG", "rag_ready: true"],
            "GraphRAG": ["graph_ready: true", "GraphRAG"],
            "Embeddings": ["embedding_version"],
        }


        def score(text: str) -> tuple[int, dict[str, bool]]:
            results = {}
            hits = 0
            total = len(CHECKS)
            for name, needles in CHECKS.items():
                ok = all(needle in text for needle in needles)
                results[name] = ok
                hits += int(ok)
            return round((hits / total) * 100), results


        def main() -> None:
            REPORT.parent.mkdir(parents=True, exist_ok=True)
            lines = ["# Knowledge Score", "", "| Arquivo | Nota | Lacunas |", "| --- | ---: | --- |"]
            for path in DOCS:
                text = path.read_text(encoding="utf-8")
                note, checks = score(text)
                gaps = [name for name, ok in checks.items() if not ok]
                lines.append(f"| `{path.as_posix()}` | {note} | {', '.join(gaps) if gaps else 'Nenhuma'} |")
            REPORT.write_text("\\n".join(lines) + "\\n", encoding="utf-8")
            print(f"Relatorio gerado em {REPORT}")


        if __name__ == "__main__":
            main()
        """
    )


def update_readme() -> None:
    content = dedent(
        """\
        # VerticalParts Knowledge Base

        Base de conhecimento Enterprise RAG/LLM da VerticalParts para documentar APIs, dominios de negocio, grafos de conhecimento, chunks, embeddings, schemas, testes e estrategias de recuperacao.

        ## Arquitetura

        - `docs/`: conhecimento tecnico fonte, com YAML obrigatorio.
        - `standards/`: padroes mestres para documentos LLM-ready.
        - `business/`: conhecimento de negocio por dominio.
        - `graphs/`: relacoes GraphRAG em Mermaid.
        - `rag/`: chunking, retrieval, reranking e estrategias hibridas.
        - `embeddings/`: orientacoes de modelos e versionamento.
        - `schemas/`: contratos JSON iniciais.
        - `datasets/questions/`: perguntas naturais para avaliacao e treinamento.
        - `tests/knowledge/`: testes automatizados de qualidade documental.
        - `scripts/`: automacoes de geracao, score e suporte.
        - `reports/`: saidas geradas por validadores.

        ## Objetivos

        - Criar conhecimento especializado para LLMs, nao apenas documentacao humana.
        - Padronizar metadados para RAG, GraphRAG e embeddings.
        - Separar informacao documentada oficialmente de conteudo que necessita validacao.
        - Evitar credenciais, segredos ou senhas no repositorio.

        ## Primeiro domínio documentado em detalhe

        O primeiro dominio detalhado e `Omie Geral > Clientes, Fornecedores e Transportadoras`, baseado na fonte oficial `https://app.omie.com.br/api/v1/geral/clientes/`.

        ## Estrutura

        Consulte `standards/LLM_DOCUMENT_STANDARD.md` para o formato obrigatorio de Markdown, YAML, FAQ, exemplos, tags, chunking, embeddings, RAG e GraphRAG.

        ## Roadmap

        1. Consolidar ClientesCadastro.
        2. Expandir Financeiro.
        3. Expandir Vendas.
        4. Expandir Servicos.
        5. Expandir Fiscal.
        6. Criar avaliadores automaticos por dominio.

        ## Como contribuir

        - Criar branch por dominio ou padrao.
        - Seguir `standards/LLM_DOCUMENT_STANDARD.md`.
        - Rodar testes e score antes de abrir PR.
        - Marcar lacunas como "Necessita validacao".

        ## Como gerar documentação

        ```bash
        python scripts/generate_enterprise_omie_clientes.py
        ```

        ## Como gerar embeddings

        1. Escolha o modelo em `embeddings/README.md`.
        2. Leia chunks em `rag/chunks/`.
        3. Preserve metadados YAML.
        4. Grave `embedding_version`.

        ## Como indexar no Qdrant

        - Criar colecao por dominio.
        - Usar filtros por `service`, `method`, `domain`, `status` e `embedding_version`.
        - Indexar chunks de `rag/chunks/clientes/`.

        ## Como indexar no pgvector

        - Criar tabela com texto, vetor e metadados JSONB.
        - Usar indices vetoriais e filtros JSONB para dominio e metodo.
        - Registrar hash do chunk para reindexacao incremental.

        ## Como integrar com LangChain

        - Usar loader Markdown.
        - Separar YAML como metadata.
        - Aplicar retriever hibrido e reranker.

        ## Como integrar com LlamaIndex

        - Carregar chunks como nodes.
        - Mapear YAML para metadata.
        - Usar graph store quando consumir `graphs/`.

        ## Como integrar com Semantic Kernel

        - Registrar chunks como memoria semantica.
        - Criar plugins por dominio Omie.
        - Restringir respostas as fontes recuperadas.

        ## Como integrar com Haystack

        - Usar document store vetorial.
        - Aplicar BM25 + embedding retriever.
        - Rerankear por metodo e status.

        ## Qualidade

        ```bash
        pytest tests/knowledge
        python scripts/knowledge_score.py
        ```
        """
    )
    write("README.md", content)


def main() -> None:
    ensure_dirs()
    write("standards/LLM_DOCUMENT_STANDARD.md", standard_doc())
    for meta in METHODS:
        write(f"docs/omie/geral/clientes/{meta['file']}", method_doc(meta))
    write("docs/omie/geral/clientes/README.md", clientes_readme())
    retrofit_docs_omie()
    write("graphs/omie/clientes.graph.md", graph_doc())
    write("business/omie/clientes.md", business_doc())
    questions_dataset()
    chunks()
    write("embeddings/README.md", embeddings_doc())
    write("tests/knowledge/test_knowledge_docs.py", tests_doc())
    write("scripts/knowledge_score.py", score_script())
    update_readme()


if __name__ == "__main__":
    main()
