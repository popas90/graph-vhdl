class Entity:

    def __init__(self):
        self.identifier = ''
        self.generics = []
        self.ports = []

    def add_generic(self, new_generic):
        self.generics.add(new_generic)

    def add_port(self, new_port):
        self.ports.add(new_port)
