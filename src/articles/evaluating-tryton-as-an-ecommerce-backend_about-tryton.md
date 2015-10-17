---
pagetitle: Tryton as an e-commerce back-end - About Tryton
longtitle: Learning about Tryton, since I might want to use it as an e-commerce back end.
tags: cto
author: Rob Martin
published: 2011-06-05 15:24
snippet: This is part one in a series exploring how Tryton might fair as the heavy-lifting portion of an e-commerce package. This first part describes Tryton - architecture, features, community, license.
---

This is part one in a series exploring how Tryton might fair as the heavy-lifting portion of an e-commerce package. This first part describes Tryton - architecture, features, community, license.

Upcoming parts (as planned, anyway):

-   Part 1: About Tryton
-   [Part 2: Stalking the Tryton community][]
-   [Part 3: The crux of the matter][]

## About Tryton

I want to call Tryton[^tryton] an open source ERP[^erp] system, and it is,
but I like their description of the project better: A
three-tier[^3tier] high-level general purpose application platform
released under the GPL-3[^gpl] license, written in Python[^python], using
PostgreSQL[^postgres] as its database engine.

That’s a lot of descriptors, but basically what it says to me is
that it’s a platform for building stuff, made from tech I like, and
licensed under the GPLv3. And when you look at the base modules
that come with Tryton, you can see it has an emphasis on ERP:
accounting, invoicing, sales management, purchasing management,
inventory management.

