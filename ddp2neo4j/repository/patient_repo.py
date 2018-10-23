from neomodel import UniqueProperty

from ddp2neo4j.entities.patient import Patient_HPO_Edge, PatientNode
from ddp2neo4j.repository.node_repo import Repository
from ddp2neo4j.repository.hpo_repo import HPOReposity


class PatientReposity(Repository):
    NodeEntity = PatientNode
    EdgeEntity = Patient_HPO_Edge

    @classmethod
    def create_nodes_from_patient_records(cls, patient_records):

        try:
            cls.deleteAll()
        except:
            raise

        batchList = []
        batchSize = 1
        total_nodes = len(patient_records)
        batch_number = total_nodes // batchSize
        batch_counter = 1
        try:
            for patient_id, pr in patient_records.items():
                node = cls.NodeEntity.inflateFromDict(pr.toDict())
                batchList.append(node.__properties__)
                if len(batchList) == batchSize:
                    print("creating batch {}/{} with {} nodes".format(batch_counter, batch_number, len(batchList)))
                    cls.batchCreate(*batchList)
                    batchList = []
                    batch_counter += 1
            cls.batchCreate(*batchList)
        except UniqueProperty:
            print('UniqueProperty error!')
            raise UniqueProperty

        patients = {}
        for patient in cls.allNode():
            patients[patient.patient_id] = patient

        for patient_id, patient in patients.items():
            for hpo in patient.hpos:
                patient.has_phenotypes.connect(HPOReposity.searchNode(hpo))
