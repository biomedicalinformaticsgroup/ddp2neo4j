from ddp2neo4j.repository.hpo_repo import HPOReposity
from ddp2neo4j.core.parser import OboParser
from ddp2neo4j.resources.res import HPO_Resource
from ddp2neo4j.repository.patient_repo import PatientReposity
from ddp2neo4j.core.parser import PatientParser
from ddp2neo4j.resources.res import Patient_Resource

g = OboParser.parse_file(HPO_Resource.file_dev)
HPOReposity.create_nodes_from_networkX(g)



patient_records = PatientParser.parse_file(Patient_Resource.file_dev)
PatientReposity.create_nodes_from_patient_records(patient_records)
