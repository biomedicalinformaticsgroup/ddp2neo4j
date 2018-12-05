from ddp2neo4j.entities.base import BaseEdge
from neomodel import FloatProperty


class HPOEdge(BaseEdge):
    pass


class Patient_HPO_Edge(BaseEdge):
    weight = FloatProperty()
    def get_weight(self):
        return self.weight
    pass
