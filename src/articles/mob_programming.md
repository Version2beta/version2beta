---
pagetitle: A year of mob programming
longtitle: The first year of my experiment with mob programming
tags: cto
author: Rob Martin
published: 2016-02-10 15:30
snippet: It's been twelve months since I started learning how to program in a mob. This post describes my experiences.
---

A friend of mine works in a computer research lab - the hard working, highly educated bastard - and a year ago he told me how his team of post-docs get together every Friday for about six hours of coding and pizza. They use a big screen TV, one person on the keyboard for the whole session, and as many as ten people contributing to what's getting typed. At first, it was a way for everyone to learn Scala, and also to make sure that the project they were writing wasn't locked up inside one person's head.

A month or so later, I was hanging out with Pat Maddox ([@patmaddox](https://twitter.com/patmaddox)), telling him about my plans for pair programming in the Women's Internship Program I was creating at work. Pat suggested I look at mob programming instead, and I remembered I had looked at mob programming and I loved the idea.

## What is mob programming?

Pat Maddox didn't just think Mob Programming sounded cool, he'd gone to do it with Woody Zuill ([woodytwitter](https://twitter.com/WoodyZuill)) and the team of developers at Hunter Industries who worked out the techniques. Pat had a lot of good things to say about the experience, and his excitement was contagious.

You can read about Woody Zuill's experience with Mob Programming[^experiencereport] directly, but the short and mostly inaccurate version goes something like this. The team of developers (I heard there were eight) were discussing a project that had been shelved a few months, and kinda fell into a code review. That turned into a little bit of programming, and because it went well, they did it all afternoon. Then the next day too, even though they were competing for conference room space. Finally after a few weeks of programming together, Woody made a mob programming space with a couple of projectors and a single computer and keyboard, and the team made it official. This was how they wanted to work. Along the way, they mastered interpersonal communication, destroyed ego, and learned to write some of the cleanest, most correct code ever committed to a repository. You think I'm kidding. I'm not.

Woody Zuill's team is both the prototype and the archetype for what we've done, but I'm a programmer as well as a manager and embody Larry Wall's three virtues: laziness, impatience, and hubris. So I scanned the literature, talked to a few people, gave a nod or two to Woody on Twitter, and went off to forge our own path.

[^experiencereport]: Woody Zuill wrote a [report about their mob programming experience](http://www.agilealliance.org/files/6214/0509/9357/ExperienceReport.2014.Zuill.pdf).

## How we do it

Over the last year, I've done mob programming with dozens of teams, all skill levels, in at least a half dozen programming languages, on two continents. I can't say that there's one way we do it.

My team at $dayjob has a mob programming area. We have a 50-something-inch television with an AppleTV and an HDMI cable surrounded by comfy chairs and a couch. It's tucked into our work area, so our desks surround it too. We keep a whiteboard and bar-height table nearby too. My team has used the space to mob as many as six hours a day, often attracting more people from other teams than we bring ourselves. We learned dom.js in a mob, taught each other monads in a mob, created a new product in a mob, and started doing property-based testing in a mob. My team is small right now, only five of us, and we work on multiple projects so our most of our mobbing is two hours or more per week on each project, giving everyone a chance to contribute to each of our projects. 

Mobbing has caught on in our department, too. My team is one of three with their own mobbing zone, plus we've converted two conference rooms to mobbing-friendly workspaces. We have weekly testing workshops that use mob programming to help individual developers solve difficult testing questions. We use mob programming to learn new languages, frameworks, and libraries.

Our CTO and VP-engineering have huge supporters of giving to the community, and I've had their support in creating an internship program within our department. It's full-time, paid, specifically for women who are returning to the workforce or retraining. It's designed to take a boot camp graduate to a solid junior level developer in 16 weeks or so. We have four interns at a time, working with at least two seniors, generally on a greenfield project (although we're working more refactoring into their internships), in a mob five hours a day five days a week. The internship mob often includes domain experts and developers from other teams sharing their experience.

Outside of $dayjob, I have a special interest in learning to build teams of functional programmers that productively includes junior developers. Part of my study has been to create a workshop series called "An Ounce of Elixir", teaching functional programming (using Elixir) mostly to new developers. Every workshop is interactive and hands-on, and includes about 6 hours of mob programming. In each workshop, the students solve the same exercise: creating an event-sourced, CQRS shopping cart in a purely functional way. In each case so far, we've managed to get venues with conference rooms that have large-screen TVs and room for eight or nine people to work.

We've done ad-hoc mobs, short-term mobs, and long-term mobs, but we haven't done anything with the level of commitment (let alone longevity!) that Woody Zuill's team has. We don't have the buy-in for that kind of commitment. Sure, on my small teams we can give it a go, but in the larger department, there are varied opinions about the potential for mob programming.

All the same, I'm confident our experience is useful, so don't stop reading yet.

## Our mob programming guidelines, and where they came from

Here are our current mobbing guidelines. We print these off and keep them in our mobbing area.

0. Kindness, consideration, and respect are way better than having anyone in charge.
0. “Yes and” goes further than “no” and “but”.
0. Learning is contributing.

0. We speak at the highest level of abstraction the mob is able to digest in the moment.
0. Declarative language and experience sharing goes further than imperative language.
0. Thinking out loud helps everyone in the mob follow what you’re doing.

0. Drivers type code that the mob proposes.
0. We learn differently when we’re the driver, so it’s important that everyone drives.
0. Rotations can happen as often as every five minutes.

0. Turn up the good.

Let's look at where they came from, and what they do for us.

### How we relate to each other

The first three guidelines are very much about how we see each other, and I'll jump right off a cliff and call it anarchy. Specifically, mutualism, a labor theory of anarchy, but all the same when we mob we are trying to create a non-coercive, egalitarian environment.

> Kindness, consideration, and respect are better than having anyone in charge.

Is it surprising that we might draw on anarchy to inform how we work? I've been fascinated by the way anarchy was informing software engineering management for years. We have flat organizational charts, everyone reporting to the CTO or CEO. We have engineering-driven organizations, where engineers choose what they'll work on. We have different rules (i.e. none) for engineers' dress code and work spaces. We have game spaces, nap spaces, and a do-whatever-you-want attitude. We have flex-time, unlimited PTO, even unlimited maternity and paternity leave at some places. If we put the team on a farm in Tennessee, we'd have no problem seeing this as anarchy.

> “Yes and” goes further than “no” and “but”.

This guideline comes straight from improv comedy training. Yes, my teams do improv training.

Improv is hard work. Improv teams build on each other, taking a wacky concept from one or two people and building it into a story that delights. It's very much the same with mob programming. When someone says "No", especially if they are an authority figure outside of the mob, progress stops. We have to overcome inertia and find a different way to make progress. "Yes, and ..." preserves momentum - it takes the position we're in and contributes not only a new milestone but also how to get there.

> Learning is contributing.

Almost every mob I've worked with has had juniors, in large part because I think juniors are tremendously valuable to any team. And almost every mob I've worked with has had juniors sit idle, refusing to participate, because they don't want to slow down the people who really know what they're doing.

It's possible that this guideline, "Learning is contributing", is the most important in the list.

* Stopping for an explanation forces someone who thinks they know what they're doing to explain it. Often just explaining it will expose any problems.
* If one person doesn't know what's going on, chances are good other people don't know what's going on. **I often don't know what's going on.**
* Mobs are great for training. Juniors aren't just learning the language, they're learning to deliver value. Mobs teach good judgement.



Talk about git checkins

## Everything we ever did wrong

From retrospectives

## Everything we ever did right

From retrospectives

## Are mobs productive?

10x devs and mobbing

## Mobbing for the win

Reasons I think mobbing is successful
