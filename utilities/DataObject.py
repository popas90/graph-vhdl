from utilities.ComparableMixin import ComparableMixin


class DataObject(ComparableMixin):

    def __init__(self, tp, ident=''):
        self.type = tp
        self.identifier = ident

    def __repr__(self):
        if self.identifier != '':
            return self.type + ' "' + self.identifier + '"'
        else:
            return self.type

    def _cmpkey(self):
        return (self.type, self.identifier)

    def __hash__(self):
        return hash(self._cmpkey())
