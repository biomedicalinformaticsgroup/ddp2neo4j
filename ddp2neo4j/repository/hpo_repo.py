from neomodel import UniqueProperty

from ddp2neo4j.entities.hpo import HPONode, HPOEdge
from ddp2neo4j.repository.node_repo import Repository


class HPOReposity(Repository):
    NodeEntity = HPONode
    EdgeEntity = HPOEdge

    @classmethod
    def create_nodes_from_networkX(cls, networkX):

        g = networkX

        try:
            cls.deleteAll()
        except:
            raise

        # nodes = {}
        # try:
        #     for term_id, properties in g.nodes(data=True):
        #         # term_id = 'HP:0010265'
        #         # properties = n
        #         properties['term_id'] = term_id
        #         node = HPONode.inflateFromNxNode(properties)
        #         node.save()
        #         nodes.update({term_id:node})
        # except UniqueProperty:
        #     print('UniqueProperty error!')
        #     raise UniqueProperty

        batchList = []
        batchSize = 2
        total_nodes = len(g.nodes)
        batch_number = total_nodes // batchSize
        batch_counter = 1
        try:
            for term_id, properties in g.nodes(data=True):
                # term_id = 'HP:0010265'
                # properties = n
                properties['term_id'] = term_id
                node = cls.NodeEntity.inflateFromDict(properties)
                batchList.append(node.__properties__)
                if len(batchList) == batchSize:
                    print("creating batch {}/{} with {} nodes".format(batch_counter, batch_number, len(batchList)))
                    cls.batchCreate(*batchList)
                    batchList = []
                    batch_counter += 1
            cls.batchCreate(*batchList)
        except UniqueProperty:
            print('UniqueProperty error!')
            raise UniqueProperty

        nodes = {}
        for node in cls.allNode():
            nodes[node.term_id] = node

        for term_id, node in nodes.items():
            for parent in node.is_a:
                node.is_child_of.connect(nodes[parent])
