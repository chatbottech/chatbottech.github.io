

class Duration:
    def __init__(self, name):
        self.name = name


class Option:
    def __init__(self, name, options):
        self.name = name
        self.options = options

    def __eq__(self, other):
        return Equals(self, other)


class Equals:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __contains__(self, item):
        print('contains')


