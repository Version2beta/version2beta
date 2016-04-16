---
pagetitle: Why be functional?
longtitle: My version of "why functional programming matters".
tags: cto dev
author: Rob Martin
published: 2016-04-09 17:00
snippet: In 1984, John Hughes wrote a seminal essay called "Why Functional Programming Matters" discussing functional programming in what it brings to our field, rather than what it leaves behind. In my efforts to understand functional programming, I ended up writing my own, less academic version of a "why functional programming matters" type of essay. In my case, it's more of a persuasive essay.
---

> "[To outsiders] the functional programmer sounds rather like a medieval monk denying himself the pleasures of life in the hope that it will make him virtuous." - John Hughes, "Why functional programming matters", 1984

I've been working on this blog post for 16 years, ever since discovering Erlang in 1999. For most of that time, I made very little progress. I was a self-taught, fairly lousy programmer with a bad case of expert beginner syndrome.[^expertbeginner] It took me years to roll back to just an advanced beginner.

Four years ago I finally started learning functional programming, but I didn't know what made it different (beyond the obvious), or how to learn it, or even why to bother. I had, of course, discovered John Hughes' "Why Functional Programming Matters" paper,[^whyfp] but I didn't know enough to understand it. I'd even found Reginald Braithwaite's "Why Why Functional Programming Matters Matters",[^whywhy] and it took me a while to get it. I needed context, and I'm stubborn enough to discover it the hard way. So I realized I needed to write my own version of "Why functional programming matters". And I've done that, several times.

This effort is called "Why be functional?", and it's more or less a persuasive essay on using functional programming.

Here's a spoiler: My answer to "why be functional?" is **simple, demonstrably correct code**. But that's my answer to most questions about coding craft, so I'll explore it further. We can start with complexity.

