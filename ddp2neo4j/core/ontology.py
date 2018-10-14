import networkx
from pkg_resources import resource_filename


class Ontology(object):
    def __init__(self):
        pass


class HPO(Ontology):
    ontology_name = "Human Phenotype Ontology"
    url = 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo'
    file = resource_filename('ddp2neo4j.resources.obo', 'hpo.obo')

    def __init__(self, graph):
        self.graph = graph

    def _ont_statistic(self):
        stat = "number of node: {}\n" \
               "number of edges: {}\n" \
               "is_directed_acyclic_graph: {}\n".format(len(self.graph), self.graph.number_of_edges(),
                                                        str(networkx.is_directed_acyclic_graph(self.graph)))
        return stat

    def print_graph_stat(self):
        print(self._ont_statistic())

    def get_node(self,node_id):
        return self.graph.nodes.get(node_id)
#
# def Node(object):
#     def __init__(self,ont):
#         pass
#
# def HPONode(Node):
#     pass
#
# def Edge(object):
#     pass

