from logic.variables import Statement


class KnowledgeBase:
    def __init__(self):
        self.knowledge = []

    def add(self, statement):
        self.knowledge.append(statement)


class say:
    def __init__(self, saying):
        self.saying = saying

    def means(self, meaning):
        return Meaning(self, meaning)

    def __str__(self):
        return '"%s"' % self.saying


class Meaning(Statement):
    """
    Class that stores the meaning associated with a saying.
    """
    def __init__(self, saying, meaning):
        self.saying = saying
        self.meaning = meaning

    def __str__(self):
        return "%s means %s" % (self.saying, self.meaning)


def hear(saying, meaning):
    pass


def rule(statement, condition=None):
    pass


def what(variable):
    pass


def is_(condtion):
    pass


def months(number):
    pass

