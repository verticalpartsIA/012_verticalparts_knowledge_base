from pathlib import Path
import yaml

ONTOLOGY = Path("ontology/verticalparts")
SEMANTIC = Path("semantic/verticalparts")


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_ontology_files_exist():
    for filename in [
        "MASTER_ONTOLOGY.md", "README.md", "ENTITY_MODEL.md", "RELATIONSHIP_MODEL.md",
        "EVENT_MODEL.md", "STATE_MODEL.md", "VALUE_OBJECTS.md", "BUSINESS_CAPABILITIES.md",
        "entities.yaml", "relationships.yaml", "business_terms.yaml", "events.yaml", "kpis.yaml", "states.yaml",
    ]:
        assert (ONTOLOGY / filename).is_file(), filename


def test_entities_are_unique_and_have_unique_aliases():
    data = load_yaml(ONTOLOGY / "entities.yaml")
    entities = data["entities"]
    names = [item["name"] for item in entities]
    assert len(names) == len(set(names))
    aliases = []
    for item in entities:
        aliases.extend(item.get("aliases", []))
        aliases.extend(item.get("abbreviations", []))
        assert item.get("synonyms")
        assert item.get("primary_attributes")
        assert item.get("department")
    assert len(aliases) == len(set(aliases))


def test_relationships_reference_valid_entities():
    entity_names = {item["name"] for item in load_yaml(ONTOLOGY / "entities.yaml")["entities"]}
    relationships = load_yaml(ONTOLOGY / "relationships.yaml")["relationships"]
    assert relationships
    for rel in relationships:
        assert rel["from"] in entity_names
        assert rel["to"] in entity_names
        assert rel["type"]


def test_states_are_valid_and_non_empty():
    entity_names = {item["name"] for item in load_yaml(ONTOLOGY / "entities.yaml")["entities"]}
    machines = load_yaml(ONTOLOGY / "states.yaml")["state_machines"]
    assert machines
    for machine in machines:
        assert machine["entity"] in entity_names or machine["entity"] == "Compra"
        assert len(machine["states"]) >= 3
        assert len(machine["states"]) == len(set(machine["states"]))


def test_semantic_files_point_to_ontology():
    for filename in ["business_dictionary.yaml", "aliases.yaml", "synonyms.yaml", "intent_catalog.yaml", "business_taxonomy.yaml"]:
        data = load_yaml(SEMANTIC / filename)
        assert data["ontology_source"] == "ontology/verticalparts/entities.yaml"
