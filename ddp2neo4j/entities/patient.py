from neomodel import (StringProperty, ArrayProperty, RelationshipTo)
from ddp2neo4j.entities.hpo import HPONode
from ddp2neo4j.entities.base import BaseNode, BaseEdge


class Patient_HPO_Edge(BaseEdge):
    pass


class PatientNode(BaseNode):
    primary_id = StringProperty(unique_index=True, required=True)

    genes = ArrayProperty(StringProperty())  # should this be a relationship?
    hpos = ArrayProperty(StringProperty())

    has_phenotypes = RelationshipTo(HPONode, 'HAS_PHENOTYPES', model=Patient_HPO_Edge)
