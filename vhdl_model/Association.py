class Association:

    def __init__(self):
        self.formal = ''
        self.actual = ''

    def __repr__(self):
        if self.formal != '' and self.actual != '':
            return 'Association -> formal: "' + (self.formal) + \
                '", actual: "' + (self.actual) + '"'
        elif self.actual != '':
            return 'Association -> actual: "' + (self.actual) + '"'
        else:
            return 'Association'
