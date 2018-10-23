from ddp2neo4j.resources.res import Patient_Resource
from ddp2neo4j.repository.patient_repo import PatientReposity
from ddp2neo4j.core.parser import PatientParser

def test_create_nodes():
    patient_records = PatientParser.parse_file(Patient_Resource.file_dev,True)
    PatientReposity.batch_create_from_dict(patient_records,batch_size=1)

    nodes={}
    for n in PatientReposity.allNode():
        assert n.id
        nodes[n.primary_id]=n

    assert len(nodes) == 2




