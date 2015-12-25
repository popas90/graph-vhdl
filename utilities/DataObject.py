from collections import namedtuple


class DataObject:

    def __init__(self, tp):
        self.type = tp
        self.identifier = ''

    def __str__(self):
        return (self.type)
