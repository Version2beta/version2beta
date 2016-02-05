---
pagetitle: Anarchy and Genius
longtitle: 
tags: cto
author: Rob Martin
published: 2016-02-4 17:00
snippet: This is an offshoot from my work building teams of functional programmers, and the trend toward anarchy in software engineering teams. In this short post, I discuss why 10x developers exist, how they do so much more than average, and some ideas for driving value up across the whole team.
---

> Anarchy may not be the best form of government, but it's better than no government at all. - Unknown

Before you fall into a knee-jerk reaction to the term **anarchy**, let me throw a few ideas at you and see if any of them sound familiar at work. Yes, at work.

* Self-governed
* Non-coercive
* Stateless
* Non-hierarchical
* Anti-authoritarian
* Mutualism
* Participatory

These terms are all associated with various forms of classical anarchy (as opposed to the rocks-through-Starbucks kind of anarchy, as well as others.) Maybe you can see how these come into play on our software engineering teams, but maybe you don't, so let's look at another list. This one is more like recruiting propoganda.

* Engineering-driven organizations: You own your work!
* Flat organizational charts: Everyone is their own boss!
* Choice of assignments and teams: Do what you love!
* No dress code: Be yourself!
* Flexible, well apportioned workspace: Leave your $1000 treadmill desk and work outside!
* Life balance at work: Games, drinks, entertainment, naps!
* Flex-time: We care about you, and the code you ship!
* Unlimited personal time off: We care about you, and the code you ship!
* Unlimited maternity / paternity leave (Really! I just saw this at [Degreed.com](https://degreed.com).) We really, really care about you, and the code you ship!

The anarchy lens breaks down when we look at the money they pay us, though. That's when it starts to look more like royalty.

Why do we do this? We build our developers communal play spaces that would make a Russian philosopher cry, and we pack them dozens to a city block.

We do this to attract, and foster, genius.

Outside of a brand spanking new startup, most developers are lucky if they make ship one feature a year that changes a user's life. Scratch that. Most developers are lucky if they **every** ship a feature than changes a user's life. The ones who do often do because of the law of averages. They ship more code, so they're more likely to ship something meaningful.

I'm talking about 10x developers. I've heard they don't exist, but I think they do. In fact, I think there are lots of 10x developers, because we have so many bad developers out there, 10x is not a very high bar.

A 10x developer only needs to make slightly better than average choices, because our choices stack on one another and the result - value - is compounding.

Imagine that an average dev makes ten average decisions each of which return an average value. This is our baseline. The average developer delivers 100% of average value.

A 10x developer makes ten above-average decisions, each of which drives value up by 25%. This is compounded - 125% ^ 10 - and the 10x developer ships 931% of average value.

On the opposite end of the spectrum, imagine a below average developer who makes ten below average decisions, each of which drive value down 25%. This is also compounded, so this developer ships a whopping 5.6% of average value.

As you can see, a 10x developer working on a project where there are, say, 10 major decisions to make can affect the overall value of the project by an order of magnitude. Here are ten ways we can do that.

## 10 practices for 10x developers

1. We write less code, so we do less work.

We do it better the first time. We don't flail around. We make good choices. We know our tools. We know our patterns.

2. We can reason about our code. You can reason about our code too.

We don't write clever code; we write readable code. We know that troubleshooting code is harder than writing it, so we don't pack our ego into our code.

3. We used the right abstractions (both programming language *and* design patterns).

We use the right programming languages, and by right I mean we use functional programming languages and principles. We know our design and architectural patterns, so we know the established best ways to solve many problems.

4. Our code is unencumbered by unneeded dependencies.

We don't start with a large code base of platforms and libraries because of rapid application development. We write core business logic in our core language, and use libraries for interfacing with the user and the persistence layer.

5. Our code scales seamlessly in production.

We make programs that are stateless, functional, referentially transparent, and independent. We don't just scale, we approach linear.

6. Our code is free from defects. We don't ship technical debt.

We like to ship value early and often, but not until it's actually correct. We don't ship prototypes, and we don't want to support prototypes in the hands of our users.

7. Our code does only what's specified.

Our programs are efficient and elegant. Bugs and security flaws come from code that does more than what's specified.

8. We can extend our code without starting from scratch.

We see architecture and design, strategy and tactics. You know when we rewrite? (1) Before the code ships, if we didn't get it right the first time. (2) And when the business pivots.

9. We can demonstrate correctness, and sometimes even prove our code.

We write good tests that mean something. Often we even write code that can be mathematically proven to always produce a correct result. This is one joy of functional programming. Because math.

10. Our code is secure.

Because our programs don't rely on bloated libraries, aren't tightly coupled, don't carry technical debt, are stateless, and do only what they're specified to do, they are more secure than the vast majority of code in the world.

## Simple and correct

I want to point out a theme. Items 1 through 5 above are about simplicity. Items 6 through 10 are about correctness. A 10x developer will write code that is simple and correct, and I believe this is key.

