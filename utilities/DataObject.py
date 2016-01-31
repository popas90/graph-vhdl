class DataObject:

    def __init__(self, tp):
        self.type = tp
        self.identifier = ''

    def __str__(self):
        if self.identifier != '':
            return self.type + ' "' + self.identifier + '"'
        else:
            return self.type
