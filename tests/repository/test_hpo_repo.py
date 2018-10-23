from ddp2neo4j.resources.res import HPO_Resource
from ddp2neo4j.core.parser import OboParser
from ddp2neo4j.repository.hpo_repo import HPOReposity

def test_create_nodes_from_networkX():
    g = OboParser.parse_file(HPO_Resource.file_dev)
    HPOReposity.create_nodes_from_networkX(g)

    nodes={}
    for n in HPOReposity.allNode():
        assert n.id
        nodes[n.term_id]=n

    assert len(nodes) == 4




