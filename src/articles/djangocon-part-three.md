---
pagetitle: DjangoCon, part three
longtitle: Notes from the second day of talks at DjangoCon 2011.
tags: community
author: Rob Martin
published: 2011-09-08 07:45
snippet: Day two is done, and I'm trying to do better at this. I definitely have better notes than yesterday. I have slightly fewer of them too, since the South session was absolutely worthless to me, and I blew off Tilting at Windmills to go up to the room with a stomach ache and a customer who needed help.
---

Note: This is part three of four on DjangoCon 2011 in Portland, Oregon, September 6 - 10, 2011. Read all four parts:

  * [one][djone]
  * [two][djtwo]
  * [three][djthree]
  * [four][djfour]

[djone]: /articles/djangocon-part-one
[djtwo]: /articles/djangocon-part-two
[djthree]: /articles/djangocon-part-three
[djfour]: /articles/djangocon-part-four

Day two is done, and I'm trying to do better at this. I definitely have better notes than yesterday. I have slightly fewer of them too, since the South session was absolutely worthless to me, and I blew off Tilting at Windmills to go up to the room with a stomach ache and a customer who needed help.

## DjangoCon agenda

Here's the recap of day two:

### Lightning talks

By the schedule, there were 90 minutes of lightning talks happening in the morning. I guess when 9:00AM rolled around, there were only three submitted so they postponed the start time. This gave me enough impetus to put together my own, on using Prezi for presentations. Here it is. (This is my first time embedding media in this blog. It may look crappy until I spend more time formatting. If so, please excuse the visual disruption; I will try to make it better soon.)

<div class="prezi-player"><style type="text/css" media="screen">.prezi-player { width: 550px; } .prezi-player-links { text-align: center; }</style><object id="prezi_ntrlqxhxpzbv" name="prezi_ntrlqxhxpzbv" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="550" height="400"><param name="movie" value="http://prezi.com/bin/preziloader.swf"/><param name="allowfullscreen" value="true"/><param name="allowscriptaccess" value="always"/><param name="bgcolor" value="#ffffff"/><param name="flashvars" value="prezi_id=ntrlqxhxpzbv&amp;lock_to_path=1&amp;color=ffffff&amp;autoplay=no&amp;autohide_ctrls=0"/><embed id="preziEmbed_ntrlqxhxpzbv" name="preziEmbed_ntrlqxhxpzbv" src="http://prezi.com/bin/preziloader.swf" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="550" height="400" bgcolor="#ffffff" flashvars="prezi_id=ntrlqxhxpzbv&amp;lock_to_path=1&amp;color=ffffff&amp;autoplay=no&amp;autohide_ctrls=0"></embed></object><div class="prezi-player-links"><p><a title=" No description " href="http://prezi.com/ntrlqxhxpzbv/a-prezi-on-prezi-for-djangocon/">A Prezi on Prezi for DjangoCon</a> on <a href="http://prezi.com">Prezi</a></p></div></div>

### Keynote: Brad Fitzpatrick


Laid-back, easy-going guy who receives a lot of emails. Of course, he's written some pretty important open source software, like memcached[^memcached], and an Android app that runs on a server in his garage scanning for his phone's SSID so that when he rides up on his motorcycle it can open the garage door automatically[^garage].

[Brad Fitzpatrick's slides](http://bradfitz.com/talks/2011-09-Djangocon/)

[^memcached]: [memcached][memcached] gives developers a place to store key-value pairs where they can be quickly retrieved, more quickly than the database or by calculation.
[memcached]: http://memcached.org/ "High performance distributed memory object cacheing system"
[^garage]: No, really. Not kidding. [A garage door opener][garage].
[garage]: http://www.appbrain.com/app/garage-door-opener-(x10)/com.danga.garagedoor "X10 garage door opener for Android"

### Restful API's, promises and lies

Tareque Hossain gave an excellent, easy-to-follow introductory presentation on Django REST APIs, with illustrations from PBS children's shows. Really - his opening slide had Elmo on it, which was only the start of visuals borrowed from his employer. His technical examples also came from PBS, of course.

One cool takeaway: JSONP[^jsonp] for sharing APIs across multiple domains.

[Tareque Hossain's slides](http://www.slideshare.net/tarequeh/restful-apis-promises-lies)

[^jsonp]: Here's the [Wikipedia article on JSONP][json].
[jsonp]: http://en.wikipedia.org/wiki/JSONP "Wikipedia article about JSONP."

### A Little South Sanity

I really tried to get something out of this session. I can totally see how useful South could be, despite my initial misimpression that it was useful only in the largest, most drawn out installations. Unfortunately, Brian Luft did much of the presentation live at the terminal and it wasn't working, so I have no clue which parts were South and which parts were Brian's attempts to get it working. It was like I was the customer showing up for training, looking over the lead developer's shoulder. Which is something I'm sure I've done with customers before. Many times.

### Building APIs with TastyPie

Isaac Kelly did in fact convince me I could build an API with TastyPie. Someday I'll have to prove that, right?

I hadn't known about json.tool for pretty printing JSON from the command line, but that looks useful too:

```
$ echo '{"json":"obj"}' | python -mjson.tool
{
  "json": "obj"
}
```

[^json]: It's part of the Python json library, readily accessible. See [json docs here][json].
[json]: http://docs.python.org/library/json.html "JSON encoder and decoder"

### Stop Tilting at Windmills: Spotting Bottlenecks

By the end of the JSON session I was already fielding voicemail, email, and text messages from a customer back home. One of us had managed to break his brand new Box.net uploader library.[^multiup] I spent the Stop Tilting at Windmills session tilting at windmills.

[^multiup]: My [multiup jQuery plugin][multiup] was part of that project. I did not blog on building a Box.net API library for PHP, although I did do exactly that, the night before delivery, when I found out that the published PHP library Box.net offered wasn't just poor quality, it was incomplete. For example, the upload functionality was not implemented at all.
[multiup]: /archive/2011/jquery-multiup-plugin.html "jQuery plugin for multiple files"

### Safely Deploying on the Cutting Edge

This session was very cool. Best parts included:

* a good branching model for git[^branch]

* a vocabulary of deployment verbs implemented in scripts (pull, build, tag, sync, install, rollback, start, stop, restart, reload)

* a reminder that the startup processes (init.d, upstart, etc) are just processes written by other developers, and sometimes it makes sense to roll your own

The session next door, "Best Practices for Front-End Django Developers", was clearly very popular as well. Roughly half the conference attendees were in the same session I was. Next door, it sounded like they had about one-and-a-half times as many people clapping.

[^branch]: Eric gave a link to "A Successful Git Branching Model" post at nvie.com as an example similar, but more complicated, than their model.
[branch]: http://nvie.com/posts/a-successful-git-branching-model/ "A Successful Git Branching Model"

### Benevolent Designer For Life's Keynote - Designers Make It Go to Eleven

Idan is cool, an excellent choice. I'm guessing that, just as design implements the physical interface between human and machine - where the skin meets metal - Idan may do the same for the Django community.

[Idan Gazit's slides](http://www.scribd.com/doc/64286481/Designers-Make-it-Go-to-Eleven)
