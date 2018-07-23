---
layout: review
title: Gupshup does a lot, but how good is it?
name: Gupshup
logo: "gupshup-logo.png"
site: "https://www.gupshup.io/"
info:
 - name: Platforms
   value: Messenger only
tags: [any, developer, non-technical]
score: 66
ratings:
 - name: Ease of use
   value: 3
 - name: Intelligence potential
   value: 3
 - name: Value for money
   value: 4
updated: 2018-07-03
---

Gupshup certainly tries to do a lot. Actually, it tries to do
everything: pre-built templates for common use cases, a non-technical
bot "flow" design tool, an IDE for developing bots using Javascript,
and a natural language processing API.

<img src="/img/gupshup-landing.png" class="img-fluid my-5">

The flow designer
-----------------

Gupshup has a flow designer much like most other chatbot creation
tools for non-technical users, except less beautifully designed than
the average.

<img src="/img/gupshup-screenshot.png" class="img-fluid my-5">

The flow designer does pretty much what you expect. This is what tools
like [Chatfuel](/reviews/chatfuel.html) have now made standard.

The integrated development environment (IDE)
--------------------------------------------

This is where it gets a bit interesting. I don't remember seeing
another tool with an online IDE built in.

<img src="/img/gupshup-ide.png" class="img-fluid my-5">

My first question here is: why? I'm not sure what there is about
chatbots that means they particularly need an online IDE rather than
using any of the many perfectly good offline ones.

My second question is: is it any good? I'd say it's ok, but it's no
match for a decent offline IDE. I really think they've tried to
reinvent the wheel here, and I don't understand the value in it.

The actual Javascript API looks ok, so if you like doing things in
Javascript you may be interested. You will get more flexibility than
the flow designer. But you will probably get less flexibility than if
you used a sophisticated framework like
[Microsoft's](/reviews/microsoft-bot-framework.html).


Gupshup's natural language processing
-------------------------------------

Gupshup has something they call "on-the-fly NLP". What this means is
that it takes some training data along with your query, and finds the
best matching intent and extracts entities using that training data.

This is a bit suspicious. What it means is that it is not really doing
any real NLP: there is no model. Instead it is probably doing
something like fuzzy string matching to identify the closest matching
string in the training items you pass in.

Actually for simple bots, this is not a bad idea, and is an approach
that I've used successfully before. The problem is that it's not a
scalable approach. For complex bots, you could need hundreds or
thousands of training examples. At this point, there will be two
problems:
 - Passing the training examples with every request becomes costly
 - Accuracy will not be as good as machine-learning based NLP models

If the NLP component is important to your bot, then you will most
likely be better off with something like
[Dialogflow](/reviews/dialogflow.html).

Pricing
-------

Gupshup is free for up to 100,000 API calls, after which it costs $1
for every 1,000 API calls.

What next?
----------

Gupshup tries to do everything, and doesn't seem to succeed at doing
any one thing extremely well. There are
[plenty of other tools](/). I'd suggest you figure out which thing you
need, then find the best tool that does that. It probably won't be
Gupshup.
