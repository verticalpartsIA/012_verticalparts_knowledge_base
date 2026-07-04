from pathlib import Path

ROOT = Path("business/verticalparts")
DOMAINS = [
    "01_comercial", "02_engenharia", "03_compras", "04_pcp", "05_almoxarifado", "06_logistica",
    "07_instalacao", "08_assistencia", "09_financeiro", "10_fiscal", "11_rh", "12_juridico",
    "13_crm", "14_qualidade", "15_bi", "16_wms", "17_erp", "18_ai_agents",
]
DOMAIN_FILES = [
    "README.md", "OVERVIEW.md", "BUSINESS_OBJECTS.md", "BUSINESS_RULES.md", "KPIS.md",
    "CHECKLIST.md", "RISKS.md", "FAQ.md", "GLOSSARY.md",
]


def test_verticalparts_root_structure_exists():
    for filename in ["README.md", "ARCHITECTURE.md", "DOMAIN_MODEL.md", "BUSINESS_RULES.md", "GLOSSARY.md", "ROADMAP.md"]:
        assert (ROOT / filename).is_file()


def test_verticalparts_domains_have_required_files():
    for domain in DOMAINS:
        for filename in DOMAIN_FILES:
            path = ROOT / domain / filename
            assert path.is_file(), path
            text = path.read_text(encoding="utf-8")
            assert "Aguardando modelagem da VerticalParts" in text or "Será preenchido posteriormente" in text


def test_verticalparts_company_process_graph_ontology_semantic_exists():
    for filename in ["company_structure.md", "organization.md", "business_units.md", "departments.md"]:
        assert (ROOT / "company" / filename).is_file()
    for filename in ["lead_to_cash.md", "procure_to_pay.md", "project_to_installation.md", "maintenance_lifecycle.md", "customer_support.md", "engineering_workflow.md", "inventory_lifecycle.md"]:
        assert (ROOT / "processes" / filename).is_file()
    for filename in ["lead_to_cash.graph.md", "procure_to_pay.graph.md", "project_installation.graph.md", "maintenance.graph.md", "organization.graph.md"]:
        assert (Path("graphs/verticalparts") / filename).is_file()
    for filename in ["entities.yaml", "relationships.yaml", "business_terms.yaml", "events.yaml", "kpis.yaml", "states.yaml"]:
        assert (Path("ontology/verticalparts") / filename).is_file()
    for filename in ["business_taxonomy.yaml", "business_dictionary.yaml", "aliases.yaml", "synonyms.yaml", "intent_catalog.yaml"]:
        assert (Path("semantic/verticalparts") / filename).is_file()
