class Process:

    def __init__(self):
        self.label = ""
        self.sensitivity_list = set()
        self.declarations = []
        self.statements = []
        self.inputs = set()
        self.outputs = set()

    def __str__(self):
        if self.label != '':
            return 'Process -> label: "' + self.label + '"'
        else:
            return 'Process'
