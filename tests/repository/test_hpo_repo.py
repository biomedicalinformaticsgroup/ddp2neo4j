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
    assert len(nodes['HP:0000001'].is_parent_of) == 1
    assert len(nodes['HP:0000001'].is_child_of) == 0

    assert len(nodes['HP:0000005'].is_parent_of) == 2
    assert len(nodes['HP:0000005'].is_child_of) == 1

    for p in nodes['HP:0000005'].is_parent_of.all():
        assert p.primary_id in ['HP:0000007','HP:0000006']









