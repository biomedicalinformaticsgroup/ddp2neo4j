from ddp2neo4j.core.parser import OboParser
from ddp2neo4j.core.parser import PatientParser
from ddp2neo4j.repository.hpo_repo import HPOReposity
from ddp2neo4j.repository.patient_repo import PatientReposity
from ddp2neo4j.resources.res import HPO_Resource
from ddp2neo4j.resources.res import Patient_Resource




def test_patient_hpo():
    hpo_terms = OboParser.parse_file(HPO_Resource.file_dev, True)
    HPOReposity.batch_create_from_dict(hpo_terms, batch_size=3)

    patient_records = PatientParser.parse_file(Patient_Resource.file_dev, True)
    PatientReposity.batch_create_from_dict(patient_records, batch_size=1)

    G = PatientReposity.toNextworkX()

    # import networkx as nx
    # G = nx.Graph()
    #
    # processed=[]
    # for node in PatientReposity.allNode():
    #     _create_nx_node(G,node,processed)

    # nodes = {}
    # for node in PatientReposity.allNode():
    #     nodes[node.primary_id] = node
    #     props = node.propertiesToDict()
    #     rels = node.relationsToDict()
    #     # rs = PatientReposity.query_relations(node,HPONode)
    #     print(props)
    #     print(rels)
    #     G.add_node(node.primary_id, **props)
    #     for rel_name, connect_nodes in rels.items():
    #         G.add_edges_from([(node.primary_id, target) for target in connect_nodes])
    print(G)


def test_patient_hpo_full():
    hpo_terms = OboParser.parse_file(HPO_Resource.file, True)
    HPOReposity.batch_create_from_dict(hpo_terms, batch_size=300)

    patient_records = PatientParser.parse_file(Patient_Resource.file, True)
    PatientReposity.batch_create_from_dict(patient_records, batch_size=300)

    # G = PatientReposity.toNextworkX()
