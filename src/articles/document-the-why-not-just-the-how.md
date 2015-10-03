---
pagetitle: A Response to Tom Henrich's Document The Why
longtitle: An example of documenting why code was written the way it was.
author: Rob Martin
published: 2012-03-26 10:15
snippet: >
  On his blog, Tom Henrich calls for better developer documentation on <em>why</em> a design decision was made, rather than just <em>what</em> decision was made. In this post I share my example.
---

On his blog, Tom Henrich[^th] calls for better developer documentation[^why] on *why* a design decision was made, rather than just *what* decision was made. In this post I share my example.

From the source code for a Box.net[^box.net] uploader snippet I wrote in MODX:[^modx]

```php
/*
 * @name      Down and Dirty Box.net Uploader
 * @author    Rob Martin <rob@qmuxs.com>
 * @copyright (c) 2011 Quintessential Mischief LLC
 * @link      http://www.qmuxs.com
 * @license   GPLv3
 * @version   0.1.0
 *
 * The need for a down & dirty uploader came about after reviewing the
 * box.net PHP library code at https://github.com/boxplatform/box-php.
 * It's just not very good, and some of it is totally borked. It's not
 * even a surprise - I found comments on blog posts dated from February
 * 2008 complaining about a bug (can you call a whole missing function
 * - promised in the docs - a bug?) that has not changed in over three
 * years.
 *
 * I was about to start over. :-( But I did get in touch with Sean ****
 * at Box.net who threw some salt on the open wounds. He let me know
 * that the new PHP library is **just days from release**.
 *
 * And no, he couldn't get it for me. So sorry.
 *
 * The Python code isn't much better, though I haven't read through it
 * as much. However, documentation such as:
 *
 * > """Exception class for errors received from Facebook."""
 *
 * makes me think it might not be. Facebook has nothing to do with this
 * code.
 *
 * **NOTE**: Just so you know, this code doesn't do any of the
 * authentication work. You've gotta do that manually. You need an API key,
 * an auth_token, and a folder ID for where you want the files to land.
 *
 * Here's how:
 *
 * 1. Get a ticket. It'll come back as <ticket>...</ticket>.
 * https://www.box.net/api/1.0/rest?action=get_ticket&api_key={YOUR_API_KEY}
 *
 * 2. Using the ticket, log in.
 * https://www.box.net/api/1.0/auth/{YOUR_TICKET}
 *
 * 3. Request the auth_token. It'll come back as <auth_token>...</auth_token>.
 * https://www.box.net/api/1.0/rest?action=get_auth_token&api_key={YOUR_API_KEY}&ticket={YOUR_TICKET}
 *
 * 4. Get the ID of the folder you want. It'll look like <folder id="xxx" name="this-one".../>
 * https://www.box.net/api/1.0/rest?action=get_account_tree&api_key={YOUR_API_KEY}&auth_token={YOUR_AUTH_TOKEN}&folder_id=0&params[]=nozip
 *
 * So that's the story. Here's the code:
 */
```


[^th]: Tom Henrich ([@tomhenrich][thtw]) is a Milwaukee web geek & caffeine fiend. [Tom's blog][blog].

[thtw]: http://www.twitter.com/#!/tomhenrich "Tom Henrich on Twitter"

[blog]: http://notes.tomhenrich.com/ "Tom Henrich's blog"

[^why]: Tom's post, [Document the Why, not just the How][post].

[post]: http://notes.tomhenrich.com/2012/03/document-the-why-not-just-the-how/ "Document the Why, not just the How"

[^box.net]: [Box.net][] is pretty good at secure cloud storage, and pretty bad at APIs - in my experience anyway.

[Box.net]: http://www.box.net "Those people who do secure cloud storage."

[^modx]: [MODX][] is a PHP-based content management framework that works well for developers, designers, and content managers.

[MODX]: http://www.modx.com "MODX content management framework"
