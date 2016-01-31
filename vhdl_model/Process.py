class Process:

    def __init__(self):
        self.label = ""
        self.sensitivity_list = []
        self.is_sequential = None

    def __str__(self):
        if self.label != '':
            return 'Process -> label: "' + self.label + '"'
        else:
            return 'Process'
