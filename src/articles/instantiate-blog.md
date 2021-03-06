---
pagetitle: Instantiate Blog
longtitle: How and why I ended up blogging. Again.
author: Rob Martin
published: 2011-05-09 20:15
snippet: The story of how and why I ended up blogging. Again.
---

The story of how and why I ended up blogging. Again.

## Stranger in a strange land.

This is somewhere around blogging attempt number 12 for me. I feel like
the cheerleader on Heroes[^claire] announcing yet another failed try at
offing myself. And here I go again.

Actually, I haven’t done horribly. Some of my blogs had a few readers. 2
or 3 a month even. Some high points:

-   grokd.org – an automated blog pulling news clips on autism. Hundreds
    of readers a month, probably because I didn’t write hardly any of
    the posts. I shut it down when the b2/cafelog[^b2] developers
    announced they were shifting focus to some new project they called
    “WordPress”.
-   closew.org – discussion of community and cooperative living, back
    when I still thought consensus was the greatest political tool since
    pork on sliced bread. Now I favor benevolent dictators[^bdfl] (so long
    as he is me) and anarchy,[^anarchy] especially anarcho-primitivism.[^anarchoprimitivism]
-   woundedpig.com – an attempt to satirize scary conservatives. Took me
    forever to write each post. Turns out I’m not Jon Stewart.

## Look. And feel.

What can I add beyond what I’ve said [on the about page][]? As of this
writing, the blog has an extremely basic theme. One could call it naked,
except that would suggest you could see what lies underneath. Let’s say
it’s unadorned. I’m using the Roots theme[^roots] for these features:

-   HTML5 Boilerplate ([http://html5boilerplate.com/][]) makes
    rock-solid HTML5 sites
-   960.gs ([http://960.gs/][]) makes 960px grid-based design easy
-   Cleaner URLs with a custom .htaccess
-   jQuery [Cycle][] and [FancyBox][] – my two favorite jQuery plugins

Of course, Roots is just a starter theme. Ideally the developer will
still style it, you know, choose those cleaner and more trustworthy
fonts, maybe add a logo, etc.? Take a look at this page. If you’re
seeing what I’m seeing (quite possibly not, since I’m at a different
point in the space-time continuum than you are), then the developer
(a/k/a me, version2beta, rob) has not gotten around to it.

**Updated 8/22/11:** I've moved the blog onto my version2beta.com domain and now I'm using Hyde[^hyde] to generate the site, so I'm not actually using Wordpress, Roots theme, or Apache, or even HTML5Boilerplate. Or FancyBox, jQuery Cycle, or jQuery *anything*. It's all rustic. I've gone native. (But I'll probably get around to making it look more designed eventually.)

**Updated 1/25/13:** Changed it up again. I'll probably blog about the new platform. Basically it's a Flask[^flask] application with Frozen Flask[^fflask] to save a static version, which is then uploaded to S3 and served via Route53.[^aws]

## Poke me.

Look around at what I’ve written. Or maybe what I’m going to write, since so far all I’ve written is this and the about page. Or maybe, what I think I’m going to write. I’ll probably leave comments on, but really, don’t bother. If I’ve inspired a response from you (probably the type of response that deserves an apology), mention [@version2beta][] on Twitter and I’ll see it there. Or, if you can’t comment in less than 126 characters (my handle takes 14 characters with a space), blog about it and tweet that. I have my doubts about blogging (especially me blogging), but one thing it seems good for is inter-blogal discussions.



[^claire]: In the television program [Heroes][], Claire starts and ends the series with a failed suicide attempt. She is unkillable.

[Heroes]: http://en.wikipedia.org/wiki/Heroes_(TV_series)#Cast "Wikipedia article for Heroes"

[^b2]: I was at a meeting a few months ago where everyone had to introduce themselves with their name, Twitter handle, and when they first started using Wordpress. I explained how I stopped using [b2/cafelog][] when they announced they'd be moving their attention to this new project, Wordpress.

[b2/cafelog]: http://en.wikipedia.org/wiki/B2/cafelog#History "Ancient history of blogland"

[^bdfl]: I'm a fan of [benevolent dictatorship][]. I'm also a fan of benevolent-dictators-for-life. If they cease to deserve the title, we can just off 'em.

[benevolent dictatorship]: http://en.wikipedia.org/wiki/Benevolent_dictatorship "See also: philosopher kings"

[^anarchy]: "Anarchy may not be the best form of government, but it's better than no government at all." See also: [Wikipedia article on anarchy][anarchy].

[anarchy]: http://en.wikipedia.org/wiki/Anarchism "Anarchy isn't chaos."

[^anarchoprimitivism]: [Anarcho-primitivism][] is a funny hobby for a geek, but you might be surprised how many of us there are. This may have something to do with the fact that lots of geeks are pretty smart, and it's possible to look around at our world and realize we are ignoring a few constraints.

[anarcho-primitivism]: http://en.wikipedia.org/wiki/Anarcho-primitivism "Another Wikipedia article, this one on anarcho-primitivism."

[on the about page]: http://version2beta.com/about/ "about version2beta's blog"

[^roots]: [Roots theme][] is a starting WordPress theme based on HTML5 Boilerplate and 960.gs

[Roots theme]: http://www.rootstheme.com/ "Roots theme for Wordpress."

[http://html5boilerplate.com/]: http://html5boilerplate.com/

[http://960.gs/]: http://960.gs/

[Cycle]: http://jquery.malsup.com/cycle/ "Malsup's jQuery Cycle. Vrooom."

[FancyBox]: http://fancybox.net/ "Fancybox makes content pop."

[^hyde]: [Hyde][] is a static website generator powered by Python and Django. Unfortunately, it's undergoing a major redesign right now, and I'm a little uncomfortable with the new direction.

[Hyde]: http://ringce.com/hyde

[@version2beta]: http://twitter.com/version2beta "Me, twitterfied"

[Twitter]: http://twitter.com "All of twitter, including me."

[^flask]: [Flask][flask] is a Python microframework written by Armin Ronacher.

[flask]: http://flask.pocoo.org/ "Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions."

[^fflask]: [Freezes a Flask application][fflask] into a set of static files. The result can be hosted without any server-side software other than a traditional web server.

[fflask]: https://github.com/SimonSapin/Frozen-Flask/ "Freezes a Flask application into a set of static files."

[^aws]: [AWS][aws] is a collection of web services provided by Amazon and used by many large scale internet services.

[aws]: http://aws.amazon.com/ "Amazon Web Services"
