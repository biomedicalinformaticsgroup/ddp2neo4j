class PationRecord(object):
    def __init__(self, patient_id, genes, hpos):
        self.patient_id = patient_id
        self.genes = genes
        self.hpos = hpos

    def toDict(self):
        return self.__dict__
