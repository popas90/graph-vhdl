class Component:

    def __init__(self):
        self.label = ""
        self.name = ""
        self.input_ports = []
        self.output_ports = []
        self.associations = []

    def add_input_port(self, input_port):
        self.input_ports.append(input_port)

    def add_output_port(self, output_port):
        self.output_ports.append(output_port)

    # def __repr__(self):
    #    return "Component, label: " + (self.label) + ", name: " + (self.name)
