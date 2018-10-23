from ddp2neo4j.resources.res import HPO_Resource
from ddp2neo4j.core.parser import OboParser
from ddp2neo4j.repository.hpo_repo import HPOReposity

def test_create_nodes_from_networkX():
    hpos = OboParser.parse_file(HPO_Resource.file_dev,True)
    HPOReposity.batch_create_from_dict(hpos,batch_size=2)

    nodes={}
    for n in HPOReposity.allNode():
        assert n.id
        nodes[n.primary_id]=n

    assert len(nodes) == 4




