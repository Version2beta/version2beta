---
title: "10x developers deliver more value."
date: "2016-02-05"
description: This is an offshoot from my work building teams of functional programmers, and the trend toward anarchy in software engineering teams. In this short post, I discuss why 10x developers exist, how they do so much more than average, and some ideas for driving value up across the whole team.
categories:
  - cto
  - dev
---

Do 10x developers exist?

I'm seeing more conference talks and blog posts saying they don't. Surely, the people making these claims aren't saying they can't find two developers who have an order of magnitude worth of skills level difference between them. Instead I think they're saying our industry is changing, that value doesn't come from isolation and the raw code processing power of the programmer. We work together now. We pair, we mob, we pull in our domain experts and develop a ubiquitous language before we even consider how to start coding.

I agree with all of that. Also, I think that 10x developers not only exist, they aren't actually all that rare. And they aren't stereotyped loners. And we want them in our pairs and on our mobs and working with our domain experts.

**10x developers deliver 10 times as much value, not 10 times as much code.** They do this by making consistently better than average choices throughout the project, and these choices stack on top of each other for a compounding increase in value.

Here are some examples:

> Imagine that an average developer makes ten average decisions each of which return an average value. This is our baseline. The average developer delivers 100% of average value.

> A 10x developer makes ten above-average decisions, each of which delivers 25% more value than the average decision. This is compounded - 1.25<sup>10</sup> - and the 10x developer ships 931% of average value.

> On the other end, imagine a below average developer who makes ten below average decisions, each of which drive value down 25%. This is also compounded, so this developer ships a whopping 5.6% of average value. While not the title character of this blog post, we could call this developer an <sup>x</sup>/<sub>10</sub> developer.

As you can see, a 10x developer working on a project where there are 10 major decisions to make can affect the overall value of the project by an order of magnitude, when compared to an average developer. Likewise, an <sup>x</sup>/<sub>10</sub> developer delivers value an order of magnitude lower than the average developer. (If you're keeping score at home, that's two orders of magnitude.)

Here are ten decisions, choices, and habits of exceptional developers that compound value on the projects they ship.

## 10 practices of 10x developers

1. 10x developers write less code, so they do less work.

10x developers do it better the first time. They don't flail around. They make good choices. They know their tools. They know their patterns.

2. 10x developers can reason about their code. We can reason about their code too.

10x developers don't write clever code; they write readable code. They know that troubleshooting code is harder than writing it, so they don't pack their ego into their code.

3. 10x developers use the right abstractions (both programming languages _and_ design patterns).

10x developers use the right programming languages for the problem at hand. They know design and architectural patterns, so they know the established best ways to solve many problems.

4. 10x developers write code that is not encumbered by unnecessary dependencies.

10x developers don't start with a large code base of platforms and libraries because "rapid application development". They write core business logic in the core language, and use libraries for interfacing with the user and the persistence layer.

5. 10x developers write code that scales seamlessly in production.

10x developers make programs that are stateless, functional, referentially transparent, and independent. Their code don't just scale, it approaches linearity.

6. 10x developers write code that is free from defects and does only what's specified.

10x developers admire efficiency and elegance. Their code uses fewer abstractions more completely, does exactly what it's specified to do, and doesn't confound its purpose with undocumented behavior.

7. 10x developers don't ship technical debt.

10x developers like to ship value early and often, but not before it's correct. They don't ship prototypes, and they don't want to support prototypes.

8. 10x developers can extend their code without starting from scratch.

10x developers see architecture and design, strategy and tactics. They rewrite before the code hits production, if they didn't get it right the first time.

9. 10x developers can demonstrate correctness, and like to prove their code is correct.

10x developers write tests that mean something. They would prefer to write code that can be mathematically proven to always produce a correct result. They take joy in functional programming, because math.

10. 10x developers write code that is secure.

Because their programs don't rely on bloated libraries, aren't tightly coupled, don't carry technical debt, are stateless, and do only what they're specified to do, 10x developers write code that is more secure than other developers write.

## Some observations

Items 1 through 5 above share a theme of simplicity. Items 6 through 10 share a theme of correctness. 10x developers, and the rest of us, **deliver value by shipping code that is simple and correct.**

8 out of the 10 characteristics (items 2, 4, 5, 6, 7, 8, 9, and 10) address the ongoing cost of software. Maintenance of our code base is the long tail when it comes to paying for our code. 10x developers shouldn't get their reputation based on writing a lot of code fast, but **by delivering long term value through extremely low maintenance costs.**

Finally, all 10 characteristics above can be **the result of leadership and training.** In fact we can foster all of these characteristics by having our 10x developers work directly with the rest of our team. If we put a 10x developer in a mob, the 10x developer may go slower, but the mob will produce much better value than average, and the individuals will go on to continue producing better value.

Most developers are lucky if they _ever_ ship a feature than changes a user's life. Most managers are lucky to work on a product that changes users' lives. Maybe the best we can do is embrace a coding ethic that makes our work meaningful, and **maybe bringing that ethic raises our work to a standard capable of changing lives.**
