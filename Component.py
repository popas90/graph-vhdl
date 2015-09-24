class Component:

    def __init__(self):
        self.label = ""
        self.name = ""
        self.input_ports = []
        self.output_ports = []

    def add_name(self, name):
        self.name = name

    def add_label(self, label):
        self.label = label

    def add_input_port(self, input_port):
        self.input_ports.append(input_port)

    def add_output_port(self, output_port):
        self.output_ports.append(output_port)