from neomodel import (StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom, ArrayProperty,
                      DateTimeProperty, StructuredRel, FloatProperty)


class Node(StructuredNode):
    pass


class Edge(StructuredRel):
    pass


class OntologyEdge(StructuredRel):
    weight = FloatProperty()
    created = DateTimeProperty(default_now=True)


class OntologyNode(Node):
    uid = UniqueIdProperty()
    term_id = StringProperty(unique_index=True, required=True)
    term_name = StringProperty(index=True, required=True)
    alt_id = ArrayProperty(StringProperty(), required=False)
    definition = StringProperty(required=False,default='')
    synonym = ArrayProperty(StringProperty(), required=False)
    xref = ArrayProperty(StringProperty(), required=False)
    is_a = ArrayProperty(StringProperty(), required=False)
    created = DateTimeProperty(default_now=True)

    parents = RelationshipTo('OntologyNode', 'IS_A', model=OntologyEdge)
    children = RelationshipFrom('OntologyNode', 'IS_A', model=OntologyEdge)
