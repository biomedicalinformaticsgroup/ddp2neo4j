from networkx import DiGraph

from ddp2neo4j.resources.res import HPO_Resource
from ddp2neo4j.resources.res import Patient_Resource
from ddp2neo4j.core.parser import OboParser
from ddp2neo4j.core.parser import PatientParser


def test_hpo_parser():
    g = OboParser.parse_file(HPO_Resource.file_dev)
    assert isinstance(g, DiGraph)
    assert len(g.nodes()) == 4


def test_patient_parser():
    patient_readers = PatientParser.parse_file(Patient_Resource.file_dev)

    assert patient_readers['P1']['patient_id'] == 'P1'
    assert set(patient_readers['P1']['genes']) == set(['2'])
    assert set(patient_readers['P1']['hpos']) == set(['HP:0000005', 'HP:0000007'])
