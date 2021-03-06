---
pagetitle: jQuery.multiup plugin for multiple files
longtitle: a jQuery plug-in for selecting multiple files for upload.
tags: dev
author: Rob Martin
published: 2011-08-30 20:21
snippet: I'm a progressive. By this I mean I like things to get progressively more complicated. Don't you? Of course, I don't mean that things should be more complicated than they are &mdash; in fact, I think they should be *at most* only as complicated as they are. But they don't have to start off that complicated; they can get complicated *progressively*.
---

I'm a progressive. By this I mean I like things to get progressively more complicated. Don't you? Of course, I don't mean that things should be more complicated than they are &mdash; in fact, I think they should be *at most* only as complicated as they are. But they don't have to start off that complicated; they can get complicated *progressively*.

One example is file uploads. Sure, some of the time we only need to upload one file, and the way that HTML inputs (type=file) work is okay. But often, we need to upload more than 1 file. Maybe 10 of them. Maybe N of them.

So a progressive solution is to show one file uploader, but give the visitor the option to get another file. And another one. Right up until they've selected as many as you're willing to allow them to upload, or as many as they have.

I did a review on this, and found some options. Malsup[^malsup] has a nice option for Ajaxifying forms, even does an Ajaxian-type thing for file uploads, but it doesn't let you build a package of files to upload. I found some nice stuff from the Stickman[^stickman], but only in a MooTools dialect. Long story short, I wrote a plugin.

I guess that's significant. It is my first jQuery plugin. Feedback welcome, please.

Here is an example of the [jQuery.multiup plugin in action][demo]. [Source code hosted at GitHub][code].

Keep the progressive idea in mind. I hope to write something about progressive authentication systems eventually too.


[^malsup]: [Malsup, of jQuery Cycle fame][malsup].

[malsup]: http://jquery.malsup.com/ "Malsup has written more than one plugin, of course."

[^stickman]: [The Stickman solved this problem][stickman] with plain Javascript back in 2005, then again over the years in MooTools. But not, as far as I saw, in jQuery. So I was inspired to do that. Thank you, Stickman!

[stickman]: http://the-stickman.com/web-development/javascript/upload-multiple-files-with-a-single-file-element/ "This is the original. He has updates over the years too."

[demo]: /static/examples/jquery-multiup-plugin/ "Try the multiup plugin here."

[code]: https://github.com/Version2beta/multiup "jQuery.multiup source code at GitHub."
