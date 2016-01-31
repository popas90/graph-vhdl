class Component:

    def __init__(self):
        self.label = ""
        self.name = ""
        self.input_ports = []
        self.output_ports = []
        self.associations = []

    def __repr__(self):
        if self.label != '' and self.name != '':
            return 'Component -> label: "' + (self.label)
            + '", name: "' + (self.name) + '"'
        else:
            return 'Component'
