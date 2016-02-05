class DataContainer:

    def __init__(self, tp):
        self.type = tp
        self.elements = []

    def __str__(self):
        if self.elements != []:
            return self.type + ' [' + ','.join(map(str, self.elements)) + ']'
        else:
            return self.type
