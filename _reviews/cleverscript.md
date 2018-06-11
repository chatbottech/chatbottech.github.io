---
layout: review
title: "Cleverscript: good if want a bot to chat to"
name: Cleverscript
logo: "existor-logo.png"
site: "https://www.cleverscript.com/"
info:
 - name: Type
   value: Chatbot scripting
 - name: License
   value: Commercial
 - name: Platforms
   value: "Web, mobile"
tags: [any, developer]
score: 66
updated: Fri Apr 13 15:34:20 BST 2018

ratings:
 - name: API Design
   value: 2
 - name: Quality
   value: 3
 - name: Value for money
   value: 4
---

Cleverscript is the technology behind
[Cleverbot](https://en.wikipedia.org/wiki/Cleverbot), whose
predecessor Jaberwacky won the Loebner prize in 1996. This is a
competition which awards a prize for creating chatbots that are judged
by humans to be the most human-like. It thus has a long history,
harking back to the days when chatbots were for fun and
experimentation rather than profit.

This shows in the way Cleverscript works. It is a powerful tool if you
want to build a bot which provides information or
entertainment. However it requires careful engineering: there is no
real semantic parsing like other tools have: natural language
expressions have to be parsed manually.

Cleverbot seems to eschew standard conventions. Parsing is done using
Cleverscript "phrases" that are basically a new syntax for regular
expressions. The script itself is written using a tab-delimited file
of columns. Each row can specify a phrase that can be recognised or
output to the user, together with a variety of different actions that
can be taken on receiving that input, such as setting variable values.

Using this format, it is possible to script conversations much faster
than if you were writing them in a standard scripting language such as
Python. The downside is, you are tied to using Cleverscript's
proprietary software to run your bot.

Cleverscript is unfortunately a long way behind the competition in
terms of building useful bots. Because there is no enforced separation
between converting natural language expressions to intents (semantic
parsing), there is also no interface to easily add new phrases that
are encountered in use - these have to be encoded manually by the
chatbot creator.

It also does not provide a straightforward way to make use of your bot
in a production setting: you can either make use of their JSON API,
use a provided Javascript library or purchase the software to run on
your own servers.

Cleverscipt costs $10 a month for up to 10,000 calls
to the JSON API. A license to run the software on your own servers
is available for a one-off fee of $5000.
