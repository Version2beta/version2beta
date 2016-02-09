---
pagetitle: Functional first development
longtitle: A brief overview of functional first development
tags: dev
author: Rob Martin
published: 2016-02-09 12:30
snippet: This is an introduction to functional first development, a coding and design practice that brings some of the benefits of functional programming to any programming language.
---

In it's simplest form, functional first development has two rules:

1. First, code everything you can without side effects.
2. Then, code your side effects.

Let's say that side effects are any way that a computer program changes the world, or is changed by the world. This includes inputs and outputs, so really anything that gets data into or out of our program is a side effect. Reading from standard input, or a database, or HTTPS. Writing to standard output, saving to disk, sending to a service, pushing to a mobile client. All of these are side effects, and we can wait to code them.

There's another kind of side effect - saving state in variables. This part is sometimes trickey for programmers who aren't used to functional programming, but it's actually not too hard to do with functional first development. We're still going to have state, but during step one we'll only have state in our tests, and that state won't ever be mutated.

## First, code everything you can without side effects:

So before we worry about any side effects, we worry about our program's core logic. Sometimes, it's quite a trick seeing what that logic is without side effects, because we think about our work in terms of how we change the world. But we can find that logic often by looking at the actions our program takes rather than the objects it acts on. We can look at verbs rather than nouns.

Let's use a shopping cart for an ecommerce site as an example. If we look at it from an object or noun-oriented point of view, we might assume that the cart keeps track of it's own state, and it has methods for manipulating that state. So we can tell the cart that we're adding or removing an item and the cart object does all the magic internally ("encapsulated state").

We can also see the core program logic as taking an existing shopping cart, and a shopper's action (our verb), and returning a new shopping cart. This a straight up transformation. We are taking one state and transforming it to a new state.

> New state = Old state, transformed by an action

Maybe this looks like we're mutating state, because we have an old state that becomes a new state based on an action, right? I like to think of the old state and new state as distinct. The shopping cart has different states over time. The old state describes the shopping cart at one point in time (before the action), and the new state describes the cart at a later point in time (after the action.) I like to make a data structure for the cart that lets me keep all the versions of the cart, all of the states over time.

Let's try that. Let's say that our shopping cart state is simply a list of events happening to the shopping cart.

```
[ {add, Eggs}, {add, Milk}, {add, Candy}, {remove, Candy}, {add, Carrots} ]
```

I've simplified things a bit. There are no prices or quantities, and we could keep track of things like who put the item in the cart, and when exactly that happened. But for now let's just assume that Eggs got added before Milk, which was added before Candy and Carrots.

Now our program's core logic is pretty straight forward. All we need to do is take a list of actions, initially an empty list of actions, and be able to add new actions onto the end of that list. Since we probably also need to display what's in the cart at any given moment, we'll also need to transform that list of actions into a representation of the current state of the cart.

Our program doesn't need to make new shopping carts at this point. That would be a side effect. It doesn't need to save the shopping cart. It doesn't need to connect to an HTTPS port. It just needs to be able to do two things: given a shopping cart, record a new event; and given a cart, reduce the list of events into a list of what the cart contains.

The first is really easy to do, in almost every language. Here it is in Python:

cart.py

```
class Cart(object):
  def add(cart, item):
    cart.append(('add', item))
    return cart
```

cart_tests.py

```
from cart import Cart
import unittest
from expecter import expect

class TestCart(object):
  def test_add(self):
    expect(Cart.add([], {'name': 'item'})) == [('add', {'name': 'item'})]
```

Because this is Python, we have some side effects that are introduced in fairly hidden ways. For example, when we create a variable `cart` in the `add` function, we're actually creating a mutable list. On the next line, `cart.append` mutates that list, because Python doesn't give us an immutable list. Also, Python passes object references by value, which means it's easy to make functions that change variables that are passed as arguments if we're not careful.

But even in Python, we can write our code as if it is without side effects. We can do that, because that's how we're going to use it. Our test demonstrates this. Our test starts with an empty list, not a variable. We add an item. We expect a new list. And even though Python might pervert some memory along the way, the parts we are allowing ourselves to care about are not mutated.

Here's the same function and test in Elixir, this time without inadvertent side effects:

cart.ex

