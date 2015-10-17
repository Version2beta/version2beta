---
pagetitle: Don't comment your code
longtitle: Feel inclined to write a comment? Do this instead.
author: Rob Martin
tags: dev
published: 2013-05-15 08:30
snippet: Comments lie. Instead of writing comments, write specs and functions. This post talks about why and how to do this.
---

**Comments lie.**

My favorite example of this was described in the Ruby Rogues podcast, episode 79.[^rr79] I believe it went something like this:

```
five = 7; # 12
```

This comment is funny, but most comment-based lies are much more sinister. They hide, waiting patiently to spring out and bite the next programmer in the ass. Sure the comments were written in good faith, and they probably documented the system accurately when the comment was written. But code changes, often before we even get out of our chairs, and there are few systems guaranteeing that we keep inline documentation consistent with the code base as it changes.

We can make a commitment to avoiding comments that lie. One of the guiding principles of Python is that computers don't care how the code is written (and whenever I read that, I think of obfuscated Perl). Future programmers working on the code base do care how the program is written, because they have to read it. We have an obligation to that future programmer to make our code obvious.

As it says in the Zen of Python,[^zen] "Readability counts."

It also says, "If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea."

It also says, "Simple is better than complex."

Let's take those aphorisms and apply them to our commitment about avoiding comments that lie. So now I want to change what I said above. Instead of "Avoid comments that lie", let's try "**Avoid comments.**"

This is a guiding principal, not a carved-in-stone law. Try to write code that doesn't contain inline comments.

Here are two ways to do that.

## Write a test instead

When you find yourself wanting to write a comment, write a test instead. Not just a test, but a spec. Tests don't lie - they either pass or they fail. If you write it as a spec, any future developer on your project (including you in six months - or maybe just after lunch) can view the test and see exactly what the code is supposed to do. Even better, you can see whether or not the code and the spec are still in sync with each other.

Here's a function written in Python. I'm not going to tell you what it does, and it doesn't have any comments.

```
def matcher(i):
    group = {}
    for element in i:
        sorted_el = ''.join(sorted(list(element)))
        if group.get(sorted_el):
            group[sorted_el].append(element)
        else:
            group[sorted_el] = [element]
            group[sorted_el].sort()
    return sorted([v for k,v in group.iteritems()])
```

Since this is a public function written in Python, it should actually have a docstring.[^pep257] I'd give it one like this:

```
def matcher(i):
    """Group items that have the same letters."""
    ...
```

Docstrings can lie just as easily as any other comment, and we want to document this code in a way that proves both the code and the comment are correct (or at least both wrong in the same way.)[^doctests]

I learned Test Driven Development and Behavior Driven Development using Ruby and RSpec,[^rspec] so in Python I tend toward tests written using Nose[^nose] and Expecter[^expecter]. Here's my test for this function:

```
class TestMatcher(unittest.TestCase):
    def test_that_strings_are_grouped_by_component_letters(self):
        expect(
            matcher(['abc', 'def', 'aca', 'acb', 'fed', 'edf', 'c'])) == \
              [['abc', 'acb'], ['aca'], ['c'], ['def', 'edf', 'fed']]
```

So now my code has an example, and the beauty of it is that this is a specification can be proven, over and over again. This test tells me what kind of result to expect, and lets me demonstrate that the code actually achieves that result any time I wish.

One disadvantage of the "write a test instead" option is that the documentation (specification, really) is not in the same place as the code. It may not be in the same file or even the same directory. This can make it difficult to find. So here's an alternative to writing a comment that puts the appropriate documentation in the code at exactly the place you wanted to put the comment. Bonus, it complements the "write a test instead" directive.

## Write a function instead

Write a function instead, and name your function for whatever you were going to put in your comment.

Here's an example, this time in Ruby. (Caveat: I'm still learning Ruby, so try not to laugh if I'm Doing It Wrong. Actually, laugh if you want, but please leave me a comment with advice.)

```
class Matcher

  def initialize
    @my_hash = Hash.new
  end

  def make_hash(list)
    list.each do |e|
      # Add the list element to my hash keyed to
      # the element's component letters, sorted
      key = e.split(//).sort().join()
      if @my_hash.has_key?(key)
        @my_hash[key] << e
      else
        @my_hash[key] = [e]
      end
    end
    return @my_hash
  end

end
```

See that comment in the middle? It explains what the next six lines of code do, the six lines of code that are making my method long and ugly. Let's refactor that comment into a method.

```
class Matcher

  def initialize
    @my_hash = Hash.new
  end

  def add_to_hash(a_hash, key, e)
    if a_hash.has_key?(key)
      a_hash[key] << e
    else
      a_hash[key] = [e]
    end
  end

  def make_hash(list)
    list.select{ |e| add_to_hash(@my_hash, e.split(//).sort().join(), e) }
    return @my_hash
  end

end
```

So now instead of the comment that described what the code was doing when I wrote the class, we defined a new method. Plus, the new method can be tested separately.

