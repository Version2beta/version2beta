---
pagetitle: A year of mob programming
longtitle: The first year of my experiment with mob programming
tags: cto
author: Rob Martin
published: 2016-02-10 15:30
snippet: It's been twelve months since I started learning how to program in a mob. This post describes my experiences.
---

A friend of mine works in a computer research lab, and a year ago he told me how his team of post-docs get together every Friday for about six hours of coding and pizza. They use a projector, one person on the keyboard for the whole session, and something like ten people contributing to what's getting typed. At first, it was a way for everyone to learn Scala, and also to make sure that the project they were writing wasn't locked up inside one person's head.

A month or so later, I was hanging out with Pat Maddox[^patmaddox], telling him about my plans for pair programming in a women's internship program I was creating at work. Pat suggested I look at mob programming instead, and I remembered I had looked at mob programming and I loved the idea.

## What is mob programming?

Pat Maddox didn't just think Mob Programming sounded cool, he'd gone to do it with Woody Zuill[^woodyzuill] and his team of developers at Hunter Industries who worked out the techniques. Pat had a lot of good things to say about the experience, and his excitement was contagious.

You can read about Woody Zuill's experience with Mob Programming[^experiencereport] directly, but the short and mostly inaccurate version goes something like this. The team of developers (I heard there were eight) were discussing a project that had been shelved a few months. They kinda fell into a code review trying to remember where things were at, and that turned into a little bit of programming, and because it went well, they did it all afternoon. Then they worked together the next day too, even though they were competing for conference room space. Finally after a few weeks of programming together, Woody made a mob programming space with a couple of projectors and a single computer and keyboard, and the team made it official. This was how they wanted to work. Along the way, they mastered interpersonal communication, destroyed ego, and learned to write some of the cleanest, most correct code ever committed to a repository. You think I'm kidding. I'm not.

Woody Zuill's team is both the prototype and the archetype for what we've done, but I'm a programmer in the vein of Larry Wall's three virtues: laziness, impatience, and hubris. So I scanned the literature, talked to a few people, gave a nod or two to Woody on Twitter, and went off to forge our own path.

