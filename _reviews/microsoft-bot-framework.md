---
layout: default
title: Microsoft Bot Framework
name: Microsoft Bot Framework
logo: "microsoft-azure-logo.png"
site: "https://dev.botframework.com/"
info:
 - name: Type
   value: Bot development framework
 - name: Messaging platforms
   value: Skype, Facebook, Teams, Slack, SMS and web
 - name: Languages
   value: C# (.NET), Node.js
tags: [any, developer]
score: 74
ratings:
 - name: API Design
   value: 4
 - name: Quality
   value: 4
 - name: Value for money
   value: 4
---

A Review of the Microsoft Bot Framework
=======================================

Microsoft have clearer put a lot of thought and effort into their bot
offerings; they clearly believe that bots are going to be big and they
want a share of the action. Their approach is definitely "developer
first" - there's currently no way to create a Microsoft bot if you're
non-technical.

Their platform is surprisingly cross-platform when it comes to
development tools, with binaries provided for Windows, Mac OS and
Linux, but I guess this is the new Microsoft. The format may not
always be what you expect (Linux binaries are supplised with a
".AppImage" extension) but at least they're making an effort.

When it comes to deployment, everything is set up to deploy to
Microsoft's Azure hosting, however it is possible to host on other
cloud services, for example Amazon Web Service.

The framework consists of the following components:

 - [Bot Builder SDK](https://github.com/Microsoft/BotBuilder): the
   open source SDK for .NET and Node.js
 - [Bot Connector Service](https://docs.microsoft.com/en-us/bot-framework/rest-api/bot-framework-rest-connector-quickstart):
   this provides a REST interface to make use of the different
   messaging platforms supported by the Bot Framework
 - [Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator):
   allows you to test your bot locally before deploying.
 - LUIS Natural Language Understanding Service
   ([reviewed separately](/reviews/developer/luis-ai.html)) which
   provides semantic parsing functionality and can be used
   independently of the Bot Framework.
 - [Bot Service](https://azure.microsoft.com/en-gb/services/bot-service/)
   for deploying bots on Microsoft's Azure platform.

Microsoft provides template bots to get you started quickly:

 - **Basic Bot:** a simple echo service
 - **Form Bot:** collects information from a user with a guided
   conversation, instead of getting the user to fill out a form
 - **Language Understanding Bot:** a bot that makes use of
   [LUIS](/reviews/developer/luis-ai.html) to perform semantic parsing
   of user queries
 - **Question and Answer Bot:** this makes use of Microsoft's
   [QnA Maker](https://qnamaker.ai/) service that allows you to
   quickly create a bot from a set of questions and answers
 - **Proactive bot:** a bot that can send messages to a user at any
   time, for example, a bot that sends users reminders

The advantage of Microsoft's framework is that it provides you with
tools to get going quickly, but it does not dictate any particular
solution. The downside of this is that when it comes to implementing
the brains of your bot, you are basically left to your own
devices. This is in contrast to
[Google's Dialogflow](/non-technical/01-dialogflow.html), for example,
which helps you interpret and make use of intents by designing the
flow of conversation.

There are two ways to implement a bot within their framework: as a
standard web app (which requires paying for a server to host the bot),
or a serverless bot that runs on
[Azure Functions](https://azure.microsoft.com/en-gb/services/functions/).
It's nice to have this option, especially for experimental bots or
practice ones, since you pay by usage, it works out very good value if
your bot never handles a lot of requests, otherwise you would have to
pay for a server to be available at all times.

Since most of the components of Microsoft's framework are freely
downloadable development tools, the cost of using their framework is
very low. You essentially just pay for hosting the bot, whether that
is on Azure or some other platform. The cloud component of their
framework, the Bot Service, is also free for "standard channels",
which includes Facebook Messenger, Slack, Skype and Cortana, and costs
$0.52 per 1,000 messages for "premium channels" which includes web
chat.
