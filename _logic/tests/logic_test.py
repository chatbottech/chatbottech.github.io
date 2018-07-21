from logic.knowledge_base import KnowledgeBase, what, is_, months, say
from logic.variables import Option


class visa_purpose(Option):
    business = 1
    study = 2


class visa_type(Option):
    short_term_study = 1
    business = 2


class profession(Option):
    entrepreneur = 1
    investor = 2
    other = 3

# def test_visa():
#     kb = KnowledgeBase()
#
#     visa_duration = Duration('visa_duration')
#
#     kb.say("How long do you want to come to the UK for?", what(visa_duration))
#     kb.say("What is the purpose of your visit?", what(visa_purpose))
#     kb.say("Are you coming for business?", is_(visa_purpose.business))
#     kb.say("You can get a short term study visa", visa_type.short_term_study)
#
#     kb.hear("I'm coming to study.", visa_purpose.study)
#     kb.hear("I want to come for five months.", visa_duration == months(5))
#
#     kb.rule(visa_type.short_term_study, visa_duration <= months(6) and visa_purpose == 'study')
#     kb.rule(what(visa_type))


def test_option():
    assert str(visa_purpose.business) == "visa purpose is business"


def test_conjunction():
    assert str(visa_purpose.business & visa_type.short_term_study) == \
        "visa purpose is business and visa type is short term study"


def test_multiple_conjunctions():
    assert str(visa_purpose.business & visa_type.short_term_study & profession.investor) == \
           "visa purpose is business and visa type is short term study and profession is investor"


def test_meanings():
    assert str(say("You need a short term study visa").means(visa_type.short_term_study)) == \
        '"You need a short term study visa" means visa type is short term study'


def test_simple_behaviour():
    kb = KnowledgeBase()

    kb.add(say("You can get a short term study visa").means(visa_type.short_term_study))
    kb.add(visa_type.short_term_study)
    kb.add(what(visa_type))

