from enum import Enum


class Statement:
    def __and__(self, other):
        return Conjunction(self, other)


class Conjunction(Statement):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return str(self.first) + " and " + str(self.second)


class Option(Statement, Enum):
    def __str__(self):
        return type(self).__name__.replace("_", " ") + " is " + self.name.replace("_", " ")