```
defmodule Cart do
  def add(cart, item) do
    cart ++ [{:add, item}]
  end
end
```

cart_test.exs

```
ExUnit.start
defmodule CartTest do
  use ExUnit.Case
  test "adding to cart" do
    assert [{:add, 'item'}] == Cart.add [], 'item'
  end
end
```

Regardless of the language, writing our code without side-effects makes our tests super easy. Our functions are simple. They always return the same output for any given input. They aren't hiding state. They don't rely on anything but the information they are provided with when they're called. When we test functions written this way, our tests are simple, fast, and easy to understand.

Writing our code without side effects, focusing on the actions and using functions, has real impact on complexity. With objects we tend to absorb and hide complexity. As our code becomes more complex, we change how we represent state inside the object. State is encapsulated - that's the point of objects - and hidden, so as objects gain complexity, that complexity is also hidden. When we write functions that transform state, we can't hide the complexity. The more complex our state becomes, the more likely we'll expose that complexity in the interfaces to our functions. We can't run and we can't hide, but we can simplify.

Here's another benefit from coding the core logic without side effects. There's an excellent chance that we don't need a framework in order to do this part. No Ruby on Rails, no Django, no Express, no Play. We can probably code this part of our program in the plain old language, possibly with (at most) a handful of third party libraries that have limited, well-defined purpose in our code. This also helps keep our core logic code simple.

That's pretty much our goal with functional first development. We want code that is simple and correct. Coding without side effects as much as possible means that the core code is simpler, and because it's much easier to reason about and test, there's a good chance it will be more correct.

## Then, code your side effects:

> "In the end, any program must manipulate state. A program that has no side effects whatsoever is a kind of black box. All you can tell is that the box gets hotter." --Simon Peyton-Jones

After we've coded everything we can without side effects, it's time to add in our side effects.

If we've done the first step right, the only code we have left to write is code that changes the world. Code that saves data to disk, or to a database. Code that sends data to a web service, or a message broker. Code that receives messages from a message broker, or on an HTTPS port. Code that goes out and gets data we want to transform. Code that returns data we transformed to someone, somewhere else.

This works to our advantage. Almost all code that changes the world comes in a framework or in a library. These libraries are often hard to test when they're integrated with our logic, because we need to either learn a framework for testing the framework, or we need to mock the things the library does to change the world, because we don't want our tests to change the world.

There is this neat benefit for us. If we're only using the framework or library to change something in the world, and we don't want to write unit tests that change the world, then we don't need to unit test our side effect code! If we don't mix our logic and their logic together, we don't have anything to mock and unit test. This is because the libraries come with their own unit tests that demonstrate (hopefully) correctness of the library code.

There's another neat benefit. If we ever decide to revisit how our program changes the world, that code is all by itself, totally modular and easy to swap out or add to. Maybe today we're using PostgreSQL, but tomorrow we want to use Hadoop. Maybe today we offer a web interface and tomorrow we want to add a message broker. The code for these features performs only these features, and making changes is simple.

There's yet another neat benefit. Our code scales. If we ever need to run it on more than one server, that's not a problem because our core logic does not depend on local state.

## It's not functional programming, but it's close.

Functional first development is certainly not the same as programming in a pure functional language, but it gives us some of the advantages of functional programming without learning new languages.

* It's easier to *reason about our code*, both from the outside in (we can look at the system and it's not too hard to tell what it's supposed to do) and from the inside out (we can look at the code and understand why we wrote it that way.) 
* It's easier to *test our code*, because our tests are super simple and they run fast. Also, we don't have to unit test our side effects, because our side effects only do side effects and we that's the part of unit tests we mock, rather than test.

We get these advantages, but only in exchange for discipline and training. We keep using the same languages our teams have been using, and the languages provide almost no extrinsic motivation to program in a functional first manner.

Functional first development is an approximation - it gets us half-way to functional programming. To go all the way, we need a pure functional language that restricts us to functional patterns. Restrictions are a good thing, but that's another blog post.

## More functional first development coming

These two rules give us only a brief introduction to functional first development. There is a lot of room left to explore, including the advantages for teaching these techniques to juniors, for refactoring legacy code, and for building large-scale applications. I'll write and present more on functional first development over the course of the next year or so.