[^patmaddox]: Pat is the creator of [Ruby Steps](https://www.rubysteps.com/). Read [Pat's bio here](https://www.rubysteps.com/about-pat/) and follow [@patmaddox on Twitter](https://twitter.com/patmaddox). Or better yet, grab a meal with Pat and talk about life. I recommend it.
[^woodyzuill]: Woody Zuill is often credited with creating mob programming, or coining the phrase, or supporting his team while they worked out the details, or something like that. I'm pretty sure he's the creator of [mobprogramming.com](http://mobprogramming.com/). He teaches mob programming all around the world, and I often see announcements for new workshops on his [@woodyzuill Twitter account](https://twitter.com/WoodyZuill).
[^experiencereport]: Woody Zuill wrote a [report about their mob programming experience](http://www.agilealliance.org/files/6214/0509/9357/ExperienceReport.2014.Zuill.pdf) at Hunter Industries.

## How we do it

Over the last year, I've done mob programming with dozens of teams, all skill levels, in more than a half dozen programming languages, on two continents. I can't say that there's one way we do it.

My team at $dayjob has a mob programming area. We have a 50-something-inch television with an AppleTV and an HDMI cable surrounded by comfy chairs and a couch. It's tucked into our work area, so our desks surround it too. We keep a whiteboard and bar-height table nearby too. My team has used the space to mob as many as seven hours a day, often attracting more people from other teams than we bring ourselves. We learned dom.js in a mob, taught each other monads in a mob, created a new product in a mob, and started doing property-based testing in a mob. Right now, my team is small - only five of us - and we're working on multiple projects. We are mobbing about two hours per week on each project. It's not much, but it keeps us all up to date on each of the projects we're responsible for.

Mobbing has caught on in our department. My team is one of three with their own mobbing zone, plus we've converted two conference rooms to mobbing-friendly workspaces. We have weekly testing workshops that use mob programming to help individual developers solve difficult testing questions. We use mob programming to learn new languages, frameworks, and libraries. We mob when new people join our teams, to bring them up to speed quickly. We share our experience with other teams in programming mobs, and invite people with skills we're still learning to our mobs.

Our CTO and VP-engineering strongly support the local tech community. With their support we created a full-time, paid, internship program specifically for women who are retraining and/or returning to the workforce. One of our goals is to take a boot camp graduate to a solid junior level developer in 16 weeks. We have four interns at a time, working with at least two more experienced developers, generally on a greenfield project, in a mob, five hours a day, five days a week. The interns' mob often includes domain experts and developers from other teams sharing their experience.

My primary direction for professional development right now is learning to build teams of functional programmers that productively includes junior developers. Part of my study has been to create a workshop series called "An Ounce of Elixir", teaching functional programming (using Elixir) mostly to new developers. Every workshop is interactive and hands-on, and includes about 6 hours of mob programming. In each workshop, the students solve the same exercise: creating an event-sourced, CQRS shopping cart in a purely functional way. In each case so far, the workshop participants, programming in a mob, have succeeded in creating a purely functional shopping cart.

I've done ad-hoc mobs, short-term mobs, and long-term mobs, but I haven't done anything with the level of commitment and longevity that Woody Zuill's team has. They have done mob programming day in and out for years, and in spite of my hubris, there's so much to learn from them. At the same time, I'm confident our experience is useful, so don't stop reading yet.

## Our mob programming guidelines, and where they came from

Our mobbing experience started with three months of thinking, discussing, and experimenting. That resulted in handful of guidelines for mob programming. With that, we started mobbing with regularity. Over time, we updated our mob programming guidelines. They're printed off and kept in our mobbing area.

These are our current guidelines:

0. Kindness, consideration, and respect are way better than having anyone in charge.
0. “Yes and” goes further than “no but”.

0. We speak at the lowest level of abstraction anyone in the mob needs in the moment.
0. Declarative language and experience sharing goes further than imperative language.
0. Thinking out loud helps everyone in the mob follow what you’re doing.

0. Drivers type code the mob proposes.
0. We learn differently when we’re the driver, so it’s important that everyone drives.
0. Rotations can happen as often as every five minutes.

0. Learning is contributing.

0. Turn up the good.

Let's look at where they came from, and what they do for us.

### How we relate to each other

The first two guidelines are very much about how we see each other, and **I'll jump right off a cliff and call it anarchy**. Specifically, mutualism, a labor theory of anarchy, but all the same when we mob we are trying to create a non-coercive, egalitarian environment.

> Kindness, consideration, and respect are better than having anyone in charge.

I've been fascinated by the way anarchy has been informing software engineering management for years. We have flat organizational charts, everyone reporting to the CTO or CEO. We have engineering-driven organizations, where engineers choose what they'll work on. We have different rules (i.e. none) for engineers' dress code and work spaces. We have game spaces, nap spaces, and a do-whatever-you-want attitude. We have flex-time, unlimited PTO, even unlimited maternity and paternity leave at some places. If we put the team on a farm in Tennessee, we'd have no problem seeing this as anarchy.

Interestingly, our mobbing anarchy also build empathy. When we work together this closely, we have to see each other, like really see where we're at and how we're doing. We can't show kindness and respect without caring. Our teams that mob know each other better, listen better, and communicate better than they did before we started mobbing.

> “Yes and” goes further than “no but”.

This guideline comes straight from improv comedy training, which is something my teams do - improv comedy training.

Improv is hard work. Improv teams build on each other, take a wacky concept from one or two people and build it into a story that delights their audience and themselves. It's very much the same with mob programming. When someone says "No", especially if they are an authority figure outside of the mob, progress stops. We have to overcome inertia and find a different way to make progress. "Yes, and ..." preserves momentum - it takes the position we're in and contributes not only a new milestone but also how to get there.

### How we communicate with each other

These three guidelines help us communicate well.

> We speak at the lowest level of abstraction anyone in the mob needs in the moment.

When the interns mob, they often talk about things like which keys to press in Vim, how to structure a Git command, and how to call a particular function.

When our seniors mob, they often talk about things like control flow, patterns, testing strategies, and architecture. Except when there are interns or juniors working too; then, they **also** talk about Vim key combinations, git commands, and syntax. This is because everyone in the mob needs to have the choice to understand what's going on, to ask questions and get answers they are capable of understanding based on their level of experience.

> Declarative language and experience sharing goes further than imperative language.

I've had the opportunity to learn a little bit about child development, specifically how we adults and parents interact with children. One interesting fact is that more than 80% of our verbal communication with children is imperative: "Do this", "don't do that". Yet when we communicate with other adults, almost 80% of our verbal communication is declarative, experience sharing. "I wonder about that", "this thing happened to me".

Can you imagine what our lives would be like if we went around talking to other adults like we do to children? You probably can. I know people like that. And weirdly, when we get in a mob, our imperative communication can quickly escalate. It's almost as if having other people between us and our keyboard turns us into control freaks. "Don't do it that way. Try this. No, type it like I say."

In our mobs we try very hard to not communicate imperatively. Instead, we try to make declarations about our shared experience. "That function looks funny." "I wonder if that test catches all our edge cases." "I don't know how this library works." "There is a typo in line 47." "I just learned something new."

> Thinking out loud helps everyone in the mob follow what you’re doing.

Thinking out loud takes our experience sharing and levels it up.

Sharing leads to understanding - we can't understand what we know nothing about. Understanding leads to learning, not just skills but learning about and from other people. Learning leads to empathy. In fact, I think it's very difficult for us to learn with or from other people without feeling more empathetic. Empathy leads to caring, and caring - about other people, about our customers and users, about our work, about ourselves - leads to fulfillment.

Yes, I got all touchy-feely, but this is what happens in a mob. We talk a lot. We think out loud. People understand what we're doing and why. We get involved. We share and listen. We trust each other. We care.

A quiet mob is a red flag. Thinking out loud has amazing benefits, and its entirely reasonable to encourage constant conversation. This is different from our typical software engineering experience, and it takes practice, but the results are invaluable and at least a little bit beautiful.

### Roles

While we've had mobs that choose to define roles, we really only have two roles in our guidelines: the driver - that is, the person on the keyboard - and the mob.

> Drivers type code the mob proposes.

Many mobbers have a hard time thinking and talking at the same time. Ask us to think, talk, and type and we fall into a well-established work habit. We stop talking. We go heads down and code, by ourselves. This is definitely not what we want to do in a mob.

In our mobs, we discourage the driver from writing any code. The driver's job is to be the hands and fingers of the mob. This keeps the driver from going solo and leaving the rest of the mob behind while he or she is controlling the keyboard. It keeps the driver engaged with the mob, interacting. It makes the mob into one body, connected and working together.

> We learn differently when we’re the driver, so it’s important that everyone drives.

Perhaps the most important reason the driver just drives is that many of us learn with our fingers as much as our heads.

I can remember most of the phone numbers that were important to me as a child. My home phone number during elementary school. My home phone number during junior high. My grandparent's phone number. But, in order to recite the number, I usually have dial it on an imaginary phone.

Many of us learn kinetically. We store data in our fingertips. We store syntax in our muscle memory. Our mobs help honor these other ways we learn things, and by switching drivers frequently, we reinforce what we're learning in the mob, learning faster, and improving our retention, because we're learning it in different ways in quick procession.[^twiceasfast]

> Rotations can happen as often as every five minutes.

We did mobs where we had one driver for hours on end. We did mobs where we barely bothered to sit down, we changed drivers so often. Interestingly, stability of roles in the mob was not necessarily a good thing.

Changing drivers frequently seems to keep everyone engaged - perhaps by keeping them invested in what comes next, since we will be driving the keyboard shortly.

In practice, 20 to 30 minutes seemed to be the ideal rotation for most mobbing sessions. There were mobs where we felt confident we didn't want to change drivers, and afterward decided we were wrong. There were mobs where we changed drivers more frequently and felt moderately successful.

[^twiceasfast]: If you're the kind of person who likes claims like this to include citations, check out this [study from Johns Hopkins University School of Medicine](http://www.hopkinsmedicine.org/news/media/releases/want_to_learn_a_new_skill_faster_change_up_your_practice_sessions).

### Creating developers, teams, and code

> Learning is contributing.

Almost every mob I've worked with has had juniors, in large part because I think juniors are tremendously valuable to any team. And almost every mob I've worked with has had juniors sit idle, refusing to participate, because they don't want to slow down the people who really know what they're doing.

It's possible that "Learning is contributing" is the most important guideline in the list. It doesn't just help the person learning while slowing every one else down. It sets a pace for the mob that best addresses all of our goals.

* Stopping for an explanation forces someone who thinks they know what they're doing to explain it. Often **just explaining it will expose many problems.**
* If one person doesn't know what's going on, chances are good other people don't know what's going on. I am usually the most senior developer in our mobs, an **I often don't know what's going on.**
* Mobs are great for training. Juniors aren't just learning the language, they're learning to deliver value. Mobs are an excellent place for seniors to **teach juniors how to deliver better value.**
* **Mobs train seniors too.** Seniors learn to communicate and collaborate better in a mob.

### Retrospectives

> Turn up the good.

Some of our guidelines came directly from Woody Zuill's experience report, and we've stuck with them from the start. This is definitely one. I love it and I want to use it everywhere in my life.

**If something is good, do more of it.**

Over the last year, we did retrospectives after almost every mob. When we first started experimenting with mob programming, we used these four questions:

* What went well?
* What went poorly?
* What would you like to try differently?
* What still has you puzzled?

In my functional programming workshops, we use these questions:

* How do you feel about your code?
* How do you feel about your team / mob?
* How do you feel about yourself?

Our interns started with these questions:

* What should we do more of?
* What should we do differently?
* What baffled you?

Over time, they got bored with those questions and chose these instead:

* What did you like that happened in the mob?
* What did you learn today?
* What did we accomplish today?
* Do you understand?
* What didn't go well?
* What should be done differently next time?

After trying the new questions a while, they made one more change to their retrospective prompts, and ended with these questions:

* What should we keep doing?
* What should we stop doing?
* What should we start doing?
* What surprised us?

Personally, I like the touchy-feely questions because they get to all of the reasons we mob, on a qualitative and analytic level. How do you feel about your code, your team, and yourself?

The interns got very pragmatic when they rewrote their retrospective questions. I like that too, especially "Do you understand?" It's very direct, and it got better conversation than "What baffled you?"

The questions are just prompts, though. We talked about mobbing every day we did it, and that was important. Learning to mob was a mob activity.

Up till this point, we've talked about how we mobbed. From here on, we talk mostly about how it went, and that information comes primary from our retrospectives.

## Everything we did wrong

### Team retrospectives

> "I started off with something I got stuck on. It didn't start smoothly. If we didn't get stuck on this we could have finished something else."

> "In the past I've felt like I had to justify dogpiling on a problem."

Of all the times we mobbed, I can count on one hand the number of times someone outside of the mob tried to compare the productivity of a mob to the productivity of the individual members working on their own. And yet, inside the mob, this was an almost constant concern. We were afraid of other people judging us for ganging up on our work. We were afraid of slowing each other down. We felt guilty when we got stuck, and were "wasting" the time of everyone in the mob.

> "I was feeling bad that I got stuck on this and asked other people to help."

We also felt guilty for what we don't know, for not being better programmers, for not having more skills, for needing to learn. One of our biggest challenges was getting people to participate when they didn't know what was going on, because participating meant disrupting the flow of the mob. When we let that happen - when we let the mob continue, even though some portion of the mobbers were lost - what we saw in the retrospectives was that no one felt like it was a good session. The code was poor quality. The practice was useless. The learning was shallow. The energy was lethargic. Code, team, and self all suffered.

> "We got stuck on these little things. If we hadn't we could have been cruising along."

This is why we implemented the "Learning is contributing" guideline, and ultimately it's why I think that it is the most important guideline. Regardless of what metrics we use to gauge the benefits of mobbing, learning will come into it. We can't budge the needle on any metric unless the mob is a learning experience.

---

> "Because this was a hack day, I feel like we needed to get more done. If we'd had more time, I would have stopped more to check if everyone know what was going on."

> "I think that went well, we did get a lot done. We got a good amount accomplished, we just didn't do a lot of learning and training so that next time we meet everyone could participate better."

> "I was going to drive for a while, but I didn't speak up. I feel like I learn more from driving more."

> "It was a lot of learning for me because I don't know much about functional programming."<br />"Did you feel excluded from the mob because you didn't know what was going on?"<br />"Somewhat."

> "Especially for those who don't know the language well, it's easier for them to feel excluded and shut down and even hurt or upset because they don't feel competent already, like 'I don't know the language and now I can't contribute in other ways either.' I think in future mobs we need to encourage them more, to make their competence level go up, and explain why we think this or that idea may not work."

That learning experience is in no way limited to the more junior members, either. I'm the most senior developer on my team, and I learn from my team every day. I often want to hide that fact, but that's hard to do in a mob. We learn from each other constantly, and we learn from each other most efficiently when we do it out in the open.

---

> "We did really high level, difficult Javascript today, stuff I wasn't prepared to understand. There were a lot of times today I was scrambling to keep up, but the team kept moving because the people who were contributing most were able to keep up at the higher level."

> "It wasn't the implementation that caused conflict, it was the high level talk."

> "I felt there was a lot of pressure on me. I was the only language expert, and the only one who knew the code."

> "If we do go the approach of 'just say no, just shut them down' instead of more comforting things, it might be good to rotate people afterwards to help people feel better."

It seems counter-intuitive to suggest that a bunch of highly-skilled developers need to learn how to talk about code, but when we're trying to do it for a half dozen hours straight, for days on end, we really benefitted from practice and reflection. Learning how to discuss code at this level was a new skill for our seniors, and for me. Learning how to do this with interns and juniors was a new skill for everyone.

This is just code. This isn't about empathizing, sharing feelings, being vulnerable.

---

> "I wasn't happy with the choice to use Node, but I feel like it was a circumstance of the mob. It was a hack day. Not everyone knew the languages I wanted to use. It would have been better to use Scala, or Haskell, or Erlang, but there was the issue of bringing people up to speed and that conflicts with needing to get something done."<br />"I was unhappy we didn't use Java 8. And I got a preemptive shut down before I even brought it up."<br />"Can we vote then?"<br />"I'm not the only person who is going to come to the mob with opinion."

> "I think it's different for you because you're in a position of authority. If someone else had said that, we could have just said no way, but when you say it, it's different."<br />"I want to say that no one in the mob has more authority than anyone else, even if I try to make it look that way."<br />"I think you can say that, but there's still going to be that underlying social factor because you're responsible for hirings, firings, raises, etc."

In the last year, I have mobbed with at least 100 different people. Want to know who was the worst person at mobbing?

Me. More often than anyone else, I was the problem.

Over time, I'd like to think our teams have learned to trust my commitment to an egalitarian mob. Part of that trust has come from me refraining from stating opinions, and instead asking questions and listening to other people in the mob. But you know what? That's not as much fun as expressing opinions.

I have work to do, most of it on myself. This is definitely one of the side effects of mobbing.

---

### Workshop retrospectives

> "I saw some people weren't as involved as others."

> "I had a harder time following along. They were doing stuff but I wasn't involved because I didn't understand what they were doing."

> "I was struggling with the syntax and things of this language so I felt like I couldn't follow along. It's like they were speaking Chinese or something."

> "Just because I didn't speak up often, doesn't mean I wasn't engaged. I was just trying to keep up but not in a bad way."

We've seen this at each of the workshops. Some people pick up Elixir quickly and run with it, and other people need extra time to catch on to the language structure. We plan on this dynamic and work with it.

We spend about three hours total with the language before breaking into mobs. We spend 90 minutes in an interactive Elixir shell (the Elixir REPL), and another 90 minutes on test driven development in Elixir. This is not enough time for even experienced developers to learn a new language, and these workshops are designed for people who aren't experienced developers. We cannot expect any of them to enter a mob knowing what they're doing.

While most participants are new developers, I do accept a handful of more experienced developers at the workshop. Every time we've scheduled one, we hear from people with more experience who really, really want to learn Elixir. I usually say yes but insist they understand that the workshop is for new developers, and that the discussion will be tailored to the experience level of the group. Developers with more experience may be welcome, but in supporting roles only.

This is kind of neat, actually. We get experienced coaches for the new developers who are also sharing the experience of learning a new language. Once we break into mobs, the mobs are on their own. It's not an instructional environment, it's a production environment. They have a project to produce - a real one, something they could take to market with more work - in less than six hours.

---

> "In our group, it was really good when people would explain how they understood things. Not so good when people didn't understand and we were all quiet and we all stared at the screen."

> "I think it was kinda frustrating to slow down quite so much, but after I got over that it made sense and we made a lot of progress after that."

I love these two comments. They expose both the difficulty and the solution succinctly. We need to share our experience with each other, even though we're all in the same space and we think we're having the same experience. We aren't, at least we aren't until we share that experience by thinking out loud constantly.

---

> "I had a hard time expressing myself declaratively. I wanted to come in and say 'That function name doesn't really speak to me.' 'I don't like that function name.'"

> "I cheated a lot at declarative vs imperative communication. Instead of 'Do this.' I said 'I think you should do this.''"

In the workshop, we discuss declarative and imperative languages, both in programming languages and in our spoken language. This is a neat intersection for our students. Most have a little experience with imperative and object oriented programming, but almost no experience with declarative and functional programming. But since every workshop so far has been hosted by either Girl Develop It or Women Who Code, the groups tend to have a lot of experience with parentingm and they relate well to imperative and declarative concepts as they relate to communicating with each other. We get it.

---

> "Because none of us know the language most of us were on doc pages."

> "Two computers with two big monitors? One with code and one with docs and help?"

> "It'd be cool to try with only one computer working and everyone working off that one."

> "I wonder if it's okay for one or two developers to follow their own path, and try things out."

> "In a group that big, there are a lot of different ideas. It's hard to tell how long and how far we should go down each path."

> "There were too many cooks in the kitchen."

> "I've done some mob programming before and I think a little smaller would have been good. Better focus, fewer side conversations."

In the workshop retrospectives, we always get an opportunity to visit the mobbing experience, even if we aren't going to iterate on it together. I'm happy to have the feedback, and some of it has informed later workshops.

---

> "I've never mobbed before. The group seems big to me."

> "I don't think mobbing is for me. I like to work by myself."

> "I want a beer."

Most of the comments tend toward ways they'd like to try it more, but a small percentage of participants just want to say no - they gave it a try, and that was enough for them.

---

### Intern retrospectives

The retrospectives I run tend to be very informational. Also, I like quoting people, or at least paraphrasing them and making sure they approve of my wording. The intern team (four interns, a junior and an intermediate developer) ran their own retrospectives without interference from me. I love how practical they are.

> *What didn't go well?*
> 
> * Not knowing how to rotate sharing the computer, versus pushing and pulling
> * Sometimes we don't want to touch someone else's computer
> 
> *What would you like to try differently?*
> 
> * What if we get really good at pushing and pulling?

This was the first day that the intern team mobbed on their own, and they immediately questioned sharing one computer - and worked out an alternative. "What if we get really good at Git?" I love their solution.

---

> *What didn't go well?*
> 
> * Some concern about how much time it takes to push and pull
> * Github pulling wasn't as smooth as we'd like.
> * Remember to git pull before making any changes.
> * Still too much time in transition, so 15 minute turns seemed a bit slower.
> * We were lost sheep but not totally lost.
> 
> *What would you like to try differently?*
> 
> * Define roles (navigator, facilitator, driver, bug squasher)
> * No one else has a computer open
> * One computer for the driver and one for research
> * Essentially, don't work individually
> * Trade more frequently
> * Set an alarm for turn-taking
> * Maybe 20 minutes each

---

> *What didn't go well?*
> 
> * Turns and roles of cards didn't go well today.
> * Total failure of Facilitator's role :(
> * Sometimes it's still hard to believe that your questions are valuable
> * Group morale is low today
> 
> *What could be done better next time?*
> 
> * Remember to put on timer, facilitator should take notes
> * Try a cool new ruby timer for mob turn-taking: https://github.com/RubySteps/mob_rotation
> * We should have bio break more frequently.

The intern team chose to have more defined expectations of themselves and each other. I haven't seen this in any other mob, but the interns are the only team that mobbed every day all day, and by the end of their internship they had done that for twelve weeks. Their experience with defined roles (they even used index cards to indicate who had what role at any given time) had ups and downs, but they stuck with it most days until the end of the internship.

---

> *What still has you baffled?*
> 
> * Why it didn't work for the first time???
> 
> *What went well?*
> 
> * Everything works
> 
> *What could be done better next time?*
> 
> * Nothing, today was fabulous

These were from the intern team's last day of mobbing. Their project shipped and has been a huge success with the users.

---

## Everything we did right

We've done mob programming in three different contexts, and the goals for each context - and for mob programming with each group - have been different.

### My team

When we've mobbed as a team at work, we are a group of mostly senior developers, often including developers from other teams (mobbing looks like a lot of fun, so other people want to do it with us) and domain experts we invite to join us. In this context, my primary goals are three-fold.

* **Team development.** I want to see the team improve, and I want to see the individual developers on my team improve. I put this goal first in the list because it's actually my primary goal. I'm a purist and a perfectionist, and I want every member of my team to stand out among the best developers in the state. And we do.
* **Value.** Developers that write simple, correct code can change the world, but only by shipping it. We don't just ship code, though. We want to ship value for the user, for the customer, for the company, and for our team.
* **Code quality.** I believe a good developer writes code that is simple and correct. That's all. Easy to reason about, and demonstrably correct in what it does. My goal as a manager is to make developers that write simple, correct code, and our goal for mobbing is to make more developers better, more efficiently, while shipping value for our stakeholders and customers.

#### Team development

> "It's better for us to work as a team sometimes, even if we don't otherwise work on the same project. It's good for the team."

> "The mob experience I had before was very different. This one we did a lot of 'yes' to things. The other one was like 'No we're not going to do it that way, no we're not going to do it that way.'"

> "I noticed a few times that the driver would make a statement along the lines of 'This is my opinion but feel free to disagree.' I feel like that should be an implicit understanding, that every statement can and should be challenged."

> "I think my favorite thing was that everyone made an effort to make sure we were all on the same page."

> "I learned some Scala. I got an idea of the project. I wouldn't have been involved in the project or in Scala except for this mob. Otherwise I wouldn't have learned anything on this."

> "I didn't know anything about React when I sat down. I learned a lot more about React in 2.5 hours of mob programming than I would have in a day on my own."

> "I learned a lot from this process. About libraries I'd never seen before. Some testing concepts. Even just refactoring the tests, to use a library that we weren't sure about. We weren't sure how it worked, so we refactored to understand the library better. Today we had a limited time frame, and the fact that we took the time to refactor is a definite positive."

> "I didn't think I was going to be able to contribute. But I feel like I did, and I learned stuff too."

Team cohesion while mobbing was really impressive to me. I've been on teams that don't need or want to collaborate, teams that turn their collective nose at code reviews, let alone pairing. Mobbing helped us help each other. We didn't just work together, we worked on ourselves and each other. We acknowledged each other's strengths and learned from them. We validated each other's weaknesses and helped strengthen them.

A lot of that cohesion has continued, but one thing I try to do is move my people to other teams as soon as they want. Every developer that moves from my team to another brings skills for code quality - pure functional programming, functional first development, property based testing, etc. - that team probably doesn't have. Likewise, they bring team building skills, communication skills, and collaboration skills that we've learned, in large part, through mobbing.

---

#### Value

> "The ability for others to look ahead while she's working on a problem, so she can keep her focus."<br />"With that, different people can pursue different avenues looking forward."<br />"Faster for me to resolve issues just because people are looking at different things, comparing stuff, instead of just me going back and forth. I might miss something."

> "Our driver got called away to a meeting and we continued without missing a beat."

> "It was pretty cool that some of the boilerplate we had to do, Nhat could just rattle off the top of his head, where it would have taken me a half hour to figure it out."

> "My worst times to code are between 2 and 4:30 in the afternoon. I think it went better in a mob. I think it might be more productive than working individually in that slow period."

> "As the driver, more of my mental capacity was used keeping up with all the suggestions rather than trying to think of a solution of my own."<br />"It was easier for me because I was the one who was trying things, rather than researching and thinking about what'll work."

> "I think once we figured out what our idea was and what we were heading for, we all pulled together and worked on the solution. That's what was neat, seeing us all work together."<br />"We kicked butt. People loved our ideas and they were very complimentary of our work."

> "We accomplished more in a short time. We built a project without a bubnch of complexity. Because we worked together we built something simpler than we would have had we worked separately."<br />"I second that, that's what I would have said."

> "I think mob programming means we end up with less technical debt."<br />"I would agree."<br />"I agree, and I think it goes along with what was said about the complexity because I kept getting pulled back a bunch of times from what I would have done, and I think what we ended up doing was a lot simpler."<br />"I agree I think we end up with simpler code, so it's possible. It'd be nice to follow some projects over a longer time to be sure."

Too often, when we talk about value, we are talking about short term value: productivity of the developer and the team, in terms of story points delivered. I can see the merit there, but I think that story points are a short-sighted way to measure value.

To me, the average developer is one who can deliver the story quickly. The exceptional developer makes better decisions along the way, decisions that deliver more value in the long term. The exceptional developer delivers the story, but with less code. She writes code that is more secure. She uses fewer dependencies, and has less complexity in her code as a result. We can read and reason about her code, and so can the developers who will maintain it in the future. She uses clear abstractions and they fit the whole problem, not just the story she worked on, so her code can be extended without being rewritten. She doesn't deliver technical debt. She demonstrates that her code is correct. Her code scales in production.

If we have even one exceptional programmer in our mob, then the mob will deliver better long term value. Once they've done that, each member of the mob is also more likely to deliver better long term value in the future too.

---

#### Code quality

> "I personally think it went better than what I would've gone through by myself"

> "It was easier to find bugs. Saved time on that part. Plus multiple people on the same problem. Especially while I'm learning."

> "Different people gave me different perspectives for looking at the problem. Fresh perspectives than what I would have thought of."

> "We did a really good job of bouncing off each other's ideas at the beginning of the day to come up with our solutions. I don't think it was any one person's ideas that got built."

> "This is kinda a plus and a minus. A lot of feedback off comments and what everyone is thinking. Good because I could make multiple hops off of what people were saying. Bad because we were queuing up things to do."<br />"I like that everyone could feed off other people's ideas. I think things queuing up was a good thing because working individually, it takes more time to think of all those ideas."<br />"But for what to do next, how to choose? Just in the order people recommend them?"<br />"I think the problem of which thing to try next is a good problem to have. Having a full queue is better than an empty queue."

> "I probably never would have dug into the source code for Jest or jsdom if it had been just me."

> "It's nice that I'm not solely responsible for any bad code. There's shared responsibility for good and bad code."<br />"I think that the result product will be less bad because there's got to be some better coders on the team. Teams with mixed levels of experience will turn out better code. And better coders."

From my perspective, the code we wrote in mobs was dramatically better quality than the code we write individually. First off, we were more strict about process. No one was willing to say, "Hey, let's call this a spike and not write any tests." We were much more likely to use test driven development to explore the problem and create the spike.

Our mobs frequently include stake holders and domain experts. We get closer to what is needed on our first try. But sometimes it's embarrassingly easy to accept a spike that works, even if the code is ugly, especially if we have someone with the next priority waiting for our attention. Sometimes is scarily easy to ship code that delivers on a short term value, without regard for long term value.

This is the primary danger of Agile software development, in my opinion. We ship value, sure. But as soon as the short term need is met, that story no longer has a priority, so we move on a story that does. Yet each story only deals with short term value, and not the long term needs of the code base. Refactoring, technical debt, tests, code quality in general - these are all underrepresented by the system, meaning that we achieve them only through discipline and training. Often, that discipline involves going against the wishes of our product people and stake holders.

Mob programming is a system for turning out quality code, before we even put it in the hands of the product owner. Where any one of us might say "this will do the job", the mob is more likely to support another test, some more refactoring, removing dead code. The mob is more likely to ship code that is simple and correct, even when product is anxious. That means the mob is less likely to ship defects, security flaws, and technical debt.

We all want to ship value, early and often. The quality code our mobs ship represent long term value: code that works now, and has significantly lower maintenance costs in the future.

---

### Functional programming workshops for new developers

> "We made a shopping cart! OMG!"

Some of our mobbing happened at my Ounce of Elixir workshops, with brand new developers learning functional programming and the Elixir programming language in a two day workshop. They mob most of the second day (6 hours or so) on a real problem, building a shopping cart service using event stores and command query responsibility segregation.

Our mobbing goals with workshop participants are very different from mobbing with my team. First and foremost, **I want the students to feel successful**. Two days isn't a lot of time for learning facts about a programming language, but it is enough time to feel empowered.

> "I think it's amazing that even though everyone there knows very little we could still figure something out."

> "When we started I thought we weren't going to get anywhere. We got a lot farther than I expected. I think we were all surprised every time something works."

> "I feel like I learned faster in a mob."

> "Mob programming is working well. There's a good constant dialogue that feels productive."

> "It's kinda less hacky. You have other people looking at you code, so you become more aware and think things through."

> "I don't think it'd be possible to do any of that on my own. Although it was cool to do, I'm not sure on my own I'd be able to do all that much."

> "I think it was good to watch your code evolve as well. You start doing it one way and then it goes down another way."

> "It's a group effort, everybody is influence the code."

> "I felt like my purpose wasn't to build something but to help everyone else build something and to be able to go home and do it more."

> "I was amazed that Alicia told me at the end 'I've never programmed before' and I didn't believe her. Everyone's just contributing, and even if you don't know the techical aspects of an idea you can still kinda get there."

> "It's great to learn things and do some examples, but seeing how you can use it is really good."

> "I don't think I would have been able to end up with the code we have after the same amount of time on my own."

> "I'm a newby and I always think 'I don't understand much, I don't know much.' But I kept up with it. And it's more comforting to me, that I want to keep going on this."

> "I understand functional programming much better now."

> "I feel very energized. I feel like I want to go home and do programming."

We have other goals for mobbing, but they are distant seconds. Participants are **learning development skills**, not just the language. **Retention** is worth considering, but as yet we haven't measured it. **Networking with other new developers** can be beneficial. But mostly, we want students to feel like they succeeded.

> "Our code is clean."

> "We weren't stumbling over the language. We didn't spend much time in docs. We didn't spend much time figuring things out. When we needed documentation, it was easy to find the relevant stuff really quickly."

> "I'd feel comfortable experimenting in the shell and expanding on what I learned today. I learned more today than I could have on my own in the same amount of time."

> "I picked up five or six patterns by saying, 'How do you do this?' and somebody telling me how to do it. I very much appreciate being able to pick up on the patterns right in the moment in the problem I'm experiencing right now."

> "I feel confident that I can learn to program. It's not completely far away, out of my reach. It's something I've wanted to learn for a long time."

Of course, one of our goals was to **learn how to do mobbing well**, and the functional programming workshops gave us great opportunities to see how mob programming works. It's a difficult environment. We have mostly inexperienced programmers, working in a language they don't know, on a tight time frame, solving a reasonably difficult program in a completely unfamiliar way. Amazingly, every mob has created a working shopping cart, plus we learned about how the students felt mobbing helped.

> "The mob was far less stressful than I thought it would be."<br />"It was far less intimidating than I thought it would be. You had everyone working, everyone looking for something to work so you never really gave up. The environment was motivating."

> "I think it was quite exciting as well to be collaborating to something that looked quite complicated, and that everyone contributed part of their knowledge, it was really quite amazing."

> "I did a coding workshop earlier this week, and after this session I think it made everything a lot less daunting. Collaborating this way is brilliant for new programmers."

> "It was quite nice that roles weren't assigned, that we just sat down and started talking and swapped roles constantly. It kept it interesting."

> "It was also more productive as well. At one time we weren't working on just one problem. People were searching for other things as well at the same time."

> "It felt more productive than on your own. Because you're sort of constantly going, it felt like you got more done."

> "I think you don't get bored quite so easily. Normally when I work alone I get bored quite easily, but in the mob you keep more focused."

> "I felt like I learned a lot more when I was driving, even when I was just like being a typewriter. I think we should have done shorter terms driving and everyone drive more often."

> "I think it's a good way to learn in general. Maybe not as productive as eight people who have more experience on their own. But if you don't have eight people who know what they're doing, it's going to be way better for them. And even if you're more experienced, it's gonna keep you more focused."

> "It feels a lot more sustainable and engaging. I'm interacting with people the whole time and not just staring at my screen. Not as frustrating."

> "Just to reiterate, maybe you gotta drive to learn."

---

### The intern team

Our goals for mobbing with the intern team were kind of a mix. We wanted the interns to come away feeling successful, and we also wanted them to ship quality code that delivered excellent value for our very real customers.

The intern team did so much right it's hard to know what to include. Here's a sample of the things they felt were particularly right over three months of mobbing, roughly in chronological order.

> *What went well, what you want to do more of?*
> 
> * We figured out bugs together.
> * We accomplished something - we actually wrote some code and solved some problems.
> * We were focused on the same thing together.
> * We found more different resources to help problem solve.
> * It's easier to feel comfortable with your own knowledge level.
> * Figuring out problems pretty easily now.
> * We all took turns more.
> * We noticed the difference between driving and navigating.
> * Pushing and pulling from github works well.
> * Retrospective are useful to get at deeper issues.
> * Using a timer worked really well, when we remembered to use it.
> * It's valuable to see that I'm not the only one who gets stuck on a problem. It's valuable to see how others solve problems.
> * Turn-taking with the cards was good, especially separating the task of researching errors.
> * We remembered the timer.
> * We're getting really good at trouble-shooting.
> * Watching how other people do things is very helpful.
> * Jira training was good.
> * We figured out the installed java location.
> * Tweaking bash! :)
> * We survived without mentors.
> * We did turns and we stuck to 15 min turns.
> * Taking time to make sure everyone understands.
> * We had many issues but team collaboration went well.
> * More flexible with the turn taking.
> * We noticed taking time for thinking makes the turns different.
> * Trying lots of things is good (at least knowing what didn't work).
> * Doing the tutorial first helped us gain knowledge of what we were going to do with pouchdb.
> * Getting a fast answer from the library author online.
> * Refactoring and resolving issue with refactoring.
> * We learned a lot about UI, the importance of UX in production, and the importance of ADA compliance.
> * Variety of turn taking strategies.
> * Julia's code review (she ask us to tell how our code works).
> * Changed everything to ES6 today.
> * Having everyone else there to help when you get stuck.
> * You don't feel so stupid asking questions when you're stuck because everyone is at the same level as you.
> * We stopped and talked about communication in the mob.
> * Everything exploded!!!!!!
> * Thinking out loud was particularly good today.
> * Lots of conversation. Off-topic conversation can make it easier to discuss work topics.
> * Working with Michael. Having Michael explain high-level concepts.
> * Everything works.

## Qualitative before quantitative

In the last year, we've learned a lot about mobbing. Every mob has tried different ideas, and reported back on them. Every mob has had people who left excited and wanting more. Some mobs had a few people who left with doubts. And while we have a lot of data about how people *felt* about their mobbing experience, we've done almost nothing to measure the code they produced.

This was on purpose. Going into mobbing, I didn't know what claims to try to prove or disprove, because I wasn't sure what mobbing would do for us. I just felt confident we would learn something interesting. And clearly we did.

Based on our experience, I can now suggest some testable hypotheses. I think these claims can probably be demonstrated, given an appropriately defined mob and good measurement criteria.

* Code written during mob programming has lower maintenance costs.
* Mob programming produces code with fewer defects.
* Mob programming produces code that is more secure.
* Code written during mob programming is more readable.
* Mob programming meets the functional requirements with less code.
* Junior developers progress to seniors more quickly when programming in a mob.
* Development teams that consistently program in a mob have better understanding of their code base.
* Development teams that consistently program in a mob have more uniform skills.

If you try mob programming, I strongly suggest you start with a qualitative approach as well. The interpersonal skills we learned are significant, and I doubt any attempt to prove the merits of mobbing quantitatively could be successful with an inexperienced mob. Once your team has the experience, I strongly recommend you find metrics and demonstrate improvement. That's what I'll be doing too.
