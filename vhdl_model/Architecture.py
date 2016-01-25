class Architecture:

    def __init__(self):
        self.identifier = ''
        self.entity = None
        self.signals = []
        self.components = []
        self.contents = []

    def set_entity(self, new_entity):
        self.entity = new_entity

    def add_signal(self, new_signal):
        self.signals.add(new_signal)

    def add_component(self, new_component):
        self.components.add(new_component)

    def add_instance(self, new_instance):
        pass

    def add_process(self, new_process):
        pass

    def add_concurrent_assignment(self, new_assignment):
        pass
