from enum import Enum


class Duration:
    def __init__(self, name):
        self.name = name


class Option(Enum):
    # def __init__(self, name, options):
    #     self.name = name
    #     self.options = options

    # def __eq__(self, other):
    #     return Equals(self, other)

    def __str__(self):
        return type(self).__name__.replace("_", " ") + " is " + self.name



class Equals:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __contains__(self, item):
        print('contains')


