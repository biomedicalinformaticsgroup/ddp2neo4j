from neomodel import config
from neomodel import db

from ddp2neo4j import settings


class Repository(object):
    username = settings.neo4j['username']
    password = settings.neo4j['password']
    config.DATABASE_URL = 'bolt://{username}:{password}@{host}:{port}'.format(username=username, password=password,
                                                                              host=settings.neo4j['host'],
                                                                              port=settings.neo4j['port'])
    config.AUTO_INSTALL_LABELS = True

    @classmethod
    def deleteAll(cls):
        print("Delete all nodes and relationships...")
        query = "MATCH (n:{}) DETACH DELETE n".format(cls.NodeEntity.__name__)
        db.cypher_query(query)

    @classmethod
    def searchNode(cls, term_id):
        return cls.NodeEntity.nodes.get(term_id=term_id)

    @classmethod
    def allNode(cls, ):
        return cls.NodeEntity.nodes

    @classmethod
    def batchCreate(cls, *args):
        cls.NodeEntity.create(*args)