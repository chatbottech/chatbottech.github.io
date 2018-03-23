---
layout: default
title: LUIS.ai
name: LUIS.ai
logo: "microsoft-azure-logo.png"
site: "https://www.luis.ai/"
info:
 - name: Type
   value: Semantic Parser
tags: [any, developer]
score: 69
ratings:
 - name: API Design
   value: 4
 - name: Quality
   value: 3
 - name: Value for money
   value: 3
---

A Review of Microsoft's Luis.AI Natural Language Understanding API
==================================================================

Microsoft's natural language understanding framework LUIS is
essentially a semantic parser. Like Facebook's Wit.ai it's goal is to
take the user's input in the form of text and transform it to a
machine readable form, in this case, an _intent_ that describes what
the user wants.

Unlike Wit.ai, Microsoft have taken the shrewd move of restricting
which intents can be chosen for your bot. Before you can try out the
API, you have to create a LUIS app for your bot and choose exactly
which intents your bot will interpret. Intents can either be from the
existing list of 150, or more likely, you will need to create your
own. Here's a random selection of things you can do with existing
intents:

 - Turn on a device setting
 - Show an app bar
 - Put the device to sleep
 - Capture a screenshot
 - Delete an entire note
 - Confirm an action relating to a place
 - Confirm an action relating to a note
 - Stop broadcasting video
 - Answer an incoming phone call
 - Start recording video

After you have selected your intents, you can train your LUIS app, and
test it out with natural language queries.

I tried creating a LUIS app for my (imaginary) restaurant, The
Eatalot. I wanted  to add an intent for ordering food. There didn't
seem to be an appropriate one available so I created a new one, called
_item-cost_, and added some examples of what a user might say, like
"How much is the pizza?" At this point you can train the app and test
it out. If I ask "How much are the burgers?" at this point, it won't
detect that I'm asking about burgers; in order for this to work you
have to add "entities". In this case, there is a set of entities for
food that I can add. I can then identify "pizza" in my example
sentence as being food. After retraining my model, I can ask it "How
much for fries?" and it correctly identifies the intent and
entity. Unfortunately, it is not very robust as asking "How much is a
burger?" identifies the correct intent, but not the entity, presumably
because "burger" has not been entered as a food entity. This is a
pity; it's easy to automatically identify all types of food using
distributional similarity, and it'd be nice for an app to be able to
say, "I'm sorry we don't do burgers" without having to add every
possible type of food as something that people may ask for.

What Microsoft has done actually makes a lot of sense. They know they
can't excel at detecting all intents, so only allow apps to detect
intents they care about - they won't be able to handle other ones
anyway, so it doesn't make sense to consider them. It's an approach
that requires designers to engineer their bots much more than relying
on artificial intelligence. This is probably sensible, as any bot with
a decent range of behaviour will necessarily require a lot of
engineering, with or without artificial intelligence.

Unfortunately Microsoft's offering falls short in several respects:

 - The set of pre-defined intents and entities are not nearly
   comprehensive enough to automatically be useful to most users.
 - The system should be able to identify terms as belonging to an
   intent category, without that term explicitly having to be defined
   as belonging to that category (the "burger" problem).
 - The bot designer should be able to enter some example queries, and
   the system should suggest intents and entities that may be
   suitable, allowing the bot designer to quickly pick the right
   ones.

These concerns are not hard to address, so I hope Microsoft is taking
note, and we'll let you know if things change!

Pricing of LUIS is simple and sensible: at $1.50 per 1,000 queries, it
is slightly cheaper than
[Dialogflow](/reviews/non-technical/01-dialogflow.html), which I would
consider the main competitor. However you get a much lower quality
service with fewer features.

In summary, unless you are somehow tied to Microsoft's ecosystem, I
would suggest going with Dialogflow instead of this for now, at least
until Microsoft improve their offering.
