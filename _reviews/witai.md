---
layout: default
title: Wit.ai
logo: "wit-ai-logo.png"
site: "https://wit.ai/"
info:
 - name: Type
   value: Semantic Parser
tags: [any, developer]
score: 77
ratings:
 - name: API Design
   value: 4
 - name: Quality
   value: 2
 - name: Value for money
   value: 5
---

A Review of Facebook's Wit.ai
=============================

I like what Wit.ai is trying to do. I like that they are focussing on
a hard problem, and I also think it's an important problem for bot
developers. Wit.ai does semantic parsing, and not much else. Semantic
parsing is the task of turning natural language expressions into a
machine readable form, in this case, "intents", for example, the
request "set the alarm for 6am" returns the following:

```json
{
   "confidence": 0.953,
   "intent": "alarm_set",
   "_text": "Set the alarm for 6am",
   "entities": {
      "datetime": [
         {
            "value": {
               "from": "2018-02-14T06:00:00.000-08:00",
               "to": "2018-02-14T07:00:00.000-08:00"
            }
         }
      ],
      "on_off": [
         {
            "value": "on"
         }
      ]
   }
}
```

The result contains everything my bot needs to perform the user's
request. And it's great when it works. Except it often doesn't. It
failed to understand these queries:

 - "I'd like a pizza with pepperoni" (unknown command)
 - "Where was Barack Obama born?" (recognised as a miscellaneous
   greeting, with confidence 0.4. I think I should try greeting people
   like that)
 - "I need a train from Luton to Norwich" (unknown command, although
   it does figure out that Luton and Norwich are places).
 - "I'm looking for an Italian restaurant near here" (unknown command,
   but it does detect "here" as a location, then adds a random "on
   off" value of "on").
 - "Play Superunknown by Soundgarden" (unknown command, with an "on
   off" value of "off").

It does recognise:

 - "What's the time, Mr Wolf?" as a query about the time, although it
   ignores "Mr Wolf"
   
Of course these are just random queries that popped into my head, and
this is not a scientific evaluation, nor are they probably the type of
queries that a real bot would have to deal with. I'm sure it would do
really well with those. Maybe.

Fortunately, Wit.ai allows you to add your own training data for cases
where it's not working - in fact it's set up so that the very fist
thing you do is add some expressions to define your intent. By
default, this training data is public (an "open app") so it is shared
with other bot developers to make the default behaviour of the system
better. It is possible to make the data private, by going to settings,
although this is discouraged in the interface by surrounding it with a
big red button and "Danger Zone" warning.

It's confusing to me that with all this training data from all the bot
developers, the default performance is as bad as it is. I'm
disappointed because it's actually a great idea. Using all this data,
together with some clever algorithms, they should be able to build an
amazing semantic parser. But something seems to have gone
wrong. What's going on, Facebook? I know you have clever data
scientists and natural language processing experts because I've seen
them talk at conferences. Surely if you got a few of them together and
implemented some state-of-the-art semantic parsing algorithms, this
would be solved?

Wit.ai's pricing model is entirely free. I assume the assumption for
them is that the training data is more valuable than people actually
paying for the service, but it concerns me that there is currently no
business model behind it. Wit.ai was purchased by Facebook in 2015;
the value for them is clearly in promoting and helping their bot
ecosystem grow, so that they can become the WeChat of the
west. However, with chatbots currently bringing in no revenue for
Facebook, and a large chunk of Wit.ai's functionality now incorporated
into Messenger's bot API, I would be concerned that the service will
be discontinued at some point. Depend on it at your peril!

