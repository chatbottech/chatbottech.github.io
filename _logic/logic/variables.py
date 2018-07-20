from enum import Enum


class Duration:
    def __init__(self, name):
        self.name = name


class Conjunction:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return str(self.first) + " and " + str(self.second)


class Option(Enum):
    def __str__(self):
        return type(self).__name__.replace("_", " ") + " is " + self.name.replace("_", " ")

    def __and__(self, other):
        return Conjunction(self, other)


class Equals:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __contains__(self, item):
        print('contains')