We still have a bit of code in the middle of the list.select block that looks obscure and a little confusing. Maybe I feel inclined to comment that, too. Let's make another method instead.

```
class Matcher

  def initialize
    @my_hash = Hash.new
  end

  def add_to_hash(a_hash, key, e)
    if a_hash.has_key?(key)
      a_hash[key] << e
    else
      a_hash[key] = [e]
    end
  end

  def sort_letters(a_string)
    return a_string.split(//).sort().join()
  end

  def make_hash(list)
    list.select{ |e| add_to_hash(@my_hash, sort_letters(e), e) }
    return @my_hash
  end

end
```

As I described above, this works in conjunction with tests, so as I'm refactoring my code-in-need-of-comments, I'm also running my tests to make sure that the code meets the spec all along. Here is a test for this code that meets the requirements above, specifying what the code is expected to do and giving an example.

```
test_data = ['abc', 'def', 'aca', 'acb', 'fed', 'edf', 'c']

hash_data = {
  'abc' => [ 'abc', 'acb' ],
  'def' => [ 'def', 'fed', 'edf' ],
  'aac' => [ 'aca' ] ,
  'c' => [ 'c' ]
}

describe Matcher do
  it "creates a hash that groups strings by component letters" do
    matcher = Matcher.new
    expect(matcher.make_hash test_data).to eq hash_data
  end
end
```

## Stop commenting your code

I've written tens of thousands of inline comments in the last 30 years. I can absolutely promise you that most of them are useless. They are all written from good intentions. Many of them inject humor, or at least personality. Quite a few of them were written to demonstrate how clever I am. Some of them might even help the poor sod who is now stuck maintaining that code understand what I was trying to do. The majority of them are probably no longer consistent with the operation of the program.

My motivations demonstrate why comments are often bad. My personality and attempts at being funny have little to do with shipping code. My clever programming was rarely an asset, and usually just made my code less understandable. And comments that no longer document the code as it stands now do nothing to enlighten the current maintainer. They confuse the issue.

I've been on the other side too, stuck with a code base that may have hundreds of lines of inline comments that made sense to someone at some point, but are useless to me now. Often I want to start from scratch rather than wallow through someone else's wall of text figuring out what's true and what's not.

Using these directives, my code is cleaner. It's not perfect, and I'm still learning, but at least the person who has to read it has a fighting chance.

Give it a try. Stop commenting your code, and see if it doesn't make you a better programmer.



[^rr79]: [Ruby Rogues][rubyrogues] is a podcast about Ruby, as you may have guessed, but I started listening to it more than a year before I considered myself a Ruby programmer. The Rogues have consistently been one of my best sources for learning to be a better programmer, regardless of language. It's fair to say I've been writing this blog post in my head ever since I listened to episode 79, [Documenting Code][rrdc].

[rubyrogues]: http://rubyrogues.com/ "Ruby Rogues podcast"

[rrdc]: http://rubyrogues.com/079-rr-documenting-code/ "Ruby Rogues episode 79, Documenting Code"

[^zen]: [The Zen of Python][zen] are 20 aphorisms about coding in Python, and coding in general. They are Python's guiding principles. Also called PEP 20.

[zen]: http://www.python.org/dev/peps/pep-0020/ "The Zen of Python"

[^pep257]: [PEP 257 Docstring Conventions][pep257] documents the semantics of docstrings. According to [PEP 8, the style guide for Python][pep8], all public modules, functions, classes, and methods should have a docstring that define the purpose of the code block.

[pep257]: http://www.python.org/dev/peps/pep-0257/ "PEP 257 Docstring Conventions"

[pep8]: http://www.python.org/dev/peps/pep-0008/ "PEP 8 Style Guide for Python"

[^doctests]: I don't cover doctests here, but the Python standard library does include a way to write docstrings that prove the code works. They're called [Doctests][doctests].

[doctests]: http://docs.python.org/2/library/doctest.html "The Python Doctest library"

[^rspec]: [RSpec][rspec] is a Ruby testing tool for Behavior Driven Development.

[rspec]: http://rspec.info/ "RSpec documentation"

[^nose]: [Nose is a testing framework][nose] that extend's Python's unittest to make testing in Python nicer.

[nose]: https://nose.readthedocs.org/en/latest/ "Nose documentation at ReadTheDocs.org"

[^expecter]: [Expecter is an assertion library][expecter] written by Gary Bernhardt that helps you write assertions that describe expected behavior. I came across this library quite directly. When I started using test driven development in Python, all I knew was RSpec and I wanted to write expect-style assertions in Python. [Gary Bernhardt][garybernhardt] was the best person I knew at the intersection of Ruby, Python, and testing, so I tweeted at him and asked for his advice. He directed me to this library.

[expecter]: https://github.com/garybernhardt/expecter "Gary Bernhardt's Expecter assertion library"

[garybernhardt]: https://twitter.com/garybernhardt "Gary Bernhardt on Twitter"
