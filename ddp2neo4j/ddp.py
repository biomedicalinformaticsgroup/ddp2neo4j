from ddp2neo4j.core.ontology import HPO
from ddp2neo4j.utli.parser import OboParser
from ddp2neo4j.entities.ontology import OntologyNode
from neomodel import config




ont = OboParser().parse_file(HPO.file)
hpo = HPO(ont)
hpo.print_graph_stat()
node = hpo.get_node('HP:0007759')
print(node)

username='neo4j'
password=''
config.DATABASE_URL = 'bolt://{}:{}@129.215.164.31:443'.format(username,password)

e_node = OntologyNode(term_id='HP:0007759',term_name=node['name']).save()
e_node = OntologyNode(term_id='HP:0007759',term_name=node['name']).save()
print(e_node)
e_node.term_id='HP:0007759aaaaa'
e_node.save()
e_node.refresh()  # reload properties from neo
print(e_node)  # neo4j internal id

exit(1)




jim = Person(name='Jim', age=3).save()
jim.age = 4
jim.save()  # validation happens here
# jim.delete()
jim.refresh()  # reload properties from neo
jim.id  # neo4j internal id

germany = Country(code='DE').save()
jim.country.connect(germany)

if jim.country.is_connected(germany):
    print("Jim's from Germany")

for p in germany.inhabitant.all():
    print(p.name)  # Jim

len(germany.inhabitant)  # 1

# Find people called 'Jim' in germany
germany.inhabitant.search(name='Jim')

# Remove Jim's country relationship with Germany
jim.country.disconnect(germany)

usa = Country(code='US').save()
jim.country.connect(usa)
jim.country.connect(germany)

# Remove all of Jim's country relationships
jim.country.disconnect_all()

jim.country.connect(usa)
# Replace Jim's country relationship with a new one
jim.country.replace(germany)
