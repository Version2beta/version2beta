---
pagetitle: DjangoCon, part two
longtitle: Notes from the first day of talks at DjangoCon 2011.
tags: community
author: Rob Martin
published: 2011-09-07 12:04
snippet: Oh my, I'm not good at this. There are people around live-blogging (and live-noting) the conference, and I'm scraping the sleepiness off my face enough to see the screen, only to realize I don't actually remember yesterday very well. I may be exagerating a little, but I did not take adequate notes (sorry, PyDanny - I heard you on this, really I did.)
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

Oh my, I'm not good at this. There are people around live-blogging (and live-noting) the conference, and I'm scraping the sleepiness off my face enough to see the screen, only to realize I don't actually remember yesterday very well. I may be exagerating a little, but I did not take adequate notes (sorry, PyDanny - I heard you on this, really I did.)

## DjangoCon agenda

Here's the recap of my first day:

### David Eaves' keynote on the science of community

David Eaves is awesome.[^eaves] He doesn't know much about the Django community, but he clearly knows about communities, including open source communities. Mostly he talked about two topics: using metrics to track and plan within a community, and using negotiation theory to include more people more effectively. Here was an important, but only peripheral, take-away: the involvement of women in an open source project is a key indicator of the health of the project.

### From designer to Django'er in six weeks

I understand that Alex was ill in the morning, so his slot went to Adam Nelson for 'Testing with Lettuce and Splinter'. I arrived about four minutes in, and left about eight minutes in. I'm sure it was a valuable talk. I've even heard that from someone who stayed. I missed the discussion on BDD (behavior driven development), and given that my testing experience is in many ways nascent, I decided that learning alternatives was further out than I was ready for.

What I did instead was listen to Tracy Osborn's[^limedaring] fascinating 'From Designer to Django'er in Six Weeks: A Story from Solo Founder'.[^solo] Anecdotes of learning not just Django, but of becoming an entrepreneur with Django.[^invite]

Alex did present in the afternoon, opposite Frank Wiles' PostgreSQL Performance talk, so I did not see him then either.

[Tracy Osborn's slides](http://www.slideshare.net/limedaring/from-designer-to-djangoer-in-six-weeks-a-story-from-solo-founder)

### Confessions of Joe Developer

Danny claims to be lazy and stupid, which is not only a solid rhetorical tool but also a good starting point for learning complex systems. I half expected to hear a reference to Larry Walls' three virtues of a good programmer.[^virtues] (In fact, it would have fit right in, except for the language mismatch.)

A good portion of his presentation described various methods for saving time, not relying on memorization, and the merits of doing things "the dumb way". His example contrasts urllib2 with the requests library[^requests].

Also terrifically important, Danny talked about diversity at the conference - PyLadies,[^pyladies] women in tech, our wives and daughters, the role of men in creating open and diverse environments. I like the thought, and believe Danny's sincere desire to make it all better. At the same time, as men we risk being the patron by being involved at all. There's much more to be said here, but I'm reluctant to say it for fear my position stands counter to the enlightened attitudes around DjangoCon. It does not. I salute the efforts to include women, to build an inclusive environment and to identify narratives and behaviors that interfere. I think I'll stick with helping my daughter with her AP Physics, AP Calculus, and AP Statistics homework. If she even needs help.

[Danny Greenfeld's Joe Developer slides](http://www.slideshare.net/pydanny/confessions-of-a-joe-developer)

### The story and tech of Read the Docs

I like devops.[^devops] I'm fascinated by it. Eric Holscher's discussion on Read the Doc kept my attention as much as anything for how they solved the devops questions - clearly, that is the essence of Eric's work, right?

### Testing - The developer strikes back

This was the densest presentation I've seen at Djangon yet. Sandy[^sandy] laid it down at 10 MBPS, I swear. I knew little about "real" testing practices before I went in, and now I have enough familiarity with the universe of options, I'm highly likely to recognize them when I finally sit down and learn them right.

[Sandy Strong's slides](https://docs.google.com/present/view?id=0AVthC0Z3iw8DZGRrdnFzeGdfN2c5bWJ6d2Y1)

### Secrets of PostgreSQL performance

I've known of Frank Wiles and Revolution Systems[^revsys] for about as long as I've used PostgreSQL, so much of what he offered wasn't brand new to me. But some of it was new - tablespaces, for instance.

[Frank Wiles' slides](http://media.revsys.com/talks/djangocon/2011/secrets-of-postgresql-performance.pdf)

[^eaves]: [David Eave's about page][eaves] is a good starting point, but don't stop there. Spend a week or two reading his work, and following links.

[eaves]: http://eaves.ca

[^virtues]: The three virtues of a good programmer are laziness, impatience, and hubris, at least according to [Larry Wall][virtues] of Perl fame.

[virtues]: http://en.wikipedia.org/wiki/Larry_Wall "Wikipedia's Larry Wall page."

[^limedaring]: [Tracy Osborne's LimeDaring.com website][limedaring].

[limedaring]: http://www.limedaring.com/

[^solo]: Tracy blogs the experience in [I’m a Designer Who Learned Django and Launched her First Webapp in 6 Weeks][solo].

[solo]: http://www.limedaring.com/im-a-designer-who-learned-django-and-launched-her-first-webapp-in-6-weeks/ "Tracy's blog post about launching a Django site in 6 weeks."

[^invite]: The product of her efforts and the subject of her presentation: [weddinginvitelove.com][invite].

[invite]: http://www.weddinginvitelove.com/ "Tracy Osborne's Django site extraordinary"

[^requests]: I tend to do things "the smart way", so this is a gem for me. PyDanny introduces me in one fell swoop to both the [HTTP requests library][requests] and to [Kenneth Reitz][reitz], who says right on the front of his site that the Library of Congress, National Geographic, and Discovery Channel all use his software.

[reitz]: http://kennethreitz.com/ "Kenneth Reitz's website"

[requests]: http://pypi.python.org/pypi/requests "Python HTTP for humans"

[^pyladies]: I don't remember exactly how it happened that we came to DjangoCon, but I do know that early in the process my employer and wife informed me she was thinking of sponsoring a PyLadies position at DjangoCon. I pouted at her in reply, "You'd send a stranger to DjangoCon, but not me?" It would have been nice if, as a company, we could have sent ourselves and sponsored a position , but we couldn't, not this year. PyLadies are cool though - check them out.

[pyladies]: http://pyladies.com/ "PyLadies"

[^devops]: Devops are the collaboration of systems administration, network administration, and software development. In other words, the integration of my schizophrenia. [Other people give other definitions.][devops]
[devops]: http://dev2ops.org/blog/2010/2/22/what-is-devops.html "Another devops definition."

[^sandy]: [Sandy Strong][sandy], Django developer, and besides telling you she kicked ass and took numbers on the stage at DjangoCon, I know little about her.
[sandy]: http://twitter.com/#!/sandymahalo "Sandy on Twitter"

[^revsys]: I knew of [Revolution Systems][revsys] from PostgreSQL work, but I didn't know of the connections with Django. I *think* Frank worked at The World Company a decade ago. I know that Jacob Kaplan-Moss is now at RevSys, which certainly seems to say a lot to me.
[revsys]: http://www.revsys.com/
