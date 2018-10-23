from neomodel import (StructuredNode, DateTimeProperty, StructuredRel)


class BaseEdge(StructuredRel):
    created = DateTimeProperty(default_now=True)


class BaseNode(StructuredNode):
    neo4j_node_created_date = DateTimeProperty(default_now=True)

    @classmethod
    def inflateFromDict(cls, dict):
        """
        Inflate a raw neo4j_driver node to a neomodel node
        :param node:
        :return: node object
        """
        # support lazy loading
        props = {}
        for key, prop in cls.__all_properties__:
            # map property name from database to object property
            db_property = prop.db_property or key

            if db_property in dict:
                props[key] = prop.inflate(dict[db_property], dict)
            elif prop.has_default:
                props[key] = prop.default_value()
            else:
                props[key] = None

        snode = cls(**props)

        return snode