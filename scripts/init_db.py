from ddp2neo4j.repository.hpo_repo import HPOReposity
from ddp2neo4j.core.parser import OboParser
from ddp2neo4j.resources.res import HPO_Resource
from ddp2neo4j.repository.patient_repo import PatientReposity
from ddp2neo4j.core.parser import PatientParser
from ddp2neo4j.resources.res import Patient_Resource

hpo_terms = OboParser.parse_file(HPO_Resource.file_dev,True)
HPOReposity.batch_create_from_dict(hpo_terms,batch_size=3)



patient_records = PatientParser.parse_file(Patient_Resource.file_dev, True)
PatientReposity.batch_create_from_dict(patient_records,batch_size=1)
