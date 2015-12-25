from collections import namedtuple


class NamedObject:

    def __init__(self, tp, ident):
        self.type = tp
        self.identifier = ident

    def __str__(self):
        return (self.type + ', id: ' + self.identifier)
