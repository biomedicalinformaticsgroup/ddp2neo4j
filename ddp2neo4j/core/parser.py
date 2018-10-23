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
    def parse_file(cls, file):
        ont = obonet.read_obo(file)
        return ont

    @classmethod
    def parse_url(cls, url):
        ont = obonet.read_obo(url)
        return ont


class PatientParser(Parser):

    @classmethod
    def parse_file(cls, file):
        patient_records = {}

        with open(file, newline='') as csvfile:
            patient_reader = csv.reader(csvfile, delimiter=',')
            next(patient_reader, None)
            for row in patient_reader:
                pr = PationRecord(row[0], row[1].split(';'), row[2].split(';'))
                patient_records[pr.patient_id] = pr
        #         patient_records[row[0]] = {'patient_id': row[0],
        #                                    'genes': row[1].split(';'),
        #                                    'hpos': row[2].split(';')}
        return patient_records

    @classmethod
    def parse_url(cls, url):
        raise NotImplementedError('Not Implemented')