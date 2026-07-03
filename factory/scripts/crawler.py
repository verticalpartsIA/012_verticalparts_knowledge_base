"""Crawler da Omie Knowledge Factory.

Responsabilidade:
    Futuramente coletar a documentação oficial de um serviço Omie a partir de
    uma URL pública ou autorizada. Nesta fase o crawler NÃO deve executar
    scraping real, chamadas autenticadas ou persistência de conteúdo externo.

Entrada prevista:
    - URL oficial da Omie.
    - Configurações de cache, timeout e política de origem.

Saída prevista:
    - Snapshot bruto versionável apenas quando não houver dados sensíveis.
    - Metadados de coleta: URL, data, hash e status.

Erros previstos:
    - URL indisponível.
    - HTML alterado.
    - Conteúdo incompleto.
    - Fonte não autorizada.

Recuperação:
    - Falhar com mensagem clara.
    - Marcar serviço como "Necessita validação".
    - Não gerar documentos finais se a origem não for confiável.
"""

