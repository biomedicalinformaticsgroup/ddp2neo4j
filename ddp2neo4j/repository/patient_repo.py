from neomodel import UniqueProperty

from ddp2neo4j.entities.nodes import Patient_HPO_Edge, PatientNode
from ddp2neo4j.repository.node_repo import Repository
from ddp2neo4j.repository.hpo_repo import HPOReposity


class PatientReposity(Repository):
    NodeEntity = PatientNode
    EdgeEntity = Patient_HPO_Edge

    @classmethod
    def _create_relations(cls):
        super()._create_relations()
        patients = {}
        for patient in cls.allNode():
            patients[patient.primary_id] = patient

        for primary_id, patient in patients.items():
            for hpo in patient.hpos:
                patient.has_phenotypes.connect(HPOReposity.searchNode(hpo),{'weight':1})