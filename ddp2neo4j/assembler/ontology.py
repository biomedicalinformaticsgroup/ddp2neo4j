from ddp2neo4j.entities.ontology import OntologyNode as e_node
from ddp2neo4j.core.ontology import Ontology as c_node


class OntologyAssembler(object):
    def __init__(self,c_node,e_node):
        raise NotImplementedError('Need tpytho implement in subclass')
