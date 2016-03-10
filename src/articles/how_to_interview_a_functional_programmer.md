---
pagetitle: How to interview a functional programmer
longtitle: Instructions for a technical interview in functional programming
tags: cto dev
author: Rob Martin
published: 2016-03-12 15:00
snippet: Many of us don't know how to interview a functional programmer. We might not even know enough functional programming to tell whether we've got a good one on our hands anyway. This blog post takes us through a full two hour technical interview - including a coding or pairing exercise - with a prospective functional programmer.
---

Functional programming is old. Lisp first appeared in 1958, and the underlying theory - Church's Lambda calculus - was first published in 1936. All the same, many of us don't have a grasp on what it means to be a functional programmer, or even how to tell if someone is a good functional programmer. This is a little bit of a problem if we are the functional programmer in question, and we're trying to get a job doing it For Real&reg;. It's even more of a problem if we are the one hiring the functional programmer and need to evaluate their skills.

This post is about interviewing a functional programmer. It should be useful regardless of whether you're interviewing or being interviewed. If you're the candidate, this post isn't going to give you all the answers, but it will give you context for why these answers are important. If you're the hiring manager, it's also not going to give you all the answers, but it might help you identify a good functional programmer, because she is the one who teaches you why these questions are important.

## Level one: pragmatics

Let's start with common functions. For many people, these three functions aren't just common to functional programming languages, they are what make functional languages "functional". I've heard people say they do functional programming because they use one or two of these functions, and that some language or other is a functional programming language because it provides these functions.

The functions are `map`, `reduce`, and `filter`.

* `map` applies a function to a list or other iterable. It's given a collection, and a function to apply to each element. `map` returns a collection that is the result of the function for each element in the collection that was provided.

In Elixir, a map might be called like this:

```
> Enum.map [1,2,3], fn x -> x * 2 end
[2, 4, 6]
```

* `reduce` is given a list and a function as well, and uses the function to recursive combine elements from the list. In practice this is useful for doing things like summing a list. In that example, the function is simply addition, and reduce adds everything up. For a list `[1, 2, 3, 4]`, the reduce can be viewed as `(1 + (2 + (3 + (4))))`.

In Erlang, a reduce is implemented as a `foldl` and expects to be given an initial accumulator value.

```
> lists:foldl(fun(X, Accumulator) -> X + Accumulator end, 0, [1,2,3,4]).
10
```

* `filter` is also give a list and a function, and uses the function to determine which elements from the list should be returned in a resulting list. If the function provided to `filter` returns true (or a truthy value in a lot of languages) for any given element, than that element is included in the result list.

In Clojure, filters might be used like this to collect all of the single letter items in a list.

```
> (filter (fn [x]
    (= (count x) 1))
    ["a" "b" "ab" "c" "d" "cd"])
("a" "b" "c" "d")
```


*Level one coding exercise*

I'm pretty good at Wordsmith, a Words With Friends predecessor and Scrabble-like mobile game. I'm good enough at it that my kids didn't like to play against me. To make it more interesting, I told them it was fine if they cheat. They can use a computer program to find words they can play - but only if they write the computer program.

That's the coding exercise. Create a program that, given a set of tiles, finds words in a dictionary that can be spelled using those tiles.

Here is a solution in Elixir:

```
defmodule Cheat do
  def matches?(tiles, word) do
    MapSet.new(word) == MapSet.intersection(MapSet.new(tiles), MapSet.new(word))
  end
  def suggest(tiles, dict) do
    Enum.filter(dict, fn(word) -> matches?(tiles, word) end)
  end
end

ExUnit.start
defmodule CheatTest do
  use ExUnit.Case
  test "match" do
    refute Cheat.matches?('a', 'abc')
    assert Cheat.matches?('abc', 'a')
  end
  test "suggest" do
    assert Cheat.suggest('abc', ['a', 'ba', 'fa', 'la']) == ['a', 'ba']
  end
end
```

And here is a solution in Haskell:

```
import Test.QuickCheck
import Data.List

suggest :: String -> [String] -> [String]
suggest tiles = filter f
    where f dictWord = null (dictWord \\ tiles) && null (tiles \\ dictWord)

prop_tile_difference :: String -> [String] -> Bool
prop_tile_difference tiles dict = all (null . (\\) tiles) $ suggest tiles dict

main :: IO ()
main = quickCheck prop_tile_difference
```

## Level two: Operational theory


Side effects
  Mutability
  State
  IO

Functions
  Referential integrity
  Transformation
  Composition

Correctness
  Informal reasoning
  Formal reasoning

Types
  Static types
  Algebraic types
  Dependent types


*Level two coding exercise*

You might ask a candidate to implement `map`, `reduce`, and `filter` in the language of their choice. Here they are in Haskell.

```
map :: (a -> b) -> [a] -> [b]
map _ [] = []
map f (x:xs) = f x : map f xs

reduce :: (a -> b -> a) -> a -> [b] -> a
reduce f z []     = z
reduce f z (x:xs) = reduce f (f z x) xs

filter :: (a -> Bool) -> [a] -> [a]
filter _pred []    = []
filter pred (x:xs)
  | pred x         = x : filter pred xs
  | otherwise      = filter pred xs
```

## Level three: Underlying theory

Lambda calculus
  What is the difference between strict and lazy evaluation?
  What is the difference between fold left and fold right, and when should you use one vs the other (strict vs lazy evaluation)?

Typed lambda calculus
  Familiarity with lambda cube?
  Can you name some typed lambda calculi?
  Can you explain the differences between typed lambda calculi?

Type theory
  How can you use types to encode business logic (product vs sum types) ?
  What are some interesting advancements in typed languages like rust, idris, haskell...?
  What are some implications to using structural recursion vs general recursion?
  How does proof by induction work?
  Induction vs coInduction?
  What are the different kinds of polymorphism, and what are their pros/cons (expression problem and typeclasses)?
  Can you explain how a type level function works (peano numbers)?
  What are some benefits of type providers?

Category theory
  What are the characteristics of a CRDT
  How/when/why would you use a Functor, Applicative, Monad, Catamorphism, etc...?
  What are the pros and cons to using categories to structure code?





I'd like to share my appreciation for my coworker Michael Whitehead who (as usual) helps me understand the more advanced concepts around functional programming.
