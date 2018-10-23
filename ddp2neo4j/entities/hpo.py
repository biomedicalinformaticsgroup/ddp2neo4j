from neomodel import (StringProperty, ArrayProperty, BooleanProperty, RelationshipTo)

from ddp2neo4j.entities.base import BaseEdge, BaseNode


class HPOEdge(BaseEdge):
    pass


class HPONode(BaseNode):
    primary_id = StringProperty(unique_index=True, required=True)
    name = StringProperty(index=True, required=True)
    definition = StringProperty()
    comment = StringProperty()
    replaced_by = StringProperty()  # should this be a relationship?
    created_by = StringProperty()
    creation_date = StringProperty()

    alt_id = ArrayProperty(StringProperty())  # should this be a relationship?
    synonym = ArrayProperty(StringProperty())
    xref = ArrayProperty(StringProperty())
    is_a = ArrayProperty(StringProperty(), default=[])  # this is also a relationship
    subset = ArrayProperty(StringProperty())
    consider = ArrayProperty(StringProperty())  # should this be a relationship?

    is_anonymous = BooleanProperty(index=True)
    is_obsolete = BooleanProperty(index=True)

    is_child_of = RelationshipTo('HPONode', 'IS_A', model=HPOEdge)

    # is_parent_of = RelationshipFrom('HPONode', 'IS_PARENT_OF', model=HPOEdge)