[^expertbeginner]: [How developers stop learning: rise of the expert beginner](http://www.daedtech.com/how-developers-stop-learning-rise-of-the-expert-beginner/), Erik Dietrich, 2012

[^whyfp]: [Why Functional Programming Matters](http://www.cse.chalmers.se/~rjmh/Papers/whyfp.html), John Hughes, 1984

[^whywhy]: [Why Why Functional Programming Matters Matters](http://weblog.raganwald.com/2007/03/why-why-functional-programming-matters.html), Reginald Braithwaite, 2007

## Complexity

> "I conclude that there are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies and the other way is to make it so complicated that there are no obvious deficiencies. The first method is far more difficult." - C. A. R. Hoare

What is complexity? There are lots of answers to that. In "No silver bullet"[^nosilverbullet], *Mythical Man Month* author Fred Brooks describes "accidental" and "essential" complexity, putting all code in one category or the other. That's probably correct: the morphology of software, it's form and structure, is complexity by definition, and there is no current way to avoid it.

Fortunately, complexity is relative and we can reduce it if we can identify it. So here are some other places we look for complexity, drawn from various sources.

* Complexity is any code that can be, but hasn't been, decomposed into simpler components.
* Complexity is the interrelationships and dependencies of software components. Complexity is the degree to which one piece of software is dependent on another.
* Complexity is the enemy of reliability. Complexity and reliability are inversely proportional.
* Complexity is the part of our code that isn't beautiful. Beauty is the ultimate defense against complexity.
* Complexity is code. If we could accomplish our goals without programming, we would.

[^nosilverbullet]: [No silver bullet](http://faculty.salisbury.edu/~xswang/Research/Papers/SERelated/no-silver-bullet.pdf), Fred Brooks, 1986

Why is complexity bad? I'll give you four simple reasons: Complexity is code that we can't reason about, can't test, can't prove, and can't trust.

* We can't reason about our code.

We do two kinds of reasoning when it comes to our code. We do "informal" reasoning, which is kind of like crawling inside the code and looking around, figuring out how things should work. We also do "formal" reasoning, which applies math and logic to our code. Complexity actually means we can't do formal or informal reasoning, but in this case I'm referring to informal reasoning, our ability to understand the code.

Being able to reason about our code is important, because we spend far more time and money maintaining a code base than creating it. Code we can't reason about is not only going to take longer to maintain, but we're going to maintain it poorly because we don't understand it. Both problems translate to larger lifecycle costs.

* We can't test our code.

Complex code is difficult to test. We mock the libraries we depend on. We build ourselves a dingus.[^dingus] We fake our IO - or worse, we don't. We try to identify edge cases and fail. Or worse, we don't. 

[^dingus]: [Dingus: a record then assert test double library](https://github.com/garybernhardt/dingus), Gary Bernhardt.

* We can't prove our code.

This is where formal reasoning comes in, but honestly, formal reasoning almost never comes into our code. It's difficult to prove anything about imperative code, and complex imperative code may fall outside of what's possible to prove. After all, it only takes 24 bytes to represent more different states than there are atoms in the earth.

* We can't trust our code.

This is the bottom line. If we can't reason about our code, and we can't demonstrate the correctness of our code either through tests or logic, then we don't have reasons to trust it, except to the degree we trust ourselves. That used to be enough, but we're learning to build better software.

> "[W]e have to keep it crisp, disentangled, and simple if we refuse to be crushed by the complexities of our own making.” - Edsger Djikstra

## Simplicity

> "It is easier to write an incorrect program than understand a correct one." - Alan J. Perlis

What is simplicity? It's the opposite of complexity. It's the lack of complexity, the other end of the spectrum from complexity. It's achieving our goals and meeting our needs without introducing unnecessary complexity.

I use the same standards described under complexity to test whether code is simple. I call it a "simplicity test".

* Can we reason about the code?
* Can we test the code?
* Can we demonstrate the correctness of the code?

The better our code meets these standards, the more simple I believe it is.

This test works for more than evaluating code we've written. I use it to think about how patterns, languages, or even programming paradigms affect my work. Shortly, we'll use the simplicity test here to functional programming, but for now let's try it out with Object Oriented Programming.

### Applying the simplicity test to Object Oriented Programming

> "OO makes code understandable by encapsulating moving parts. FP makes code understandable by minimizing moving parts." - Michael Feathers

We can use the simplicity test as a lens to view object oriented programming.

* Can we reason about the code? Yes, we can reason about well-written OO code.

At least, we *might* be able to reason about well-written object oriented code, but in practice there's a lot of OO code out in the wild that's extremely difficult to reason about. There are some good reasons for this.

A core principle of object oriented programming is encapsulation. We hide complexity, even reasonable complexity, inside of objects to make sure that most programmers don't ever have to experience it. Unfortunately this means that we can hide complexity, even unreasonable complexity, inside our objects because no one but us are ever going to see it. Later, when we're maintaining code, we are often inclined to increase complexity of someone else's code because it's hidden.

Object oriented programming not only encapsulates complexity, but offers a lot of it. Our objects have mutable state, and behaviors to mutate that state. It's often hard to explain why we're in the state we are, because state can be mutated anywhere inside the object by any code that accesses the object. We don't typically keep track of how our state changed in the past, so we can't track how we got where we are.

* Can we test the code? Yes, we can test our code. We do it all the time.

In practice, in order to make our code testable we follow a lot of principles and patterns to try to keep our complexity down. Even then, it's often difficult to test our code, even just unit tests, and our tests often take a long time to run. Our objects are complex, our state is mutable, and our code is hard to reason about.

Of course, most code doesn't have tests, and composing tests for legacy code is often an art form.

* Can we demonstrate the correctness of the code? Yes, it's possible to write OO code that can be formally verified.

In practice, very little OO code is written for formal proof and very few OO programmers would even know where to start. 

Using the simplicity test, we can see it's possible to write simple code in an object oriented language. Of course we knew that, because we've all written simple code in object oriented languages. We've also seen our OO code go from simple to complex, often feeling like we fell off the complexity cliff and didn't even see it coming.

## What is functional programming?

> “Inside every well-written large program is a well-written small program.” - C. A. R. Hoare

First and foremost, functional programming is math. A lot of programming is math, but in imperative programming we use that math to make programs that don't need to follow rules the way math follows rules. With functional programming, we figure that the more a language follows the rules of math and logic, the more "purely" functional programming it is.

Functional programming is made up, mostly, of functions. Pure functions have a few characteristics that follow simple rules of math.

### Functions

* Functions are referentially transparent.

"Referential transparency" is a characteristic that says a function will return the same value whenever it's given the same arguments. Another way of saying this is that nothing about the state of a program can affect how a function works. Another way of saying this is that a function call and its result are always interchangeable, without impacting the meaning of a program.

This is what we expect from math, too. Math is a hard science; it doesn't change from one moment to another, even when the world around us changes.

* Functions can be composed of functions.

We can apply one function to the result of another function. We can string a bunch of functions together to make a program. In functional programming, that's typically how we make a program.

```
f(g(x)) // composition
g(x) |> f // or pipelining
x |> g |> f // or more elegant pipelining
```

This is also what we expect of math. We can reason mathematically about functions applied to other functions applied to variables, without solving for the functions. 

* Functions can be distributed.

Because a function will always return the same value for a given argument, it often doesn't matter what order we do things in, or even on what computer we do things. We can distribute functions across a cluster and we'll always get the same result, because the result can not be dependent on the state of the computer.

Again, this is what we expect from math. If we're solving a formula for a value, the order in which we solve uncomposed functions doesn't matter. We can reason about it without solving it. We can even compose functions and reduce them without solving for a specific value.

* Functions can be evaluated lazily.

Often with functions, we have the option of not figuring out a result until we actually need it. Just because a program has code arranged in a certain order, that doesn't mean it has to be run in that order. Instead of calculating and storing a result, a language could just remember how to figure out the result if and when someone actually tries to use it.

There's some question about whether this is an important part of functional programming, but we tend to see it more in functional programming than in imperative programming.

* Functions can be arguments to other functions.

In functional programming, we can pass a function as an argument to another function. This characteristic of functional programming has been pretty widely adopted in imperative programming languages too. In fact, Javascript would hardly work without callback functions.

Common functions that use higher order functions (that is, functions as arguments) are `map`, `filter`, and `reduce` or `fold`.

* Functions can be recursive.

Recursive functions are hardly limited to functional programming languages, but they are used very often in functional programming. This is because pure functional programming doesn't provide mutable state, and our typical imperative manner of iterating requires mutability. As L. Peter Deutsch said, "To iterate is human, to recurse divine."

### Immutability

Functional programming languages don't do assignment the way that imperative and object oriented languages do. In imperative languages it makes sense to say something like "Set X to True" or "Assign 1 to Y". In declarative languages, including functional languages, we aren't doing assignment, we're describing the world. If we tell a functional language that Y is equal to the value 1, and then we try to say that Y is equal to a different value, the program may just say "No it isn't. You already told me it was 1." (Actually, it'll probably say something like 'right hand and left hand values do not match', because that's what the language is doing, matching names and values.)

Immutability comes to us from two directions.

* Remember how we said a function call applied to an argument is always interchangeable with the result, and can't affect the meaning of a program? That also applies to any reference to that function call. If we say `x = f(1)`, then `x` always has to be interchangeable with the result of the function call. If `x` can change, then it's not guaranteed to be interchangeable.
* Most of us tend to think about programming from a single-threaded perspective, but there's nothing about the math that suggests things happen sequentially unless there's causality. So what happens in a multi-threaded environment with mutable data? One thread might change data that another thread is accessing, or intends to access. That's not thread safe, and as a result we can't guarantee referential transparency.

These are advantageous to us as developers because they make it easier to reason about our code. If we know what `x` means, we always know what `x` means. Values, references to values, and values returned by functions will always be consistent.

This makes a difference in informal reasoning, but it also makes a difference in formal reasoning. If we have these invariants, if functions are referentially transparent and values can't change, then we can use math and logic to draw conclusions about the properties of our code. The conclusions we're most likely to want to draw is that the code is correct to its specification.

### Side effects

> "In the end, any program must manipulate state. A program that has no side effects whatsoever is a kind of black box. All you can tell is the box gets hotter." - Simon Peyton-Jones

Functional programming doesn't eliminate side effects. After all, side effects are how we get value from our work. Imagine this conversation:

Functional programmer: "I wrote a purely functional program that will transform our data."

Product manager: "Cool, how do I get data in?"

Functional programmer: "You can't."

Product manager: "Um, how do I get data out?"

Functional programmer: "You can't."

Instead, functional programming isolates side effects, because side effects represent the real world and the real world is messy. It may be governed by physics and math, but the complexity is out of this world! We manage that complexity by isolating it.

One way to isolate it is to keep side effects at the edges. For example, we can bring in data from the real world, and then pass it through a series of functions that transform it, and then return the transformed value to the real world. This reduces almost all the complexity. We have a "given" at the beginning, a series of functions we can reason about, and a way to return a result at the end.

Another way to isolate the complexity from side effects is to wrap it up in a model of the world, and pass that around as an argument. Actions that affect the world transform our model of the world into a new model of the world, which is passed on to the next function.

Some functional programming languages just give us an imperative way to do side effects, and trust us to not use that power foolishly.

Ultimately, getting data in and out of our functional program are imperative, not declarative, operations. We have react to events or respond to commands or write to a file. These operations aren't referentially transparent - they can return a different value each time they're called. They aren't immutable, and in fact we may have many different actors changing the data concurrently.

### The simplicity test, applied to functional programming

We've already discussed a way of looking at a program and determining if it's simple. We called it the simplicity test. We can apply that test to functional programming as a whole.

* Can we reason about it? Yes. Functional programming can make it easier to reason about our code. 

Referential transparency promises us that we can trust the result of our function calls. The results won't change based on anything but the arguments right in front of us.

Function composition gives us a way to look at our code in different levels of abstraction, from the implementation details of each step, to the way the steps are put together.

Immutable state ensures that we always know the value of things. If we transform data, we always get new data back.

Side effects are isolated, leaving us with a very stable view of our system.

* Can we test it? Yes. Functional programming makes unit testing very easy, and integration testing easier.

Referential transparency promises us that nothing but the arguments to a function will change the result of a function. If we write pure functions, we should never have to use mocks in our unit tests.

Function composition with referential transparency gives us confidence that a program tested at a unit level will perform predictably.

Side effects are isolated, and they're almost always limited to IO libraries. We don't need to unit test IO when it's isolated; the IO libraries come with their own unit tests.

* Can we demonstrate correctness? Yes, we can often use formal methods and more effective testing to demonstrate our code will perform correctly.

Functional programming was not only designed to be provable, it comes from math that's designed to be used for proofs. In 1935, several years before the first general purpose computer, Alonzo Church published about lambda calculus, a math for demonstrating the completeness and correctness of algorithms. Today almost all functional programming languages are based on lambda calculus.

Not all programs are deterministic and not all can be proven correct, but with functional programming we are almost always better able to demonstrate correctness.

## Programming our brains

> "A language that doesn't affect the way you think about programming is not worth knowing." - Alan Perlis 

While functional programming meets our simplicity test better than object oriented programming, that's only part of the advantage. Functional programming also changes the way we approach our work, and think about the problems we're solving. I think the way it changes our thinking is as important as how it changes our coding.

### Imperative and declarative language

Functional programming is a subset of declarative programming, and object oriented programming is a subset of imperative programming. One way of thinking about the difference is whether a variable is set equal to a value, or if we are informing our program that a variable has the same value as something else. In imperative programs, we instruct the computer to do things: set X to 0, calculate a result, print a message. In declarative programs, we describe relationships between things and then ask the program to give us conclusions: There is a function like this, and X has the same value as 3, so what do we get if we solve the function with X?

We speak in declarative language most of the time, especially with other adults. We share experiences ("That meeting sure was a bore!"), and talk about our feelings ("If manager Rob does that one more time, I'm gonna blow my fuse.") We tend to dislike adults who speak imperatively to us ("Make me a sandwich. Sudo make me a sandwich."[^sandwich]) and think of them as jerks.

It turns out that imperative communication is easy to find between adults and children. "Close the door." "Pick up your shoes." One the other hand, declarative language is amazing with kids. "I'm cold because the door is still open." "I see your shoes are in the middle of the floor. I'm afraid someone will trip over them." It helps toddlers develop surprising vocabularies. It helps teens relate to adults and each other. It helps kids with autism increase their verbal and social skills. It literally grows the prefrontal cortex.

Robin Dunbar, the guy who described Dunbar's Number, has done research connecting the size of our orbitomedial prefrontal cortex and the size of our social network, the number of meaningful social relationships we can manage at one time. The upshot is that people with bigger orbitomedial prefrontal cortices have larger social networks, approaching 220 people.

Good news for programmers, the size of our prefrontal cortex also seems related to the amount of complex of code we can hold in our head at one time. So maybe declarative programming languages aren't just simpler, but make us smarter and better at managing social relationships.

"I'm a functional programmer, and gosh darn it, people like me."

[^sandwich]: [https://xkcd.com/149/](https://xkcd.com/149/)

### Identity at the corner of State and Time

Functional programming changes how we model the world in our code, and as a result how we see the world.

We know that objects make for a decent abstraction in our programming. That's true. It's a reasonably effective way to model the real-world. The problem is that objects have no way to account for the passage of time, and in the real world, "identity" needs to account for the passage of time.

* In object oriented programming, **identity is the present state of an object**.
* In functional programming, **identity is a collection of immutable states over time**.

It's fair to say "I'm not the person I used to be." But who I used to be is an integral part of who I am today. The object-oriented way of viewing objects doesn't account for this. Instead the state of an object is frozen in the current moment.

In functional programming, we don't mutate state, so we have a different state for every changed version of a model. I am who I am right now, but I'm also a collection of all the people I used to be. Functional programming enforces this in its most basic pattern: new state is old state transformed by a function. While we don't have to keep every previous version of our state, each version was created separately and we often do choose to keep them.

### The power of a restrictive language

My favorite tech tee-shirt reads "My compiler compiled your compiler". That's the power of a systems language - it can do anything, including creating new programming languages that expand the possibilities. But how much of that power do we need? Sometimes our systems languages feel like driving a semi tractor to the grocery store. More than enough power to transport a dozen eggs, fast enough to hit the speed limit, and really difficult to drive around and park. And I hate to think about what happens in a fender bender.

Languages with a few, well defined, and useful abstractions are limiting in comparison to a systems language. My Toyota can't pull a semi trailer and can't easily transport 60 head of cattle. It can however transport a dozen eggs, hit the speed limit, and it is easy to drive and park.

There are languages that have power and flexibility to do almost everything with a computer that you can imagine. Many of these languages give you wide choice of how to model a problem, how to address control flow, how to structure your data. Unfortunately, all of this flexibility means that there many more ways to solve any given problem, and they don't all have the same merit. All of the power means that we can make bigger and bigger mistakes. It's like Bjarne Stroustrup said: "C makes it easy to shoot yourself in the foot; C++ makes it harder, but when you do it blows your whole leg off."

For me and my team, I like a restrictive language. Give me fewer abstractions that fit more situations. Give me abstractions of the other languages' abstractions. A language with fewer abstractions can be learned faster, designs are done sooner and with less code. We focus on the problem instead of the implementation.

> “Mathematicians stand on each others' shoulders. Computer scientists stand on each others' toes.” - Richard Hamming

There's another way of looking at this question of how languages present different abstractions. I heard about it from Phil Wadler in a talk about Curry-Howard isomorphism, which is just a fancy term for the way these two dudes realized that mathematicians and computer scientists kept discovering the same stuff.

* Hilbert-style deduction systems (Frege & Hilbert, 1925?) <-> Combinatory logic (Curry & Fey, 1958)
* Natural deduction (Gentzen, 1935) <-> Typed lambda calculus (Church, 1940)
* Type schemes (Hindley, 1969) <-> ML (Milner, 1975)
* Modal logic (Lewis, 1910) <-> Monads (Kleisli, 1965; Moggi, 1987)
* Classical-Intuitionistic Embedding (Godel, 1933) <-> Continuation passing style (Reynolds, 1972)
* Linear logic (Girard, 1987) <-> Session types (Honda, 1993)
* Intuitionistic logic <-> Typed lambda calculus <-> Cartesian closed categories

After hearing Phil Wadler present his talk on "Propositions as Types",[^wadler] I had a breakthrough. Wadler seemed to desribe that some languages were invented, and some languages were discovered. This fit with my idea on simpler, better abstractions and put it more neatly. Some languages felt to me like they were derived from the rules of the universe, and others felt like they were invented in someone's garage.

The Curry-Howard (-Lambek) isomorphism gave me the proof I needed to trace languages back to the abstractions introduced by both computer scientists and mathematicians independently. Here are some examples:

ML family languages:

* ML (Milner, Gordon, Wadsworth, 1979)
* Haskell (Hudak, Hughes, Peyton Jones, and Wadler, 1987)
* O'Caml (Leroy, 1996)
* F# (Syme, 2006)
* Elm (Czaplicki, 2012)

Lisp/Scheme family languages:

* Scheme (Steele and Sussman, 1975)
* Clojure (Hickey, 2007)

Prolog/Erlang family languages:

* Prolog (Colmerauer, 1972)
* Erlang (Armstrong, Virding, Williams, 1988)
* Elixir (Valim, 2012)

I contrast these languages with Scala (Odersky, 2004), a general purpose programming language inspired by Java's deficiencies and supporting functional programming. I've also heard it called "a slippery slope to functional programming" for Java developers.

[^wadler]: ["Propositions as Types")[http://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf], Philip Wadler, 2015

## Functional-first programming

Having built the case for pure functional programming and even identifying a bunch of languages that expose clean and functional abstractions, let's finish up with ways to bring some of the good things from functional programming into our imperative environments.

I call it "functional-first programming", but I'm hardly the first to make suggestions like these. Some people have simply suggested isolating side effects. Gary Bernhardt has presented it as "Functional core, imperative shell".[^bernhardt]

We can drag the low hanging fruit from functional programming into our imperative languages by following two simple steps:

1. Code everything you can without side effects.
2. Then code your side effects.

These two steps are not as simple as they look, but if we follow them we get a bunch of benefits.

### Benefits

* Our functions should have referential transparency.

If our functions have no side effects, then the only effect they have on the meaning of our program comes from the value they return. They are referentially transparent, and simple to reason about.

Our functions should be pure, at least within the limits of the language. For example, any language that passes arguments by reference risks mutating those arguments. Python, for example, passes object references by value, which means the function will be looking at the same object in memory that was passed to it. If the standard ways of interacting with that object also mutate it, as Python Arrays do, it will mutate it in place and have side effects unless the developer knows to avoid this.

* Our program is a composition.

If our functions are fairly pure, much of our business logic will be a composition of functions that transforms our inputs into our outputs. Again, we win on simplicity and reason.

* Our testing story is beautiful.

Pure functions are fast and easy to test. We can write better tests about them. We don't have to mock anything. Each test runs in virtually no time, and when you put all your tests together they don't add up to very much time.

Because our side effects are isolated, the part of our code that does IO doesn't do business logic and doesn't need unit tests. That means we don't have to mock IO libraries and we probably don't have to inject dependencies and our testing is simple.

* Our business logic is separate from our IO.

We don't need functional-first programming in order to separate our business logic from IO. We've been doing this for decades with the MVC pattern and numerous others.

Separating side effects, however, takes this to a new level. It means that our functions can be as pure as possible. Our business logic can be written without even referencing framework or database, and we shouldn't even have a dependency on libraries that do IO.

* Our IO is modular.

Moving all of the IO to the edges has a nice advantage too. Anything that does IO can be easily added or replaced. If we decide to change our database layer, it's all in one place. If we want to add another interface, we can tack it onto the shell with the other interfaces.

### Disadvantages

* We're not really doing object oriented programming any more.

Functional-first programming isn't object oriented, and that's going to be hard for a lot of teams. Even if you make utility classes and singletons, it's still going to feel weird, and it's going to look weird, and it's going to be weird to an OO programmer.

* Requires training and discipline

I like languages that make it hard to do things wrong, according to the abstractions that language provides. Doing functional-first programming in an object oriented language is doing it wrong, because it doesn't fit the abstractions that an OO language provides.

As it happens, a lot of languages don't actually care if you do OO or straight up procedural / imperative code. So it might not feel terribly wrong. It does take training to re-learn how to program in our favorite OO languages, and discipline to keep everything separate. We rely on the developer to do things well, because the language isn't going to help.

* May not fit well with frameworks (but probably will)

It's not just the language that provides abstractions we need to fit into our new workflow. Our frameworks in particular will greatly influence how we think about our code, and fitting the framework to the two principles of functional-first programming can be tricky.

### The simplicity test for functional-first programming

Let's go back to the simplicity test, and see how functional-first programming fares.

Is it easier to reason about our code? Yes it is, because of our functions are referentially transparent, fairly pure, and composed; our state is exposed and even though it may not be immutable, we're careful not to mutate it; and we know exactly where to find all of our side effects, and they aren't mixed in with business logic.

Is it easier to test? Yes it is, because our functions are fairly pure and referentially transparent, and our IO and side effects are isolated. And since our side-effect code is pretty much all IO, there's no business logic to test and we can skip unit tests altogether and cover IO with integration tests that don't require mocking IO libraries.

Can we demonstrate correctness? We probably can demonstrate correctness, but I doubt we will. At least not typically. If formal methods of proof are important to our market, we're probably already doing them and can continue to do them with functional-first code. If formal methods aren't critical, then we're probably going to demonstrate correctness with really good tests and monitoring, and both are made easier by functional-first programming.

[^bernhardt]: ["Functional core, imperative shell"](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell), Gary Bernhardt, 2012.
