---
layout: default
title: Botpress
logo: "botpress-logo.png"
site: "https://botpress.io/"
info:
 - name: Type
   value: Open Source Bot Framework
 - name: License
   value: GNU Affero GPL v3
ratings:
 - name: API Design
   value: 
 - name: Quality
   value: 
---

A Review of the Botpress Chatbot Framework
==========================================

Botpress is different from other chatbot frameworks: it is really a
way to glue different pieces of chatbot technology together. This is
potentially a powerful idea - let's say you've done all the hard work
of making your bot for Messenger, but now you want to roll it out to
Slack too. With Botpress this is (in theory) simple: it includes
modules for both Messenger and Slack, so all you have to do is swap
out one module for another, while the rest of your implementation
stays the same. This can potentially save you a lot of time. In
addition, it wraps up other third party tools so you can easily
combine them.

At the time of writing, there are modules available for the following
tools:

 - Wit.ai
 - Dialogflow
 - [Rasa NLU](https://github.com/RasaHQ/rasa_nlu)
 - Microsoft Bot Framework

and the following platforms:

 - Embeddable web chat
 - Slack
 - Messenger
 - Discord
 - Telegram
 - Twilio
 - IRC

It also has some custom built modules:

 - A [scheduler](https://www.npmjs.com/package/botpress-scheduler) for one-off or recurring tasks
 - A [monetization module](https://www.npmjs.com/package/botpress-monetize)
 - A [way to create webhooks](https://www.npmjs.com/package/botpress-webhook)
   for your bot
 - Bot [analytics](https://www.npmjs.com/package/botpress-analytics)
 - A [BroidKit](https://github.com/broidHQ/broid-kit) module allowing
   you to access an even wider range of platforms
 - A [way to interact with your bot through the terminal](https://www.npmjs.com/package/botpress-terminal)
 - A [module for the RiveScript scripting language](https://www.npmjs.com/package/botpress-rivescript)
 - A [module for managing subscriptions](https://www.npmjs.com/package/botpress-subscription)
 - A [module that allows people to take over conversations](https://www.npmjs.com/package/botpress-hitl)
 
One concern I have about this is the quality of all these modules. At
some point, perhaps I'll try and evaluate each one individually, but a
quick glance indicates that the quality is highly variable, with some
modules updated frequently and some not at all. The idea sounds great,
but I suspect that it will be a while before the module ecosystem is
developed enough for building a bot to be painless with this
framework.

In summary, enormous potential, but be prepared to put in some work to
find the bits that work reliably, and/or fix the things that don't.
