"""Gera documentacao Enterprise LLM/RAG para Omie Contas a Receber."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from textwrap import dedent


TODAY = date.today().isoformat()
SOURCE = "https://app.omie.com.br/api/v1/financas/contareceber/"
ROOT = Path(".")


METHODS = [
    ("alterar_conta_receber.md", "AlterarContaReceber", "alteracao", "conta_receber_cadastro", "conta_receber_cadastro_response", "Altera uma conta a receber ja cadastrada."),
    ("alterar_distribuicao_departamento.md", "AlterarDistribuicaoDepartamento", "alteracao_rateio_departamento", "rateio_cadastro", "conta_receber_cadastro_chave", "Altera a distribuicao por departamento de uma conta a receber."),
    ("cancelar_conta_receber.md", "CancelarContaReceber", "cancelamento_boleto", "conta_receber_cadastro_chave", "conta_receber_cadastro_response", "Cancela o boleto gerado de uma conta a receber."),
    ("cancelar_recebimento.md", "CancelarRecebimento", "cancelamento_recebimento", "conta_receber_cancelar_recebimento", "conta_receber_cancelar_recebimento_resposta", "Cancela uma baixa de recebimento de contas a receber."),
    ("conciliar_recebimento.md", "ConciliarRecebimento", "conciliacao", "conta_receber_conciliar_request", "conta_receber_conciliar_response", "Realiza a conciliacao do recebimento."),
    ("consultar_conta_receber.md", "ConsultarContaReceber", "consulta", "lcrChave", "conta_receber_cadastro", "Consulta uma conta a receber por chave."),
    ("desconciliar_recebimento.md", "DesconciliarRecebimento", "desconciliacao", "conta_receber_conciliar_request", "conta_receber_conciliar_response", "Desconcilia um recebimento previamente conciliado."),
    ("excluir_conta_receber.md", "ExcluirContaReceber", "exclusao", "conta_receber_cadastro_chave", "conta_receber_cadastro_response", "Exclui uma conta a receber."),
    ("excluir_distribuicao_departamento.md", "ExcluirDistribuicaoDepartamento", "exclusao_rateio_departamento", "conta_receber_cadastro_chave", "conta_receber_cadastro_response", "Exclui a distribuicao por departamento de uma conta a receber."),
    ("incluir_conta_receber.md", "IncluirContaReceber", "inclusao", "conta_receber_cadastro", "conta_receber_cadastro_response", "Inclui uma nova conta a receber."),
    ("incluir_conta_receber_por_lote.md", "IncluirContaReceberPorLote", "inclusao_lote", "conta_receber_lote", "conta_receber_lote_response", "Inclui contas a receber por lote."),
    ("incluir_distribuicao_departamento.md", "IncluirDistribuicaoDepartamento", "inclusao_rateio_departamento", "rateio_cadastro", "conta_receber_cadastro_chave", "Inclui distribuicao por departamento em uma conta a receber."),
    ("lancar_recebimento.md", "LancarRecebimento", "baixa_recebimento", "conta_receber_lancar_recebimento", "conta_receber_lancar_recebimento_resposta", "Lanca a baixa/recebimento de uma conta a receber."),
    ("listar_contas_receber.md", "ListarContasReceber", "listagem", "lcrListarRequest", "lcrListarResponse", "Lista contas a receber cadastradas."),
    ("upsert_conta_receber.md", "UpsertContaReceber", "upsert", "conta_receber_cadastro", "conta_receber_cadastro_response", "Inclui ou altera uma conta a receber conforme chave informada."),
    ("upsert_conta_receber_por_lote.md", "UpsertContaReceberPorLote", "upsert_lote", "conta_receber_lote", "conta_receber_lote_response", "Inclui ou altera contas a receber por lote."),
]


RELATED_ENTITIES = [
    "Cliente",
    "Pedido de Venda",
    "Ordem de Serviço",
    "NF-e",
    "NFS-e",
    "Categorias",
    "Bancos",
    "Movimentos Financeiros",
]


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    normalized = re.sub(r"(?m)^ {8}", "", content.strip())
    normalized = re.sub(r"(?m)^[ \t]+(#{1,6}\s)", r"\1", normalized)
    normalized = re.sub(r"(?m)^[ \t]+(```)", r"\1", normalized)
    normalized = re.sub(r"(?m)^[ \t]+(>)", r"\1", normalized)
    target.write_text(normalized + "\n", encoding="utf-8")


def method_slug(method: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", method).lower()


def method_meta(item: tuple[str, str, str, str, str, str]) -> dict:
    file, method, operation, request_type, response_type, summary = item
    return {
        "file": file,
        "method": method,
        "operation": operation,
        "request_type": request_type,
        "response_type": response_type,
        "summary": summary,
        "slug": method_slug(method),
    }


METAS = [method_meta(item) for item in METHODS]


def yaml_for(meta: dict) -> str:
    lines = [
        "---",
        f'title: "{meta["method"]} - Omie Financeiro Contas a Receber"',
        'service: "LancamentoContaReceber"',
        'domain: "omie.financeiro"',
        'resource: "contas_a_receber"',
        f'method: "{meta["method"]}"',
        f'endpoint: "{SOURCE}"',
        'http_method: "POST"',
        'version: "1"',
        'entity: "conta_a_receber"',
        "related_entities:",
    ]
    lines.extend(f"  - {entity}" for entity in RELATED_ENTITIES)
    lines.extend(
        [
            "related_methods:",
            "  - ConsultarContaReceber",
            "  - IncluirContaReceber",
            "  - AlterarContaReceber",
            "  - ListarContasReceber",
            "permissions:",
            '  - "Necessita credenciais Omie validas fora do repositorio"',
            '  - "Nao documentar chaves, segredos ou senhas"',
            'complexity: "media"',
            'status: "Documentado oficialmente / Necessita validação em integração"',
            f'source: "{SOURCE}"',
            f'last_review: "{TODAY}"',
            "tags:",
            "  - omie",
            "  - financeiro",
            "  - contas-a-receber",
            f"  - {meta['operation']}",
            "  - enterprise-rag",
            "keywords:",
            "  - LancamentoContaReceber",
            f"  - {meta['method']}",
            "  - Contas a Receber",
            "  - RAG",
            "questions:",
            f'  - "Como usar {meta["method"]}?"',
            '  - "Como documentar Contas a Receber para LLM?"',
            '  - "Quais campos necessitam validação?"',
            "use_cases:",
            "  - conciliacao_financeira",
            "  - baixa_recebimento",
            "  - sincronizacao_financeira",
            "  - assistente_llm",
            'business_area: "ERP / Financeiro / Contas a Receber"',
            "llm_ready: true",
            "rag_ready: true",
            "graph_ready: true",
            "embedding_version: 1",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def sample_param(request_type: str) -> dict:
    if request_type == "conta_receber_cadastro":
        return {
            "codigo_lancamento_integracao": "CR-FICTICIO-001",
            "codigo_cliente_fornecedor": 123456,
            "data_vencimento": "31/12/2026",
            "valor_documento": 100.0,
            "codigo_categoria": "1.01.02",
            "data_previsao": "31/12/2026",
            "id_conta_corrente": 987654,
        }
    if request_type in {"conta_receber_cadastro_chave", "lcrChave"}:
        return {"codigo_lancamento_omie": 123456789, "codigo_lancamento_integracao": "CR-FICTICIO-001"}
    if request_type == "lcrListarRequest":
        return {"pagina": 1, "registros_por_pagina": 50, "apenas_importado_api": "N"}
    if request_type == "conta_receber_lote":
        return {"lote": 100, "conta_receber_cadastro": [sample_param("conta_receber_cadastro")]}
    if request_type == "rateio_cadastro":
        return {"codigo_lancamento_omie": 123456789, "distribuicao": [{"cCodDep": "DEP-FICTICIO", "nPerDep": 100.0}]}
    if request_type == "conta_receber_lancar_recebimento":
        return {"codigo_lancamento": 123456789, "codigo_conta_corrente": 987654, "valor": 100.0, "data": "31/12/2026", "observacao": "Baixa ficticia"}
    if request_type == "conta_receber_cancelar_recebimento":
        return {"codigo_baixa": 123456789}
    if request_type == "conta_receber_conciliar_request":
        return {"codigo_baixa": 123456789}
    return {"referencia_ficticia": "Necessita validação"}


def examples(meta: dict) -> str:
    payload = {"call": meta["method"], "param": [sample_param(meta["request_type"])]}
    json_text = json.dumps(payload, indent=2, ensure_ascii=False)
    compact = json.dumps(payload, ensure_ascii=False)
    return dedent(
        f"""\
        > Exemplos fictícios. Credenciais Omie foram omitidas de propósito.

        ### JSON base

        ```json
        {json_text}
        ```

        ### curl

        ```bash
        curl -X POST "{SOURCE}" -H "Content-Type: application/json" -d '{compact}'
        ```

        ### Python

        ```python
        import requests

        payload = {repr(payload)}
        response = requests.post("{SOURCE}", json=payload, timeout=30)
        print(response.json())
        ```

        ### JavaScript

        ```javascript
        const payload = {json_text};
        const response = await fetch("{SOURCE}", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify(payload)
        }});
        console.log(await response.json());
        ```

        ### TypeScript

        ```typescript
        type OmieRequest = {{ call: string; param: Array<Record<string, unknown>> }};
        const payload: OmieRequest = {json_text};
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
        $payload = {compact};
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
        var payload = new {{ call = "{meta['method']}", param = new object[] {{ new {{ codigo_lancamento_integracao = "CR-FICTICIO-001" }} }} }};
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
            .POST(java.net.http.HttpRequest.BodyPublishers.ofString(\"\"\"{json_text}\"\"\"))
            .build();
        var response = client.send(request, java.net.http.HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
        ```

        ### Delphi

        ```pascal
        // Exemplo ficticio: enviar POST para o endpoint oficial com call="{meta['method']}".
        ```

        ### n8n

        ```json
        {{
          "node": "HTTP Request",
          "method": "POST",
          "url": "{SOURCE}",
          "sendBody": true,
          "bodyContentType": "json",
          "jsonBody": {compact}
        }}
        ```
        """
    )


FAQ = [
    "Como usar este método?",
    "Quando uma LLM deve escolher este método?",
    "Qual endpoint oficial deve ser citado?",
    "Qual entidade principal é manipulada?",
    "Como este método se relaciona com clientes?",
    "Como este método se relaciona com pedidos de venda?",
    "Como este método se relaciona com ordem de serviço?",
    "Como este método se relaciona com NF-e?",
    "Como este método se relaciona com NFS-e?",
    "Como este método se relaciona com categorias?",
    "Como este método se relaciona com bancos?",
    "Como este método se relaciona com movimentos financeiros?",
    "Quais campos precisam de validação?",
    "O exemplo é oficial?",
    "Como tratar código de lançamento Omie?",
    "Como tratar código de integração?",
    "Como tratar valor do documento?",
    "Como resolver campo obrigatório ausente?",
    "Como resolver lançamento não encontrado?",
    "Este método está pronto para produção?",
]


def faq(meta: dict) -> str:
    answer = (
        f"O método `{meta['method']}` é documentado oficialmente na página do serviço LancamentoContaReceber. "
        "Detalhes operacionais, obrigatoriedade condicional e comportamento em produção necessitam validação em ambiente autorizado. "
        "Os exemplos deste repositório são fictícios."
    )
    return "\n\n".join(f"### {i}. {q}\n\n{answer}" for i, q in enumerate(FAQ, 1))


def method_doc(meta: dict) -> str:
    required = {
        "conta_receber_cadastro": ["codigo_cliente_fornecedor", "data_vencimento", "valor_documento", "codigo_categoria", "data_previsao", "id_conta_corrente"],
        "lcrListarRequest": ["pagina", "registros_por_pagina"],
        "conta_receber_cadastro_chave": ["codigo_lancamento_omie ou codigo_lancamento_integracao"],
        "lcrChave": ["codigo_lancamento_omie ou codigo_lancamento_integracao"],
        "conta_receber_lote": ["lote", "conta_receber_cadastro"],
        "rateio_cadastro": ["chave do lançamento", "distribuição por departamento"],
        "conta_receber_lancar_recebimento": ["codigo_lancamento", "codigo_conta_corrente", "valor", "data"],
        "conta_receber_cancelar_recebimento": ["codigo_baixa"],
        "conta_receber_conciliar_request": ["codigo_baixa"],
    }.get(meta["request_type"], ["Necessita validação"])
    required_md = "\n".join(f"- `{field}`" for field in required)
    related_methods = "\n".join(f"- `{m['method']}`" for m in METAS if m["method"] != meta["method"] and m["operation"].split("_")[0] in meta["operation"])
    if not related_methods:
        related_methods = "- `ConsultarContaReceber`\n- `ListarContasReceber`\n- `IncluirContaReceber`"
    body = dedent(
        f"""\
        # {meta['method']}

        ## Objetivo

        {meta['summary']} O conteúdo é preparado para LLMs, RAG e GraphRAG, com separação clara entre "Documentado oficialmente" e "Necessita validação".

        ## Quando utilizar

        Utilize quando a intenção do usuário estiver ligada à operação `{meta['operation']}` em contas a receber do Omie.

        ## Quando NÃO utilizar

        Não utilize para contas a pagar, movimentos financeiros genéricos, cadastro de clientes ou pedidos de venda. Nesses casos, a LLM deve direcionar para o domínio correto.

        ## Fluxo de negócio

        1. Identificar o cliente ou origem do título.
        2. Relacionar o título com pedido, ordem de serviço, NF-e, NFS-e ou lançamento manual quando aplicável.
        3. Aplicar categoria financeira, conta corrente/banco e datas.
        4. Executar a operação `{meta['method']}` com payload fictício em exemplos ou dados autorizados em produção.
        5. Interpretar retorno, status e relação com movimentos financeiros.

        ## Entidades relacionadas

        - Cliente
        - Pedidos de Venda
        - Ordem de Serviço
        - NF-e
        - NFS-e
        - Categorias
        - Bancos
        - Movimentos Financeiros

        ## Métodos relacionados

        {related_methods}

        ## Pré-requisitos

        - Credenciais Omie válidas fora do repositório.
        - Cliente/fornecedor cadastrado quando o título exigir vínculo.
        - Categoria financeira validada.
        - Conta corrente/banco validado para baixa, conciliação ou previsão.
        - Fonte oficial consultada antes de produção.

        ## Payload

        - Tipo oficial de entrada: `{meta['request_type']}`.
        - Tipo oficial de retorno: `{meta['response_type']}`.
        - Endpoint oficial: `{SOURCE}`.

        ## Campos obrigatórios

        {required_md}

        ## Campos opcionais

        - `numero_documento`
        - `numero_documento_fiscal`
        - `numero_pedido`
        - `chave_nfe`
        - `observacao`
        - `codigo_projeto`
        - `categorias`
        - `distribuicao`
        - `nCodPedido`
        - `nCodOS`
        - Campos adicionais devem ser tratados como "Necessita validação" quando não houver confirmação no fluxo.

        ## Regras de negócio

        - Contas a receber representam direitos financeiros a receber de clientes ou fontes operacionais.
        - Podem nascer de pedido de venda, ordem de serviço, NF-e, NFS-e ou lançamento manual.
        - Categorias e bancos influenciam relatórios, conciliação, baixa e movimentos financeiros.
        - Baixa e conciliação devem preservar rastreabilidade financeira.

        ## Validações

        - Validar cliente antes de criar título.
        - Validar vencimento, previsão e valor.
        - Validar categoria e conta corrente.
        - Validar relação com NF-e/NFS-e quando houver documento fiscal.
        - Validar se o lançamento pode ser alterado, excluído, baixado ou conciliado.

        ## Restrições

        - Não armazenar `app_key`, `app_secret`, token, senha ou bearer.
        - Não usar dados reais em exemplos.
        - Não assumir regra fiscal sem validação.
        - Não confundir contas a receber com movimentos financeiros já efetivados.

        ## Resposta esperada

        Retorno oficial: `{meta['response_type']}`. A interpretação de códigos e mensagens deve ser validada em integração.

        ## Erros comuns

        - Cliente inexistente.
        - Categoria inválida.
        - Conta corrente inexistente.
        - Valor ou data ausente.
        - Baixa já realizada.
        - Tentativa de conciliar sem baixa válida.

        ## Como resolver os erros

        - Consultar o título antes da operação.
        - Validar cliente, categoria e banco.
        - Conferir se há baixa ou conciliação anterior.
        - Revisar campos obrigatórios do tipo `{meta['request_type']}`.
        - Marcar lacunas como "Necessita validação".

        ## Casos de uso

        - Assistente financeiro respondendo dúvidas sobre títulos a receber.
        - Integração entre vendas, serviços e financeiro.
        - Sincronização de contas a receber para BI financeiro.
        - Auditoria de baixas, conciliações e vínculos fiscais.
        - GraphRAG conectando clientes, pedidos, documentos fiscais e movimentos.

        ## Exemplos completos

        {examples(meta)}

        ## FAQ

        {faq(meta)}

        ## Perguntas naturais

        - Como escolher `{meta['method']}`?
        - Como relacionar uma conta a receber a um cliente?
        - Como relacionar uma conta a receber a pedido de venda?
        - Como saber se preciso consultar, listar, baixar ou conciliar?
        - Quais campos ainda necessitam validação?

        ## Tags para RAG

        - omie
        - financeiro
        - contas-a-receber
        - {meta['operation']}
        - enterprise-rag
        - graphrag

        ## Fonte oficial consultada

        - {SOURCE}
        """
    )
    return yaml_for(meta) + body


def readme_doc() -> str:
    methods = "\n".join(f"- `{m['method']}`: {m['summary']}" for m in METAS)
    return yaml_for(METAS[13]) + dedent(
        f"""\
        # Omie Financeiro: Contas a Receber

        ## Objetivo

        Documentar o serviço `LancamentoContaReceber` como base Enterprise LLM/RAG para títulos a receber.

        ## Quando utilizar

        Use este índice para escolher o método correto de consulta, inclusão, alteração, exclusão, baixa, conciliação, lote ou rateio por departamento.

        ## Quando NÃO utilizar

        Não utilize como contrato final de payload; use o arquivo do método específico.

        ## Fluxo de negócio

        Contas a receber conectam clientes, pedidos de venda, ordens de serviço, NF-e, NFS-e, categorias, bancos e movimentos financeiros.

        ## Casos de uso

        - Escolha de método por uma LLM financeira.
        - Recuperação RAG de contratos de payload.
        - Expansão GraphRAG para clientes, pedidos, documentos fiscais, bancos e movimentos.
        - Triagem de dúvidas sobre baixa, conciliação e listagem.

        ## Entidades relacionadas

        - Cliente
        - Pedidos de Venda
        - Ordem de Serviço
        - NF-e
        - NFS-e
        - Categorias
        - Bancos
        - Movimentos Financeiros

        ## Métodos relacionados

        {methods}

        ## Exemplos completos

        Consulte os arquivos de método para payloads completos. Este índice mantém apenas referências fictícias.

        ### curl

        Exemplo omitido no índice; consulte o método específico.

        ### Python

        Exemplo omitido no índice; consulte o método específico.

        ### JavaScript

        Exemplo omitido no índice; consulte o método específico.

        ## FAQ

        ### 1. O que é Contas a Receber no Omie?

        É o domínio financeiro de títulos a receber, baixas, conciliações e vínculos com clientes e documentos.

        ### 2. A documentação está pronta para LLM?

        Sim, os métodos desta pasta estão marcados como `llm_ready: true` e `rag_ready: true`.

        ## Perguntas naturais

        - Como listar contas a receber?
        - Como baixar um recebimento?
        - Como conciliar uma baixa?

        ## Tags para RAG

        - omie
        - financeiro
        - contas-a-receber
        - enterprise-rag

        ## GraphRAG

        Consulte `graphs/omie/contas_a_receber.graph.md` para relações entre contas a receber, clientes, pedidos, ordens de serviço, NF-e, NFS-e, bancos, categorias e movimentos financeiros.

        ## Fonte oficial consultada

        - {SOURCE}
        """
    )


def business_doc() -> str:
    return dedent(
        f"""\
        # Business Knowledge: Omie Contas a Receber

        ## Como funciona no ERP

        Contas a receber representam direitos financeiros da empresa contra clientes ou outros pagadores. No Omie, o serviço `LancamentoContaReceber` documenta operações para criar, alterar, consultar, listar, excluir, baixar, cancelar baixa, conciliar e ratear títulos.

        ## Relações principais

        - Clientes: identificam o devedor do título.
        - Pedidos de Venda: podem originar parcelas a receber.
        - Ordem de Serviço: pode originar cobrança de serviço.
        - NF-e e NFS-e: documentos fiscais podem gerar ou referenciar títulos.
        - Categorias: classificam receitas.
        - Bancos: representam conta corrente usada em previsão, baixa ou conciliação.
        - Movimentos Financeiros: refletem eventos efetivados de baixa, conciliação e movimentação.

        ## Regras para LLM

        A LLM deve distinguir título a receber de movimento financeiro. O título representa obrigação a receber; o movimento representa evento financeiro efetivado ou conciliado.

        ## Fonte oficial

        - {SOURCE}
        """
    )


def graph_doc() -> str:
    return dedent(
        """\
        # GraphRAG: Omie Contas a Receber

        ```mermaid
        graph TD
          Cliente["Cliente"] --> ContaReceber["Conta a Receber"]
          PedidoVenda["Pedido de Venda"] --> ContaReceber
          OrdemServico["Ordem de Serviço"] --> ContaReceber
          NFe["NF-e"] --> ContaReceber
          NFSe["NFS-e"] --> ContaReceber
          ContaReceber --> Categorias["Categorias"]
          ContaReceber --> Bancos["Bancos / Conta Corrente"]
          ContaReceber --> Movimentos["Movimentos Financeiros"]
          ContaReceber --> Baixa["Baixa / Recebimento"]
          Baixa --> Conciliacao["Conciliação"]
          Categorias --> Relatorios["Relatórios Financeiros"]
          Bancos --> Conciliacao
        ```

        ## Uso por LLM

        Use este grafo para expandir perguntas que mencionem recebíveis, baixa, conciliação, cliente, pedido, nota fiscal, banco ou categoria.
        """
    )


def questions_dataset() -> None:
    intents = ["consultar", "listar", "incluir", "alterar", "baixar", "cancelar", "conciliar", "desconciliar", "excluir", "sincronizar"]
    targets = ["conta a receber", "título", "recebimento", "baixa", "parcela", "lançamento"]
    fields = ["cliente", "pedido de venda", "ordem de serviço", "NF-e", "NFS-e", "categoria", "banco", "código Omie", "código de integração", "vencimento"]
    templates = [
        "Como {intent} {target} por {field}?",
        "Qual método Omie uso para {intent} {target} relacionado a {field}?",
        "Como uma LLM deve explicar {intent} {target} quando o usuário informa {field}?",
        "O que preciso validar para {intent} {target} com {field}?",
        "Como localizar {target} usando {field} antes de {intent}?",
    ]
    items = []
    seen = set()
    for template in templates:
        for intent in intents:
            for target in targets:
                for field in fields:
                    q = template.format(intent=intent, target=target, field=field)
                    if q in seen:
                        continue
                    seen.add(q)
                    items.append({"question": q, "domain": "omie.financeiro", "resource": "contas_a_receber", "expected_source": SOURCE, "status": "Documentado oficialmente / Necessita validação quando depender de regra condicional"})
                    if len(items) == 300:
                        write("datasets/questions/contas_a_receber.json", json.dumps(items, indent=2, ensure_ascii=False))
                        return


def chunks() -> None:
    index = []
    focuses = ["identidade", "contrato", "operacao", "faq"]
    for meta in METAS:
        for focus in focuses:
            path = f"rag/chunks/contas_a_receber/{meta['slug']}.{focus}.chunk.md"
            content = dedent(
                f"""\
                ---
                source_path: "docs/omie/financeiro/contas_a_receber/{meta['file']}"
                chunk_id: "{meta['method']}.{focus}"
                service: "LancamentoContaReceber"
                method: "{meta['method']}"
                endpoint: "{SOURCE}"
                focus: "{focus}"
                status: "Documentado oficialmente / Necessita validação em integração"
                embedding_version: 1
                ---

                # Chunk {meta['method']} - {focus}

                Este chunk descreve o método `{meta['method']}` do serviço `LancamentoContaReceber` para recuperação RAG. Entrada oficial: `{meta['request_type']}`. Retorno oficial: `{meta['response_type']}`. Operação: `{meta['operation']}`.

                Contas a receber conectam cliente, pedido de venda, ordem de serviço, NF-e, NFS-e, categorias, bancos e movimentos financeiros. A LLM deve usar esse contexto para separar título financeiro, baixa, conciliação e movimento efetivado. Quando a pergunta mencionar vencimento, valor, categoria, conta corrente, pedido, ordem de serviço ou nota fiscal, este chunk pode ser recuperado junto do documento de método.

                Critério de resposta: declarar que o método é documentado oficialmente na fonte Omie e marcar comportamento operacional, obrigatoriedade condicional e regras fiscais como "Necessita validação" quando não houver contrato específico validado. Exemplos são fictícios e não incluem credenciais.

                Estratégia híbrida: usar busca lexical por `{meta['method']}`, `{meta['request_type']}`, código de lançamento, código de integração, baixa, conciliação, categoria e banco; combinar com busca vetorial por intenção de negócio. Reranking deve priorizar método exato, entidade conta a receber, status documentado oficialmente e compatibilidade com a operação solicitada.

                GraphRAG: expandir vizinhos Cliente, Pedido de Venda, Ordem de Serviço, NF-e, NFS-e, Categorias, Bancos e Movimentos Financeiros. Para perguntas de baixa e conciliação, expandir também para recebimento, conta corrente e movimento financeiro.

                Validações importantes: confirmar cliente, categoria, conta corrente, data de vencimento, valor do documento, estado de baixa e estado de conciliação. Não recomendar exclusão, alteração, cancelamento ou baixa sem checar o estado atual do título.

                Contexto de negócio adicional: contas a receber são registros financeiros que normalmente representam expectativa de entrada de caixa. Uma pergunta pode chegar com vocabulário de cobrança, parcela, boleto, título, recebível, faturamento, nota, cliente, baixa ou conciliação. A recuperação deve manter todos esses termos próximos do método para reduzir risco de resposta fora do domínio. Quando o usuário mencionar pedido de venda ou ordem de serviço, a LLM deve explicar que o título pode ter vínculo operacional, mas o vínculo exato precisa ser validado no payload e no ambiente Omie. Quando o usuário mencionar NF-e ou NFS-e, a resposta deve separar documento fiscal de título financeiro. Quando mencionar banco, conta corrente ou conciliação, a resposta deve priorizar métodos de baixa, conciliação ou consulta de estado. Quando mencionar categoria, a resposta deve orientar classificação financeira e rateio como pontos de validação. Esse contexto melhora embeddings, reranking e GraphRAG sem substituir a fonte oficial.
                """
            )
            write(path, content)
            index.append({"chunk": path, "source": f"docs/omie/financeiro/contas_a_receber/{meta['file']}", "method": meta["method"], "focus": focus})
    write("rag/chunks/contas_a_receber/index.json", json.dumps(index, indent=2, ensure_ascii=False))
    write("rag/chunks/contas_a_receber/retrieval_strategy.md", "# Estratégia de Recuperação: Contas a Receber\n\nCombinar busca vetorial, busca lexical, filtros por método, operação e status, reranking por intenção financeira e expansão GraphRAG por cliente, pedido, OS, NF-e, NFS-e, categorias, bancos e movimentos financeiros.\n")


def schemas() -> None:
    schema_dir = Path("schemas/omie/financeiro/contas_a_receber")
    schema_dir.mkdir(parents=True, exist_ok=True)
    for meta in [m for m in METAS if m["method"] in {"ConsultarContaReceber", "IncluirContaReceber", "AlterarContaReceber", "ListarContasReceber", "LancarRecebimento", "CancelarRecebimento"}]:
        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": f"https://verticalparts.local/schemas/omie/financeiro/contas_a_receber/{meta['slug']}.schema.json",
            "title": meta["method"],
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "call": {"const": meta["method"]},
                "param": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": True}},
            },
            "required": ["call", "param"],
        }
        write(str(schema_dir / f"{meta['slug']}.schema.json"), json.dumps(schema, indent=2, ensure_ascii=False))


def update_index_and_readme() -> None:
    write("docs/omie/financeiro/contas_a_receber/README.md", readme_doc())
    write("docs/omie/financeiro/contas_a_receber.md", readme_doc())
    readme = Path("README.md").read_text(encoding="utf-8")
    marker = "## Domínios documentados em detalhe"
    section = dedent(
        """\
        ## Domínios documentados em detalhe

        - Omie Geral > Clientes, Fornecedores e Transportadoras.
        - Omie Financeiro > Contas a Receber.
        """
    )
    if marker not in readme:
        readme = readme.replace("## Estrutura\n", section + "\n## Estrutura\n")
    elif "Omie Financeiro > Contas a Receber" not in readme:
        readme = readme.replace(marker, section.strip())
    write("README.md", readme)


def main() -> None:
    for meta in METAS:
        write(f"docs/omie/financeiro/contas_a_receber/{meta['file']}", method_doc(meta))
    update_index_and_readme()
    write("business/omie/contas_a_receber.md", business_doc())
    write("graphs/omie/contas_a_receber.graph.md", graph_doc())
    questions_dataset()
    chunks()
    schemas()


if __name__ == "__main__":
    main()
