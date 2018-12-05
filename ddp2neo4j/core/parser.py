import csv

import obonet

from ddp2neo4j.core.patient_record import PationRecord


class Parser(object):
    def parse_file(self, **kwargs):
        raise NotImplementedError('Need to implement in subclass')

    def parse_url(self, url):
        raise NotImplementedError('Need to implement in subclass')


class OboParser(Parser):

    @classmethod
    def parse_file(cls, file, as_dict=False):
        ont = obonet.read_obo(file)
        if (as_dict):
            ont = cls.networkx_node_to_dict(ont)
        return ont

    @classmethod
    def parse_url(cls, url, as_dict=False):
        ont = obonet.read_obo(url)
        if (as_dict):
            ont = cls.networkx_node_to_dict(ont)
        return ont

    @classmethod
    def networkx_node_to_dict(cls, networkx):
        dict = {}
        for term_id, properties in networkx.nodes(data=True):
            properties['primary_id'] = term_id
            dict[term_id] = properties
        return dict


class PatientParser(Parser):

    @classmethod
    def parse_file(cls, file, as_dict=False):
        patient_records = {}

        with open(file, newline='') as csvfile:
            patient_reader = csv.reader(csvfile, delimiter=',')
            next(patient_reader, None)
            for row in patient_reader:
                pr = PationRecord(row[0], row[1].split(';'), row[2].split(';'))
                patient_records[pr.primary_id] = pr

        if (as_dict):
            for patient_id, record in patient_records.items():
                patient_records.update({patient_id: record.toDict()})

        return patient_records

    @classmethod
    def parse_url(cls, url):
        raise NotImplementedError('Not Implemented')


