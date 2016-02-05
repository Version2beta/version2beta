---
pagetitle: The 10x developer
longtitle: 
tags: cto
author: Rob Martin
published: 2016-02-4 17:00
snippet: This is an offshoot from my work building teams of functional programmers, and the trend toward anarchy in software engineering teams. In this short post, I discuss why 10x developers exist, how they do so much more than average, and some ideas for driving value up across the whole team.
---

I've been seeing a trend claiming that 10x developers don't actually exist, and I can understand the motivation to make such claims. Surely, even the people making the claims aren't saying they can't find two developers who have an order of magnitude worth of skill levels between them. Instead I think they're saying our industry is changing, that value doesn't come from isolation and raw processing power of the programmer. We work together now. We pair, we mob, we pull in our domain experts and develop a ubiquitous language before we even consider code.

I agree with all of that, and I think that 10x developers not only exist, they aren't actually all that rare. Also, they aren't stereotyped loners. Also, we want them in our pairs and on our mobs and working with our domain experts.

**10x developers don't deliver 10 times as much code, they deliver 10 times as much value.** They do this by making consistently better than average choices throughout the project, and these choices stack on top of each other for a compounding increase in value.

Here are some examples:

* Imagine that an average dev makes ten average decisions each of which return an average value. This is our baseline. The average developer delivers 100% of average value.

* A 10x developer makes ten above-average decisions, each of which delivers 25% more value in comparison to the average decision. This is compounded - 1.25<sup>10</sup> - and the 10x developer ships 931% of average value.

* On the opposite end of the spectrum, imagine a below average developer who makes ten below average decisions, each of which drive value down 25%. This is also compounded, so this developer ships a whopping 5.6% of average value. While not the title character of this blog post, we could call this developer an <sup>x</sup>/<sub>10</sub> developer.

As you can see, a 10x developer working on a project where there are, say, 10 major decisions to make can affect the overall value of the project by an order of magnitude, when compared to an average developer. Likewise, an <sup>x</sup>/<sub>10</sub> developer delivers value an order of magnitude lower than the average developer.

Here are ten ways the decision, choices, and habits of exceptional developers can have a compound impact on the value they ship.

## 10 practices of 10x developers

1. 10x developers write less code, so they do less work.

10x developers do it better the first time. They don't flail around. They make good choices. They know their tools. They know their patterns.

2. 10x developers can reason about their code. We can reason about their code too.

10x developers don't write clever code; they write readable code. They know that troubleshooting code is harder than writing it, so they don't pack their ego into their code.

3. 10x developers use the right abstractions (both programming language *and* design patterns).

10x developers use the right programming languages for the problem at hand. They know design and architectural patterns, so they know the established best ways to solve many problems.

4. 10x developers write code that is unencumbered by unneeded dependencies.

10x developers don't start with a large code base of platforms and libraries because of rapid application development. They write core business logic in the core language, and use libraries for interfacing with the user and the persistence layer.

5. 10x developers write code scales seamlessly in production.

10x developers make programs that are stateless, functional, referentially transparent, and independent. Their code don't just scale, it approaches linearity.

6. 10x developers write code that does only what's specified, and is free from defects.

10x developers admire efficiency and elegance. Their code uses fewer abstractions more completely, does exactly what it's specified to do, and doesn't confound its purpose with undocumented behavior.

7. 10x developers don't ship technical debt.

10x developers like to ship value early and often, but not before it's correct. They don't ship prototypes, and they don't want to support prototypes.

8. 10x developers can extend their code without starting from scratch.

10x developers see architecture and design, strategy and tactics. This is when they rewrite: (1) Before the code hits production, if they didn't get it right the first time. (2) When the business pivots.

9. 10x developers can demonstrate correctness, and sometimes even **prove** their code is correct.

10x developers write tests that mean something. They would prefer to write code that can be mathematically proven to always produce a correct result. They take joy in functional programming, because math.

10. 10x developers write code that is secure.

Because their programs don't rely on bloated libraries, aren't tightly coupled, don't carry technical debt, are stateless, and do only what they're specified to do, 10x developers write code that is more secure than other developers write.

## Some observations

Items 1 through 5 above share a theme of simplicity. Items 6 through 10 share a theme of correctness. **10x developers, and the rest of us, deliver our best value by shipping code that is simple and correct.**

8 out of 10 of the characteristics of a 10x developer (items 2, 4, 5, 6, 7, 8, 9, and 10) directly address the ongoing cost of the software. Maintenance of our code base, from fixing defects and plugging security holes to adding features, is the long tail when it comes to paying for our code. 10x developers shouldn't get their reputation based on writing a lot of code fast, but **by delivering long term value efficiently.**

Most developers are lucky if they *ever* ship a feature than changes a user's life. The ones who do often do because of the law of averages. They ship more code, so they're more likely to ship something meaningful. I'm talking about 10x developers. I've heard they don't exist, but I think they do.

Finally, all 10 characteristics above **can be the result of leadership and training.** In fact we can foster all of these characteristics by having our 10x developers work directly with the rest of our team. If we put a 10x developer in a mob, the 10x developer will go slower, but the mob will produce better much value than average, and the individuals will go on to continue producing better value.
