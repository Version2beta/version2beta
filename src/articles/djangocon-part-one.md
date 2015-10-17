---
pagetitle: DjangoCon, part one
longtitle: My DjangoCon 2011 prep notes.
tags: community
author: Rob Martin
published: 2011-09-04 12:33
snippet: It's two days before DjangoCon, I'm on a plane to Portland, and I've mostly been spending my time reading the Django Book. That has me thinking about what I expect from the conference.
---

Note: This is part one of four on DjangoCon 2011 in Portland, Oregon, September 6 - 10, 2011. Read all four parts:

  * [one][djone]
  * [two][djtwo]
  * [three][djthree]
  * [four][djfour]

[djone]: /articles/djangocon-part-one
[djtwo]: /articles/djangocon-part-two
[djthree]: /articles/djangocon-part-three
[djfour]: /articles/djangocon-part-four

It's two days before DjangoCon, I'm on a plane to Portland, and I've mostly been spending my time reading the Django Book. That has me thinking about what I expect from the conference.

## DjangoCon agenda

You'll be able to recognize me at DjangoCon.[^djangocon] I have all of the sessions printed and three-hole punched inside a 1.5" binder, with my schedule inserted in the front cover. My schedule looks reasonably good - I have a session I want to see during every session, and in two or three slots, I have both sessions selected. I'm hoping my wife will be willing to attend the my counter-sessions.

## Tuesday

### Alex Gaynor, Summer in the wild

Optimization is good and I always want to feel reasonably confident I can make things faster, so I look forward to this discussion of PyPy. But I'm also curious to hear about Alex's position at Quora, a company  I expect to fail, which probably indicates it will be wildly successful.

### Confessions of Joe Developer

Joe's real name is @PyDanny,[^pydanny] which is why I plan to attend this session. Danny promises the benefit of his experience. I'll buy that.

### The story and tech of Read the Docs

When I first visited readthedocs.org,[^readthedocs] I wondered how they got anyone to put in the effort to maintain their centralized database of software manuals. I learned enough more to make the important connections between Sphinx, GitHub, and Django to make the automation connection. Now I'm fascinated with how Read The Docs came about and how it works. This session is one of my highest priorities.

### Testing - The developer strikes back

I don't know who Sandy is, but I hope she or he is going to help me greatly improve my understanding and use of unit tests. I've been coding a long time, like over thirty years now, but generally by myself. Shortcuts have happened, but I know I do not want to develop code without tests any more.

### Secrets of PostgreSQL performance

I have over the years had a few opportunities to optimize databases, most recently PostgreSQL. I've used three different resources for that task, and they all came from Frank Wiles.[^revsys] Hell yeah I'm going to hear him talk.

## Wednesday

### RESTful APIs - promises and lies

You may have heard the term "mobile first". I'm beginning to wonder if we shouldn't be looking at the API goals of a website first. I'm serious. Even the semantic web has goals related to sites as applications - what's my address, hours of operation, etc. What web site has no opportunity to share?

### Real-world Django deployment using Chef

Scale is one big reason I am learning Django and attending DjangoCon at all. Besides, it sounds like Glyph is going to complain about Chef in his keynote address "Why does Django hate Python?" Might be good to have more context with Chef, as Glyph specifically mentions it.

### Building APIs in Django with Tastypie

See above on APIs. Now add in Tastypie, which does sounds interesting.

### Making the Django ORM multilingual

I've only had the opportunity to work on a couple of multilingual websites so far, but I expect that frequency to shift. I don't have a clue yet how Django does i18n, translation, or localization. I'm worried it doesn't do it well, based on the description of this session.

### Stop tilting at windmills - Spotting bottlenecks

This session promises the kind of good advice you only get from someone _experienced_. But just as important to me, it appears that the best Django debugging tools will be demonstrated and potentially discussed.

### Safely deploying on the cutting edge

Urban Airship's Eric Holscher[^urbanairship]  talking about Fabric, Gunicorn, Virtualenv, Rsync, Supervisord, and Python in fully isolated server environments? Oh yeah. Yes yes yes. This session is like sysadmin porn.[^nomore]

## Thursday

### Advanced Django Form usage

@PyDanny's back again, talking about forms. We have a customer who does a lot with forms, and I've already redesigned everything for them once, more than a year ago, to drastically improve the usability of their forms. That was the front side - how good can it get on the back side?

### Pinax after three years: lessons learnt and the way forward

I want a content management system that my customers will rave about. I have no idea what that is with Django, if there even is someone complete and open source. Learning more about Pinax seems like a good direction to go, though.

### Advanced security topics

'nuf said.

### Write the friendly manual

There is some really good stuff going on in the Python world with documentation. Sure, I've read most of the Django book, but have you looked at Flask's documentation? Geez, who has time to not only code a cool platform like Flask, but also put out documentation of that quality? There has to be some secrets. I plan to uncover them.

### Content ain't a thing: Web scraping with our favorite Python libraries

I'm bracketing my DjangoCon experience, right? Share (APIs with Tastypie, etc.) and share (Web scraping) alike!

### Cache rules everything around me

I'm back to scale, and systems administration, with this last formal session.

## Find me?

So these are my picks for DjangoCon - find me at any of these sessions, strike up a conversation, and maybe even talk about sprints. I'm the guy with the long beard, big laugh, and contemplative look, trying to figure out how to put this new knowledge to use professionally.

[^djangocon]: [DjangoCon 2011][djangocon] in Portland, Oregon. Starts Tuesday; we're early. My wife lived in Eugene, OR for 16 years before we got married, and for just three days after we got married. We have people to see, and mountains and trees to visit.

[djangocon]: http://www.djangocon.us "DjangoCon."

[^pydanny]: [@pydanny][pydanny] is Daniel Greenfield, and as Pythonista Djangonauts go, he's up there. So is his fiancée [Audrey Roy][audreyr], who I discovered on Twitter before I knew who pydanny was. Look both of them up. Talented, dedicated developers with much to share and very generous with it.

[pydanny]: http://twitter.com/#!/pydanny "Daniel Greenfield on Twitter."

[audreyr]: http://twitter.com/#!/audreyr "Audrey Roy on Twitter."

[^readthedocs]: [Read the docs][readthedocs] is this awesome free documentation hosts that gets the docs automatically out of your version control system, like Bazaar, or GitHub. They saw a problem and saw how to make it work better.

[readthedocs]: http://www.readthedocs.org "Read The Docs."

[^revsys]: Frank Wiles' company is [Revolution Systems][revsys] in Lawrence, KS. [Jacob Kaplan-Moss][jacobian], a Django lead developer and co-BFDL, joined in 2009.

[revsys]: http://www.revsys.com "Revolution Systems, LLC."

[jacobian]: http://jacobian.org/ "Jacob Kaplan-Moss' writing."

[^urbanairship]: I didn't know about [Urban Airship][urbanairship] until I read about this session. I mean, I knew something like Urban Airship had to exist, but I didn't know that they were in Portland, running on Django and Python, and had so much interesting stuff happening. I can't leave Milwaukee, but if I were I'd be very interested in Urban Airship.

[urbanairship]: http://urbanairship.com/ "Urban Airship powers mobile development."

[^nomore]: I should provide more footnotes and links, but the hotel wireless latency is too nasty. The next installment may perhaps offer more.
