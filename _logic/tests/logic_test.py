from logic.operators import what, say, is_
from logic.variables import Duration, Option


def test_simple():
    visa_duration = Duration('duration')
    visa_purpose = Option('visa_purpose')
    visa_type = Option('visa_type')

    say("How long do you want to come to the UK for?", what(visa_duration))
    say("What is the purpose of your visit?", what(visa_purpose))
    say("Are you coming for business?", is_(visa_purpose == 'business'))
    say("You can get a short term study visa", visa_type == 'short_term_study')
