from utilities.EqualityMixin import EqualityMixin


class DataObject(EqualityMixin):

    def __init__(self, tp, ident=''):
        self.type = tp
        self.identifier = ident

    def __repr__(self):
        if self.identifier != '':
            return self.type + ' "' + self.identifier + '"'
        else:
            return self.type
