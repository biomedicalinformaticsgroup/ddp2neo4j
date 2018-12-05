from neomodel import (StructuredNode, DateTimeProperty, StructuredRel)


class BaseEdge(StructuredRel):
    created = DateTimeProperty(default_now=True)

    def getProperties(self):
        dict = {}
        props = self.defined_properties(aliases=False, rels=False)
        for prop in props:
            dict[prop] = getattr(self, prop)
        return dict

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

    def getProperties(self):
        dict = {}
        props = self.defined_properties(aliases=False, rels=False)
        for prop in props:
            dict[prop] = getattr(self, prop)
        return dict

    def getRelations(self, deep=True):
        dict = {}
        rels = self.defined_properties(aliases=False, properties=False)
        for rel_name, rel in rels.items():
            # print(float(getattr(rel.definition['model'],'weight')))
            if (deep):
                dict[rel_name] = [r for r in getattr(self, rel_name).all()]
            else:
                dict[rel_name] = [r.primary_id for r in getattr(self, rel_name).all()]
        return dict



