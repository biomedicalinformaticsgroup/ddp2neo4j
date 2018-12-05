class PationRecord(object):
    def __init__(self, primary_id, genes, hpos):
        self.primary_id = primary_id
        self.genes = genes
        self.hpos = hpos

    def toDict(self):
        return self.__dict__

