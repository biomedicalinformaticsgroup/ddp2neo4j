from pkg_resources import resource_filename


class resources:
    pass

class HPO_Resource(resources):
    ontology_name = "Human Phenotype Ontology"
    url = 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo'
    file = resource_filename('ddp2neo4j.resources.obo', 'hpo.obo')
    file_dev = resource_filename('ddp2neo4j.resources.obo', 'hpo_dev.obo')


class Patient_Resource(resources):
    file = resource_filename('ddp2neo4j.resources.patient', 'patirntset.csv')
    file_dev = resource_filename('ddp2neo4j.resources.patient', 'patientset_dev.csv')