*[Note to past self: In the future, you're going to get excited about this stuff. No, not anxious. I said excited.]*

*[Note from past selves: Did you forget your first professional programming project - 1985 - was calculating economic order quantities? And your first industrial automation job - 1991 - counted feet of magnetic wire coming off 50 machines for integration with their business systems? Loser. We're ready. You're the anxious one.]*

### Architecture

So Tryton is made up of three main components *(tiers)*: A client,
a database, and some code stuck in the middle to make things go
smoothly.

-   On the client side, we have a Python GTK+ program that runs on
    a bunch of desktop operating systems (unfortunately not yet
    including mobile.) But there’s lots of ways to look at what the
    client application is. In some ways, my e-commerce websites will be
    the client, too.
-   Opposite the client, we have PostgreSQL, a badass database
    powerhouse. ‘Nuff said.
-   In the middle comes a bunch of Python programming that does all
    sorts of cool stuff. From my perspective, it manages a bunch of
    objects (as in Object Oriented Programming[^oop]) like ‘Orders’ and
    ‘Persons’, and keeps most of them tucked safely away in the
    database for future reference. This is where the magic happens.
    It’s also where the growth happens, because Tryton is modular,
    which means you can create new objects, introduce Tryton to them,
    and wham-bam you get new features. For example, instead of blogging
    about Tryton right now I’m supposed to be building two new modules
    for Tryton’s cousin, OpenERP[^openerp], adding increased functionality
    for interfacing with UPS[^ups] for shipping and CyberSource[^cybersource] for
    payments.

That middle layer between the client and the database is also the
reason Tryton isn’t just an ERP system, because really, you can use
it to manage any data-intensive application. There’s nothing about
Tryton that intrinsically says “You must have an Certified Public
Accountant involved in this project” – Tryton’s design lets it
manage schools and hospitals and music festivals and motorcycles
and people and emails and whatnots just as easily procurement
orders or P&L statements.

While the middle tier provides the magic, there’s an important
consideration in the client, too.
**The client doesn’t have to be human**. If I had my druthers, I’d
no longer develop any web applications that don’t provide an
API, or Application Programming Interface[^api]. Tryton’s server,
known as trytond or “the Tryton daemon”, connects to the regular
old client using a protocol known as XML-RPC[^xmlrpc], or “eXtensible
Markup Language – Remote Procedure Call”. trytond uses XML-RPC to
tell the client what to show, and the client responds in XML-RPC to
tell the server what to do. Well, that means that any program that
knows the secret handshake and how to speak XML-RPC can be a Tryton
client. (For accuracy’s sake, I’d like to point out that Trytond is
like, trilingual. It’s fluent in XML-RPC[^xmlrpcspec], JSON-RPC[^jsonrpc], and
Net-RPC[^netrpc]. It’s also gets by with WebDAV[^webdav], psycopg[^psycopg], and
even some OpenOffice[^openoffice] – you know, enough to ask where the
bathroom is, how to hail a cab, what’s safe to order at a
restaurant.) The upshot of this, of course, is that I can create an
e-commerce site running on MODX[^modx] Revolution[^revolution] or Django[^django]
that interfaces completely with Tryton because
**my website is the client**.

### Features

I feel like I should mention something about what Tryton actually
does, which is an interesting concept. I almost think of it like I
would a programming language – not what it does, but what you can
do with it. Given enough time.

Despite my inclination to see multiple uses for it, Tryton focuses
on business systems. Install the standard modules and it will
handle the business of a catalog retailer, for example:

-   Manage contacts: customers, vendors, companies, employees,
    addresses, etc.
-   Workflow management
-   Issue RFQs (requests for quotation) and purchase orders to
    suppliers, keep track of current and historical costs associated
    with products
-   Receive stock, track inventory by location, move stock around
    and out the door, get the value of inventory by location, set
    orderpoints
-   Process invoices for accounts payable, reconcile the invoices
    against received product, make payments
-   Track leads, schedule meetings and events
-   Create customer quotations, accept purchase orders, schedule
    delivery
-   Issue invoices, accept payments, reconcile accounts
-   Manage projects, including billing for time on projects
-   Review finances, generate reports, close out financial periods
-   Track specialized business intelligence
-   Generate standard and customized reports

There are certainly some things that Tryton doesn’t do, that a
typical ERP system might (or should, or maybe I wish it would) do:

-   Manage production (work orders, repair orders, schedule
    resources, etc.)
-   Comprehensive CRM (track emails, phone calls, social media;
    manage issues or complaints; delegate accounts and tasks, etc.)
-   Better localization support for the United States
-   Support mobile clients

That’s not to say Tryton can’t do these things. It can – some
assembly required, please allow six to eight months for delivery.

Looking at my target application, however – performing as the
backend for a large-scale e-commerce system – Tryton has much of
what I need:

-   Account management
-   Catalog management
-   Stock management and product availability
-   Multiple pricelists and multi-tiered pricelists
-   Sales quotations (often called “shopping carts” and “wish
    lists”)
-   Sales orders (“Complete your order”)
-   Order management
-   Customer support
-   Process integration (“track your order”)

Alas, there are a few things I’d want to add to that list:

-   Online payment support through Authorize.net, PayPal, Google
    Checkout, etc.
-   Shipping integration with UPS, USPS, and FedEx
-   WYSIWYG editing of product data
-   A decent point of sale terminal interface for e-commerce stores
    with a brick-and-mortar presence

While I might not expect it to be part of Tryton, there’s always
the rest of the e-commerce site too – content management, templates,
dynamic content outside of the store, etc. I think it could be
interesting to see a merger between these elements, but I am not
convinced it’s a good marriage. Should an ERP system provide
internet and intranet, online document management, institutional
knowledge management? Sounds like a question for another blog post.
Meanwhile there’s MODx and Django.

### Community

I’ll discuss community more in the next post, but Tryton seems to
be developed under what’s called a Community Open Source model. If
you ask me, that’s the old school way of doing it. You know, the
right way, before the new fangled methods came along and perverted
the process. (I’m not opinionated or anything.)

Tryton is developed by a federation of companies and individual
developers. There seem to be at least five main companies involved,
all of which also provide commercial services for the system as
well. Of course, there is a strong argument that these companies
are most expert in the software. This expertise translates into
demand, and revenue.

In contrast, some open source projects (examples include
OpenERP[^openerp2] and Magento[^magento]) follow what’s called a Commercial
Open Source model. In this model, one company typically calls the
shots (or “edits”) the software. They often do most of the
development, especially early on, but they also draw upon work done
by users and developers of the system. If the editor likes your
code, they pull it into the main branch. If they like your idea but
not your code, they might implement your idea themselves. If they
don’t want either your idea or your code, it sits out there for
others to find and use. Often, the commercial open source model
matures into a dual-release model, where the package is released in
a community (open source) version, and an enterprise (proprietary)
version.

### License

I’ve developed in OpenERP and already had that uncomfortable
discussion with the client where you teach them how to read a
specification, especially the section defining how the code is
licensed. OpenERP is, curiously, licensed under the
GNU Affero General Public License version 3.0[^agpl]. It’s just like
the (in)famous GNU General Public License version 3.0[^gpl2], except
it adds a bit of text closing what’s called the “Application
Service Provider Loophole”. That is, the user of a system licensed
under the AGPL has a right to the source code for the system, even
if they’re accessing the system over a network. Even if it’s been
customized. Even if it’s got trade secrets in it. In practice (and
I Am Not A Lawyer) this seems to mean that the people using the
OpenERP client to connect to an OpenERP server over a network
should be able to retrieve the source code for custom modules.
Generally speaking, this would be the customer who paid a developer
to create the modules, and of course they should get the code.
Likewise, the person who owns a website that connects to an OpenERP
server should be able to get any custom OpenERP module code that
supports the website connecting to it. Phew. But I don’t think it
goes farther than that – I don’t believe this means that the
website needs to be licensed AGPL, or that visitors to the website
should be able to download code for the website, or any custom
OpenERP modules.

Tryton, on the other hand, is licensed under the regular old
GNU General Public License version 3.0, complete with ASP
loophole. That tells me that the source code for any customization
made to the Tryton code (a custom module, for instance) used by a
client over a network does not need that custom code offered to the
client. I don’t have a problem playing nicely with others. I like
to share. I appreciate those subtle shades of difference between
the AGPL and GPL. But when it comes to splitting the hairs of
freedom, it seems that distributing custom code to lowly users
causes palpitations among some clients, typically those with legal
departments.

### What else is there?

-   Part 1: About Tryton. An overview of Tryton – architecture,
    business model, features, license.
-   [Part 2: Stalking the Tryton community][]. There are some
    impressive people working on this project. I’m pleased to get to
    know them.
-   [Part 3: The crux of the matter][]. Tryton needs a web framework so we don't have to do things twice.

*If I’ve inspired a response from you (probably the type of response that deserves an apology), mention [@version2beta][] on [Twitter][] and I’ll see it there. Or, if you can’t comment in less than 126 characters (my handle takes 14 characters with a space), blog about it and tweet that.*



  [Part 2: Stalking the Tryton community]: /articles/evaluating-tryton-as-an-ecommerce-backend_stalking-the-tryton-community "Evaluation Tryton as an e-commerce back-end: Stalking the Tryton community"
  [Part 3: The crux of the matter]: /articles/evaluating-tryton-as-an-ecommerce-backend_web-framework "Tryton as an e-commerce back-end: Tryton needs a web framework."

  [^tryton]: [http://tryton.org/][Tryton] Tryton project home

  [Tryton]: http://tryton.org/ "Tryton home page"

  [^erp]: Don't know what [Enterprise Resource Planning][ERP] is? Wikipedia does.

  [ERP]: http://en.wikipedia.org/wiki/Enterprise_resource_planning "Wikipedia article on enterprise resource planning."

  [^3tier]: Three-tiered architecture structures applications so that the data, business logic, and presentation are separate modules, independently maintained and applied, with all actions passing through the business logic tier. Wikipedia also has an article on [multi-tiered architectures][three-tier].

  [three-tier]: http://en.wikipedia.org/wiki/Three_layer_architecture "Wikipedia article on multi-tier architecture"

  [^gpl]: [The Gnu General Public License version 3.0][GPL-3]. Tryton is licensed under these terms.

  [GPL-3]: http://www.gnu.org/licenses/gpl-3.0.html "The Gnu General Public License version 3.0"

  [^python]: The [Python programming language official website][Python]. Guido van Rossum started development on Python in 1986, and named it in part after Monty Python's Flying Circus.

  [Python]: http://www.python.org/ "The Python programming language official website. Hello, Guido!"

  [^postgres]: Have I mentioned how much I like [PostgreSQL][] before? I really did discount and ignore it before I had to start using it on a project, and that's all it took. I prefer PostgreSQL now over every other SQL database I've used.

  [PostgreSQL]: http://www.postgresql.org/ "Have I mentioned how much I like PostgreSQL before?"

  [^oop]: Wikipedia's article on [object oriented programming][oop] is a good primer. My first class on OOP, back in the early 90's, was interesting. The instructor started to describe an object like a telephone. "It has a phone number associated with it, that's a property. It has the ability to call out, and that's a method. It can also receive incoming calls and ring, and that's an event." Just then, the phone in the back of the room rang. Everyone looked around to see if it was a prop, or a real call, and eventually someone got up and answered it. They listened for a moment and then called out, "Is there a Rob Martin here?" It was my office, sending me to California. I had three hours to pack and get to the airport. I managed to pick up object oriented programming on my own later.

  [oop]: http://en.wikipedia.org/wiki/Object-oriented_programming "Primer on Object-oriented Programming from Wikipedia. Remind me to tell you sometime about my first OOP class."

  [^openerp]: [OpenERP][] and Tryton share a lineage, but don't see eye-to-eye on philosophy. I can relate. That's what my family is like too.

  [OpenERP]: http://openerp.com "OpenERP SA home page"

  [^ups]: UPS, [United Parcel Service][UPS].

  [UPS]: http://ups.com  "United Parcel Service."

  [^cybersource]: [CyberSource][] is like Authorize.net, but for companies with over US$3M a year in sales. Actually the local salesperson might think that number is higher. I brought them a customer with nearly double that, and we gave up on her ever sending a contract after three months.

  [CyberSource]: http://cybersource.com "Cybersource is like Authorize.net, but for grown-up companies."

  [^api]: Wikipedia just knows it all, you know what I mean? Here's the [application programming interface article][API].

  [API]: http://en.wikipedia.org/wiki/Api "Wikipedia article on Application Programming Interfaces"

  [^xmlrpc]: [XML-RPC at Wikipedia][XML-RPC]. I wasn't kidding. Sometimes I think Wikipedia is smarter than Google. At least it's right more often.

  [XML-RPC]: http://en.wikipedia.org/wiki/Xml-rpc "XML-RPC at Wikipedia. I wasn't kidding. Sometimes I think Wikipedia is smarter than Google. At least it's right more often."

  [^xmlrpcspec]: Geeky readers may want to glance at the [spec][xmlrpcspec]. Truly geeky ones already have it memorized. I'm in the former group.

  [xmlrpcspec]: http://www.xmlrpc.com/ "XML-RPC specification"

  [^jsonrpc]: [JSON-RPC][] is like XML-RPC, but quieter.

  [JSON-RPC]: http://en.wikipedia.org/wiki/JSON-RPC "JSON-RPC Wikipedia article."

  [^netrpc]: [Net-RPC][] is XML-RPC that's been pickled in Python.

  [Net-RPC]: http://docs.python.org/library/pickle.html "Python library article about Pickle."

  [^webdav]: [WebDAV][] is HTTP with a bit more Ooomph.

  [WebDAV]: http://en.wikipedia.org/wiki/Webdav "WebDAV is HTTP with a bit more Ooomph."

  [^psycopg]: [Psycopg][] implements a database API in Python. I don't know (yet) how Tryton uses it.

  [psycopg]: http://www.initd.org/psycopg/ "Psycopg implements a database API in Python. I don't know (yet) how Tryton uses it."

  [^openoffice]: See [http://www.libreoffice.org/][OpenOffice].

  [OpenOffice]: http://www.libreoffice.org/ "Libre Office home."

  [^modx]: [MODX][] is a content management framework, easy for the user and powerful for the developer.

  [MODx]: http://modx.com "MODx home page."

  [^revolution]: [MODX Revolution][Revolution] is the "advanced" version of MODX.

  [Revolution]: http://modx.com/revolution/ "Revolution section of the MODX website."

  [^django]: [Django][] is a Python-based web framework for delivering content efficiently. Originally developed by newspaper publisher The World Company in Lawrence, Kansas, it's not used in a wide variety of applications throughout the internet. The largest Django site right now is Disqus, which will host comments for my blog when I get around to implementing that.

  [Django]: https://www.djangoproject.com/ "Django is a Python-based web framework for delivering content efficiently"

  [^openerp2]: OpenERP SA is the editor and holder of the [OpenERP][] project.

  [^magento]: Varien publishes the [Magento e-commerce system][Magento]. That's kind of like the advice Mom gave me. If you can't say anything nice, don't say anything at all.

  [Magento]: http://www.magentocommerce.com/

  [^agpl]: The full and official text of the [GNU Affero General Public License version 3.0][agpl]

  [agpl]: http://www.gnu.org/licenses/agpl.html "Affero General Public License version 3.0."

  [^gpl2]: The full and official text of the [GNU General Public License version 3.0][GPL-3]

  [@version2beta]: http://twitter.com/version2beta "Me, twitterfied"

  [Twitter]: http://twitter.com/ "All of twitter, including me."
