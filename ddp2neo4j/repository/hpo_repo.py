from neomodel import UniqueProperty

from ddp2neo4j.entities.nodes import HPONode, HPOEdge
from ddp2neo4j.repository.node_repo import Repository


class HPOReposity(Repository):
    NodeEntity = HPONode
    EdgeEntity = HPOEdge

    @classmethod
    def _create_relations(cls):
        super()._create_relations()
        nodes = {}

        for node in cls.allNode():
            nodes[node.primary_id] = node

        for id, node in nodes.items():
            for parent in node.is_a:
                node.is_child_of.connect(nodes[parent])

    @classmethod
    def fetch_largest_connect_compounent(cls):
        cls.NodeEntity.cypher("MATCH (a) WHERE id(a)={self} MATCH (a)-[:FRIEND]->(b) RETURN b")

