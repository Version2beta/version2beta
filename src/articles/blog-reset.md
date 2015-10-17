---
pagetitle: Blog reset
longtitle: How and why I started over with my blog, just three months after launching it.
tags: dev
author: Rob Martin
published: 2011-08-25 08:27
snippet: My blog had been hosted on a legacy shared server account that I don't manage, running Wordpress. I was frankly embarrased to tweet links to it - often it wouldn't come up at all. Now that's all changed. Now my blog is on Django. (But only kinda.)
---

My blog had been hosted on a legacy shared server account that I don't manage, running Wordpress. I was frankly embarrased to tweet links to it - often it wouldn't come up at all. Now that's all changed. Now my blog is on Django. (But only kinda.)

A month ago I heard from a potential customer in Chicago who needs to move a site from Wordpress to Django.[^django] They'd heard about me in particular from a colleague, and wanted to know if I could help.

Of course I could! I've been learning Django for months. I even have the Django book.[^djangobook] I've even *read* the Django book. Parts of it, anyway. And I do have tickets for DjangoCon[^djangocon] in Portland next month.

I'm afraid the colleague might have oversold me. It wasn't complete radio silence when I said I didn't have any production Django sites she could look at, but it was close.

"But I was thinking of moving my blog onto Django. I could probably have that done over the weekend." I could hear her slight sigh of relief.

I didn't move my blog onto Django that weekend. What I did with my weekend was build out two sets of high-availability server pairs and write up a how-to on the same.[^ha-pairs] Then, at 5:30pm on the night before my 6:15am train to Chicago to meet with this customer, I sat down to figure out how I could get my blog onto Django, quickly.

I was already somewhat familiar with Hyde[^hyde]. It's a static site generator written in Python, inspired by a remarkably similar Jekyll[^jekyll] written in Ruby. Conveniently, Hyde is also based on Django, using both the settings.py file and Django templates, so I'd be able to use some of what I already knew to show off what I might be able to do for a customer using Django. Because that's what every customer needs, right? A small, unobtrusive, under-designed blog-like website that uses Django templates?

My whole blog did not get moved that evening, but I did post the high-availability write-up in a blog section of a website I called "proof of concept". That was convenient, since the new site is hosted on one of the server pairs I'd just built, and the write-up was a key take-away for my presentation at Web414[^web414] the next night on cloud hosting.

A couple of weeks passed before I got back to the project, but I did finally move my blog. I also improved the design some, though of course it's still small, unobtrusive, under-designed, and blog-like. I did away with almost all of my inline links in blog posts, opting for footnotes instead. Not only does this make the reading easier (and less spammy-looking), it gives me more room to be snarky[^snarky] out-of-band. (There are many fine examples of footnoting bloggers, but as usual Barbara[^barbara] has the most influence on me.) I'd also been wanting to use Disqus for comments, and figured it'd be best to do that while I only have 8 comments to figure out what to do with. (Note: if you are one of the people who'd commented on my old blog, please accept my apology as I decide how, when, and if to move them.)

I haven't heard back from the Chicago customer yet, which is probably okay because they wanted freelance, and I would want to run it through QMUXS.[^qmuxs] But in spite of the dubious benefit of the sales call, I worked through the new high-availability challenges, built up the new servers, got to work with Django more, and built a new fast fast fast website for version2beta.

I hope you enjoy it.

[^django]: [Django][] is the web framework for perfectionists with deadlines. Often, it's also the web framework for perfectionists with deadlines on *really big websites*, like [Disqus][], the [Washington Post][washpost], and the [New York Times][nytimes].

[django]: https://www.djangoproject.com/ "Django makes it easier to build web applications more quickly and with less code."

[disqus]: http://disqus.com "Disqus is a cloud-based comment and discussion platform"

[^djangobook]: [_The Django Book_][djangobook] is about working with Django. It's published under the Gnu Free Document License.

[djangobook]: http://www.djangobook.com/

[^djangocon]: [DjangoCon][] is the Django community conference. This year it's happening in Portland, OR on September 6 - 10. We're going.

[djangocon]: http://djangocon.us/ "DjangoCon. Three days of talks and two days of sprints."

[^ha-pairs]: See my blog post, "[High Availability Linode Pairs][ha-pairs]".

[ha-pairs]: http://version2beta.com/articles/high-availability-linode-pairs "Something like a recipe for creating database and application servers that failover on each other, using Ubuntu and Linode."

[^hyde]: I like [Hyde][] and I'm pretty impressed with it. At least, at version 0.4. It's also getting a complete rewrite and is currently available in a [version 0.8 flavor][hyde0.8] as well that uses Pocoo's Jinja2 templates instead of Django's templates. I don't know how I feel about that version yet.

[hyde]: http://ringce.com/hyde "Hyde version 0.4"

[hyde0.8]: http://hyde.github.com/ "Hyde version 0.8"

[^jekyll]: I already told you that Jekyll is like a spin-off of Hyde, except that it came first, right? Really, [Jekyll][] is very cool. I don't program much in Ruby, but I know enough to understand why programmers who use it love it. One very interesting site running on Jekyll is [The Cyborg Institute][cyborg], not the Wiki but all of the static pages. Also, both Jekyll and Hyde do this cool thing where you can host a site right from GitHub. I haven't tried it (need to justify my servers, right?) but it certainly has some advantages.

[jekyll]: http://jekyllrb.com/ "Jekyll static site generator"

[cyborg]: http://cyborginstitute.com/about/ "About the Cyborg Institute."

[^web414]: [Web414][] is our local professional web designer/developer/master/writer/worker/etc. group. We have good people in Milwaukee.

[web414]: http://web414.com/ "Web414 is Milwaukee's web community."

[^snarky]: You didn't really follow a footnote for "snarky", did you?

[^barbara]: Barbara footnotes her footnotes. I am not so dedicated. But if you want to see, check out her [post-feminist rant on Blogher][blogher], written from her hotel room at the convention. It's not the best example of footnoted footnotes, but she says some pretty important stuff in it. If you want to see gratuitous footnoting in action, try her [Life is in the Subtext][lst] post.

[blogher]: http://www.barbaralmhandley.com/blog/?p=1782 "A rant and a ramble."

[lst]: http://www.barbaralmhandley.com/blog/?p=1758 "Life is in the subtext."

[^qmuxs]: [QMUXS is Quintessential Mischief LLC][qmuxs], the company that Barbara owns and for which I work. As I've said elsewhere, I’m available for freelance work only under limited circumstances. Generally I determine what these circumstances are on a case-by-case basis, in cooperation with my employer. I don’t like my employer to think I’m competing with her. It’s not good for our marriage.

[qmuxs]: http://www.qmuxs.com "Quintessential Mischief's website belongs at this address. Someday."
