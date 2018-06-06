---
layout: review
title: "IBM Watson Assistant is not too shabby"
name: IBM Watson Assistant
logo: "ibm-watson-logo.png"
site: "https://www.ibm.com/watson/services/conversation/"
info:
 - name: Platforms
   value: "Messenger, Slack, Twilio, Web, App"
tags: [any, non-technical, developer]
score: 76
updated: Wed Apr 18 12:48:47 BST 2018

ratings:
 - name: Ease of use
   value: 4
 - name: Intelligence potential
   value: 4
 - name: Value for money
   value: 3
---

Watson seems to be IBM's brand for anything AI related. You may have
heard how Watson competed in the TV quiz show Jeopardy and won. Well,
I doubt they used much of that technology in their chatbot tool, but
it was a great promotional gimmick.

They've actually built a pretty standard, and pretty solid tool, not
too dissimilar from TensorFlow. You can define intents and entities,
giving examples for each. Once you've deployed your bot and got some
examples from real users, you can train it further by correcting any
incorrectly identified intents or entities.

Testing your bot
----------------

Trying out the bot is gloriously simple. A button opens a right-hand
drawer in which you can chat with your bot. A flashing bar at the top
shows if Watson is currently training your model, which typically
doesn't take too long. This aspect of the tool is a win over
Tensorflow, where testing your bot is a little more convoluted.

Intents and Entities
--------------------

<img src="/img/ibm-watson-screenshot.png" class="img-fluid">


One design decision they have made that is a little questionable is
that entities and intents are not explicitly related. Unlike
dialogflow, where an intent has an associated set of required
entities, this type of requirement is specified in the dialog
specification itself. I can define a "node" which looks for a
particular intent. I can then specify that certain entities are
required to continue. I can also specify questions to ask the user if
these are missing.

The end result is that you can build something similar in behaviour to
what you would build with tensorflow, just that the workflow is a
little different.

I am a little sceptical of this decision. It feels wrong to me that
you can define an intent without specifying how it relates to
entities. For example, imagine an intent around booking a train
journey. If I'm taking the train, there will be a required departure
point, a destination and certain time restrictions. These are inherent
to the intent itself. But Watson's design implies that it might be
possible to want to take a train without knowing those things. In
practice, their approach will probably work, but it just _feels_
wrong...

Pricing
-------

The free plan allows 10,000 API calls per month, five chatbots, 100
intents and 25 entities. The standard plan has unlimited API calls at
a cost of $0.0025 per call. You can have up to 20 chatbots, 2,000
intents and 1,000 entities. They also offer a "premium" plan of
unspecified cost if this does not meet your needs.
