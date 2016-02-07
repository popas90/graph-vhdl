from utilities.EqualityMixin import EqualityMixin


class Association(EqualityMixin):

    def __init__(self, act='', frm=''):
        self.actual = act
        self.formal = frm

    def __repr__(self):
        if self.formal != '' and self.actual != '':
            return 'Association -> formal: "' + (self.formal) + \
                '", actual: "' + (self.actual) + '"'
        elif self.actual != '':
            return 'Association -> actual: "' + (self.actual) + '"'
        else:
            return 'Association'
