from neomodel import UniqueProperty
from neomodel import config
from neomodel import db

import math

from ddp2neo4j import settings


class Repository(object):
    username = settings.neo4j['username']
    password = settings.neo4j['password']
    config.DATABASE_URL = 'bolt://{username}:{password}@{host}:{port}'.format(username=username, password=password,
                                                                              host=settings.neo4j['host'],
                                                                              port=settings.neo4j['port'])
    config.AUTO_INSTALL_LABELS = settings.neomodel['AUTO_INSTALL_LABELS']

    NodeEntity = None
    EdgeEntity = None

    @classmethod
    def batch_create_from_dict(cls, dict, delete_before_create=True, batch_size=300):
        """
        create node from a dictionary of items. Item primary id is used as index and all properties as value.

        Example:
                dict = {'HP:00001': {'primary_id': 'HPO:00001', 'is_a' :'HPO:000000'},
                        'HP:00002': {'primary_id': 'HPO:00002', 'is_a' :'HPO:000001'}}
        :param dict:
        :param delete_before_create:
        :param batch_size:
        :return: None
        """
        if (delete_before_create):
            try:
                cls.deleteAll()
            except:
                raise

        cls.batchCreate(dict, batch_size)
        cls._create_relations()


    @classmethod
    def _create_relations(cls):
        """
        create relations of the nodes inserted by the function batch_create_from_dict
        :return: None
        """
        print("Creating relations for nodes...")
        # raise NotImplementedError('Need tpytho implement in subclass')


    @classmethod
    def deleteAll(cls):
        """
        delete all node with a label specifiy by cls.NodeEntity
        :param cls:
        :return: None
        """
        print("Delete all nodes and relationships of node type {} ...".format(cls.NodeEntity.__name__))
        query = "MATCH (n:{}) DETACH DELETE n".format(cls.NodeEntity.__name__)
        try:
            db.cypher_query(query)
        except:
            raise


    @classmethod
    def searchNode(cls, primary_id):
        """
        search node with label cls.NodeEntity
        :param cls:
        :param primary_id:
        :return: a node entity of class cls.NodeEntity
        """
        try:
            return cls.NodeEntity.nodes.get(primary_id=primary_id)
        except:
            raise


    @classmethod
    def allNode(cls, ):
        """
        query all nodes with label cls.NodeEntity
        :param cls:
        :return:
        """
        return cls.NodeEntity.nodes


    @classmethod
    def batchCreate(cls, dict, batch_size):
        """
        create nodes in batch.
        :param cls:
        :param dict:
        :param batch_size:
        :return:
        """
        batchList = []
        total_nodes = len(dict)
        batch_number = math.ceil(total_nodes / batch_size)
        batch_counter = 1
        print("Inserting {} {} nodes into neo4j with batch size of {}.".format(total_nodes,cls.NodeEntity.__name__ ,batch_size))
        try:
            for id, item in dict.items():
                node = cls.NodeEntity.inflateFromDict(item)
                batchList.append(node.__properties__)
                if len(batchList) == batch_size:
                    print("creating batch {}/{} with {} nodes...".format(batch_counter, batch_number, batch_size))
                    cls.NodeEntity.create(*batchList)
                    batchList = []
                    batch_counter += 1

            if(len(batchList) > 0):
                print("creating batch {}/{} with {} nodes...".format(batch_counter, batch_number, len(batchList)))
                cls.NodeEntity.create(*batchList)
        except UniqueProperty:
            print('UniqueProperty error!')
            raise UniqueProperty
