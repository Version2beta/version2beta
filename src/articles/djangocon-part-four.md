---
pagetitle: DjangoCon, part four
longtitle: Notes from the final day of talks at DjangoCon 2011.
tags: community
author: Rob Martin
published: 2011-09-11 16:55
snippet: Here's the recap of day three, the last day of the talks. Apparently I took good notes on day three, since this is by far the longest post, and the one it took me longest to produce. It was, indubitably, an excellent day.
---

Note: This is part four of four on DjangoCon 2011 in Portland, Oregon, September 6 - 10, 2011. Read all four parts:

  * [one][djone]
  * [two][djtwo]
  * [three][djthree]
  * [four][djfour]

[djone]: /articles/djangocon-part-one
[djtwo]: /articles/djangocon-part-two
[djthree]: /articles/djangocon-part-three
[djfour]: /articles/djangocon-part-four

Here's the recap of day three, the last day of the talks. Apparently I took good notes on day three, since this is by far the longest post, and the one it took me longest to produce. It was, indubitably, an excellent day.

## DjangoCon agenda

### Keynote: Glyph Lefkowitz on Why does Django hate Python

In 2008 Cal Henderson gave a DjangoCon speech entitled "Why I Hate Django". Apparently it provided an opportunity for Django core developers to demonstrate gracefulness and generosity. The speech has also created a legacy. 2011's Why I Hate Django keynote was given by Glyph Lefkowitz, founder of the Twisted framework project. Glyph's particular flavor was not why he hates Django (indeed, he'd only tried to install it once before writing the speech) but why Django hates Python. His premise is that, if Django didn't hate Python, we might start using more Python (and fewer tools that are not based on Python.) "It is not enough that your system be well designed. It needs to be consistently designed as well."

In order to assist Djangonauts and developers in moving toward a more Pythonic environment, Glyph recommended a number of projects we might wish to consider. It may be more accurate to say that Glyph challenged the Django community to use more Python, including these projects. (I'm breaking my style guideline on footnotes over in-line links for this list, since it's basically a list of links.)

* Fabric: [Fabric][] is a library and framework for performing systems administration tasks, both locally and over a network using SSH. I'd heard of Fabric prior to DjangoCon, but not used it. Using Fabric will be one of the key benefits I got from this year's conference.
* WSGI and Web servers
    * FAPWS: FAPWS stands for [Fast Asynchronous Python Web Server][FAPWS]. It's WSGI-compliant with two primary goals: keep it small, and keep it asynchronous.
    * Spawning: [Spawning][] is a multi-process, multi-threaded, non-blocking WSGI compliant web server. Eric Florenzano wrote about [using Spawning and Django together][DjangoSpawning].
    * Tornado: [Tornado][] is the open-source version of a Web server written to run [FriendFeed][]. It is non-blocking, relatively fast, and includes some of the tools they use at FriendFeed.
    * Gunicorn: [Gunicorn][] is a Python fork of the [Ruby Unicorn project][Unicorn], a prefork worker model WSGI web server.
    * Cogen: [Cogen][] is a library for network programming using coroutines via enhanced generators. I don't understand it either, but it provides a WSGI server and is asynchronous.
    * Twisted Web: [Twisted Web][] is the HTTP portion of Twisted, an event-driven networking engine.[^twisted] It may be important to note that this is the project that Glyph heads.
* Lamson Project: [Lamson][] is a Python-based MTA, SMTP server and library. While that probably says enough, I want to add it can use anything Python can use for storing it's data, which of course includes the Django ORM as well as CouchDB, MongoDB, and many other options. I'm pretty excited about Lamson.
* PyDNS: [PyDNS][] is a Python library for performing DNS lookups.
* PyCron: Glyph, maybe you were just stretching at this point, looking for more applications? I found two pycrons. Neither are in PyPi. One doesn't seem to include source. [Here is the other.][pycron]
* Python Sched library: [sched][] is the Python event scheduler library.

Glyph had much more to say in his keynote, much of it about the overall monolithic structure of Django. Really, I think it boils down to "Django is not particularly Pythonic." But that's beyond my pay grade right now &mdash; I am improving my Django skills so that might work with more customers. I am not asking to join the core development team in planning Django 2.0.[^django2.0]

[Fabric]: http://www.fabfile.org "Fabric"
[FAPWS]: http://www.fapws.org/ "FAPWS Fast Asynchronous Python Web Server"
[Spawning]: http://pypi.python.org/pypi/Spawning/0.7 "PyPi page on spawning"
[DjangoSpawning]: http://www.eflorenzano.com/blog/post/spawning-django/ "Using Spawning and Django together from Eric Florenzano's blog"
[Tornado]: http://www.tornadoweb.org/ "Scalable, non-blocking web server written in Python"
[FriendFeed]: http://friendfeed.com/ "FriendFeed's web site"
[Gunicorn]: http://gunicorn.org/ "Prefork worker model web server"
[Unicorn]: http://unicorn.bogomips.org/ "Ruby Unicorn project"
[Cogen]: http://code.google.com/p/cogen/ "Python-based WSGI web server"
[Twisted Web]: http://twistedmatrix.com/trac/wiki/TwistedWeb "Web component of the Twisted Matrix event-driven network engine"
[Lamson]: http://lamsonproject.org/ "Python SMTP server"
[PyDNS]: http://pydns.sourceforge.net/ "Python DNS library"
[pycron]: http://pycron.sourceforge.net/ "Python cron engine"
[sched]: http://docs.python.org/library/sched.html "Python event scheduler library"

[^twisted]: It is fair to say that Twisted is why I got involved in Python programming. When I first read about it, maybe 3 or 4 years ago, I was fascinated - but since I wasn't actually developing code at that level (pretty much everything was PHP at that point) and I had done no Python programming, I set it aside with a mental note to learn Python someday so I could use Twisted.
[^django2.0]: In his own keynote, Jacob Kaplan-Moss explained how there would be a Django 2.0 only because "Django 1.11" sounded stupid. What I took him to mean is that Django's development would be evolutionary, not revolutionary. Django 2.0 will be much like (and backward-compatible with) Django 1.9.

### Advanced django forms

Danny Greenfeld and Miguel Araujo proposed and then demonstrated a more thoughtful application of The Zen of Python[^zen] and Spartan Programming[^spartan] to Django forms. Some key points for me:

* Limit vertical complexity
* Limit conditionals
* Flat is better than nested

A few more notes I took for making Django forms easier for me in the future:

* See [Jacob Kaplan-Moss' post on Dynamic Form Generation][jkmforms]
* Check out [django-uni-forms][uniforms], especially since it is Section 508 compliant
* Also look at [django-floppyforms][floppyforms].

[Danny Greenfeld and Miguel Araujo's slides](http://www.slideshare.net/pydanny/advanced-django-forms-usage)

[^zen]: The [Zen of Python][zen], also known as PEP-20, is Tim Peter's collection of aphorisms and guiding principles for Python's design, and design in Python. It's always available at a Python prompt by typing `import this`.
[zen]: http://www.python.org/dev/peps/pep-0020/ "The Zen of Python"
[^spartan]: While [spartan programming][spartan] can be described as a coding style guide, it goes beyond that. Like the Zen of Python, spartan programming brings principles to programming that inform the creation of the code, not just its appearance. The key principles of spartan programming are simplicity and minimalism.
[spartan]: http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Spartan_programming "Spartan Programming"
[jkmforms]: http://jacobian.org/writing/dynamic-form-generation/ "Jacob Kaplan-Moss provides a description of how Django might handle dynamic forms"
[uniforms]: http://readthedocs.org/docs/django-uni-form/en/latest/ "django-uni-form at Read the Docs"
[floppyforms]: http://django-floppyforms.readthedocs.org/en/latest/ "dango-floppyforms at Read the Docs"

### Teaching Django to comrades

Issac Kelly gave some excellent starting advice, which is good since I'm still starting in many ways.

Some key troublespots:

* The ORM
* Reverse relations
* Migrations
* Forms, forms, forms
* Signals
* URLs
* Deployment

Of course, it might have been easier to list the areas that are not key troublespots...

I particularly liked Issac's Axioms:

1. There is a method for that. Corollary: If you're new and it's hard, you're probably doing it wrong.
2. There is a Django way of doing this. Corollary: Don't fight the system until you are assured of victory.

### Deployment, daemons, and datacenters

I wasn't sure if I'd need to read five years of Andrew Godwin's blog in order to describe him well enough. He is young and brilliant, in a polite, relatively unassuming way. I like Andrew; he impresses me. And his presentation was good too &mdash; solid mechanics and good advice, some of which I recorded:

* ep.io's standard stack is nginx (for static files and gzipping), gunicorn, postgres 9, redis, and virtualenv
* For higher loads, Andrew says:
    * Use Varnish or other upstream caching
    * Use HAProxy or nginx for load balancing
    * Give PostgreSQL more resources
* Keep staging identical to production
* Redis is easy to setup and use
* Ship long-running tasks off. Use Celery or a worker solution.
* Don't use SQLite in production
* Use transactions
* Plan so you can always add another machine.
* Keep things loosely coupled - simple components loosely connected are easy to troubleshoot
* Anything you've done at least three times should be automated
* ZeroMQ is really, really nice to have.
* MongoDB and Redis will both lose data when they are running low on disk space.
* Regarding backups and redundancy
    * A Postgres slave is not a backup
    * RAID is not a backup
    * Backup in multiple forms at diverse locations
    * Make sure you can restore from backup on a somewhat regular basis
    * Always make the backup machine pull the backups, not production push

I didn't know about that last one. In fact, for much of my backup process that wouldn't work - Amazon S3, for example, cannot pull files. But I'm curious about this.

I don't know that Andrew exactly promoted this, but I put in my notes to make backups progressive. I've thought of this before, too. Perhaps ep.io is doing it. Here is a progressive schedule of backups to keep:

* First of year
* First of month
* First of week

### Content ain't a thing: web scraping

I missed the first half of this session, and decided not to take notes on the second half. While much of what the presenter offered was technically interesting, I found myself increasingly bothered by the blasé disregard for intellectual property rights on the web. It's not that the speaker did not give some homage to the concept, just that a cultivated ability to split hairs was obviously a part of her professional upbringing.

So no further notes on the topic.

### Cache rules everything around me

Especially on Thursday, the last day of talks, there were quite a few tag-team presentations. Some of them were so highly tuned, they finished each other's sentences. Each one I saw was impressive.

Jacob Burch and Noah Silas presented on caching. Jacob works with Frank Wiles and now Jacob Kaplan-Moss at Revolution Systems. I don't actually know where Noah is from, but he certainly knew his stuff too.

First, I liked the warnings.

Don't cache:

* Caching adds complexity. Don't do it.
* Caching adds additional points of failure. Don't do it.
* Modern databases are "stupidly optimized" (by which they seem to mean fast). Maybe you don't even need to cache. Don't do it.
* As the quote goes, there are only two hard things in computer science. Naming things and cache invalidation. Don't do it.

If you do cache:

* Your application should never ever rely on caching.
* The Super Awesome Fun Time Rule for Minimizing Sadness: You should have one canonical data source, and it is not your cache.

From here, they went into a number of caching patterns. I'm not going to translate all my notes here. I took too many for just part of one blog post. Suffice with just a few.

The "New Hotness" model:

* Cache indefinitely - for as long as the back-end will allow.
* Invalidate explicitly - replace, don't delete

"Publish Cache"

* Put entire responses into cache
* Implementation in Django is easy - just drop in middleware
* Cache invalidation is probably easy too, when the blog post, article, etc. is updated
* Might be difficult with dynamic page elements

Django.core.cache is simple to setup and supports multiple caching backends. Don't use these backends:

* db.DatabaseCache
* filebased.FileBasedCache
* locmem.LocMemCache
* dummy.DummyCache

These are okay:

* memcached.MemcachedCache
* memcached.PyLibMCCache

And these are good for the Publish Cache pattern:

* django.views.decorators.cache.cache_page
* django.middleware.cache.UpdateCacheMiddleware

Third party enhancements for Django:

* django-newcache
* johnny-cache
* django-cache-machine
* django-autocache

And finally, they recommend that it might be good to create a "Does Not Exist" cache entry, something like `!!!DNE!!!`. This can come in handy if you ever get slammed for something that, no matter how many times the back-end is asked for it, you cannot create it. Putting `!!!DNE!!!` in cache can prevent the extra load of discovering over and over that it does not exist.
