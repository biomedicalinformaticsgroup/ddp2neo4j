import obonet


class Parser(object):
    def parse_file(self, **kwargs):
        raise NotImplementedError('Need to implement in subclass')

    def parse_url(self, url):
        raise NotImplementedError('Need to implement in subclass')


class OboParser(Parser):

    def parse_file(self, file):
            ont = obonet.read_obo(file)
            return ont

    def parse_url(self, url):
            ont = obonet.read_obo(url)
            return ont
