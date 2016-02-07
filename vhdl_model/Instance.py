from utilities.EqualityMixin import EqualityMixin


class Instance(EqualityMixin):

    def __init__(self):
        self.label = ""
        self.name = ""
        self.generic_map = None
        self.port_map = None

    def __repr__(self):
        if self.label != '' and self.name != '':
            return 'Instance -> label: "' + self.label + \
                '", name: "' + self.name + '", ' + str(self.port_map) + \
                ', ' + str(self.generic_map)
        else:
            return 'Instance'
