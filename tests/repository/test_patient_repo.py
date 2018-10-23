from ddp2neo4j.resources.res import Patient_Resource
from ddp2neo4j.repository.patient_repo import PatientReposity
from ddp2neo4j.core.parser import PatientParser

def test_create_nodes():
    patient_records = PatientParser.parse_file(Patient_Resource.file_dev)
    PatientReposity.create_nodes_from_patient_records(patient_records)

    nodes={}
    for n in HPOReposity.allNode():
        assert n.id
        nodes[n.term_id]=n

    assert len(nodes) == 4




