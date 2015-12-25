class Process:

    def __init__(self):
        self.label = ""
        self.sensitivity_list = []
        self.is_sequential = None

    def add_label(self, label):
        self.label = label
