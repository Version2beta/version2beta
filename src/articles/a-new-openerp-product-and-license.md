---
pagetitle: A new OpenERP product and license
longtitle: OpenERP announces a new enterprise licence, and their community reacts.
tags: community
author: Rob Martin
published: 2011-06-27 20:03
snippet: Last Friday (June 24, 2011) under an unassuming headline 'Improved OpenERP Website', OpenERP announced the new Enterprise edition of the OpenERP software. The response among community members was swift. Two topics attracted most of the conversation - the new OpenERP AGPL + Private Use license available only to Enterprise edition customers, and apparent policy changes regarding security alerts.
---

Last Friday (June 24, 2011) under an unassuming headline 'Improved OpenERP Website',[^headline] OpenERP announced the new Enterprise edition of the OpenERP software. The response among community members was swift. Two topics attracted most of the conversation: the new OpenERP AGPL + Private Use license[^private-use] available only to Enterprise edition customers, and apparent policy changes regarding security alerts.

## The OpenERP AGPL + Private Use license

Essentially, OpenERP SA has introduced a dual licensing model for
the OpenERP program.

-   Download the community version and the code is strictly
    licensed under the GNU Affero Public License[^affero], which is much
    like the GNU General Public License[^gpl] except that it closes what
    is sometimes called the “Application Service Provider Loophole”.
-   Subscribers of the OpenERP Enterprise Edition receive much the
    same code as the community users, but they are conveyed the right
    to create “private modules”. These modules are meant for companies
    that need to include confidential data and/or business practices in
    their customizations to the program. This second, private license
    grants such users an exception to the AGPL so that they are not
    required to distribute that sensitive code to users of the system,
    but only under very limited circumstances.

I have no doubt this additional license addresses a need or meets a
demand among some users of OpenERP. Certainly I can see how it
might desirable, or even necessary in some applications.
Nonetheless, members of the OpenERP community raised serious
concerns about this announcement.

### The right to license

OpenERP SA owns the rights to a significant portion of the source
code for the OpenERP system. However, portions of the core code for
OpenERP, and the vast majority of the 1,200 modules for OpenERP,
were written by developers who have not handed their rights over to
OpenERP SA. As such, these developers have the right to release
their code as they choose. In fact, they have exercised that right
in releasing their code under the GNU AGPL license, which is why
their modules can be distributed along with the rest of the OpenERP
system.

For clarity I should note that
**all OpenERP modules must be licensed under the AGPL**, as they
are derivative works of OpenERP, which is released under the AGPL
license. (There is an exception for GPL licensed code; more below.)
This isn’t to say that anyone anywhere should have access to the
source code for any custom OpenERP module ever written, but because
OpenERP itself is released
**under the AGPL, the users of any given OpenERP system have the right to the source code for the entire system including the custom modules**.

It is unclear at this point exactly what code OpenERP SA will be
offering under this new dual license. It could be as described
above – only including core code and modules to which OpenERP owns
all the rights. It’s my opinion (and I am not a lawyer) that they
could license a system comprised only of OpenERP SA code under any
license they wish. But some community members fear it will include
work they created, relicensed without their permission.

One basis for this concern is that OpenERP SA code, without modules
and base code contributed by community developers, may be
insufficient for building an effective ERP system. If this is the
case, every Enterprise edition installation will include community
code.

Another basis for this concern might be drawn from the new dual
license itself. In reviewing the text of their OpenERP AGPL +
Private Use license, some of the terms seem to include code created
by the community.

Under section 0, *Additional Definitions*, the license defines
Program to include all components without limitation (emphasis is
mine):

> In the context of this License, the Program refers to OpenERP
> ***including all its components: client programs, server system, modules, etc.***
> “OpenERP modules” are extensions to the Program that can be
> activated separately.

Under section 1, *Exceptions to section 13 of the GNU AGPL*,
describing the conditions required for the exception, the license
implies that OpenERP SA is the original licensor of the program
defined to include all components in section 0 (again, emphasis is
mine):

> \a. You have received written permission to do so
>  ***from the original licensor of the Program, OpenERP S.A.***
>
> \b. You do not convey the covered work.
>

One could read this as OpenERP SA claiming licensing rights to code
written by the community, and several developers in the community
interpreted the announcement in exactly this way.

### Compatible licenses

Under the terms of the dual license, nearly all of the code
distributed to an Enterprise edition subscriber is licensed AGPL.
The subscriber then has the option of creating a derived work (in
the form of a module that extends the functionality of the system)
that is not open source. Under the GPL this is clearly allowed. The
Free Software Foundation has made this clear in the
Frequently Asked Questions about the GNU Licenses:[^gpl-faq] ”The GPL
does not require you to release your modified version, or any part
of it. You are free to make modifications and use them privately,
without ever releasing them.” In fact, OpenERP’s language even
parallels that of the Free Software Foundation in terming the
license “AGPL + Private Use”.

If OpenERP were released under the GPL (as it used to be), private
use of modified source code could cover Application Service
Providers offering the program as a service over a network, and
then the provider would not be required to offer their customers
the source code for the program. OpenERP base code and all modules,
however, are released under the Affero GPL license that plugs the
Application Service Provider loophole. Users of the system, even
those accessing it as an online service, must be prominently
offered the opportunity to download all corresponding source code.

I mentioned briefly above that there is the option to combine
another (possibly non-derivative) work licensed under the GPL with
OpenERP licensed under the AGPL. The terms of the AGPL suggest the
GPL portion of the combined work would be covered under the GPL
license. However, Section 13 of the GPL clearly states that “the
special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to
the combination as such.” So even combined with the explicitly
compatible GPL license, the more restrictive (from the publishers
perspective) requirement to prominently offer source code applies,
even to the GPL code.

### Why it matters

In many cases, an OpenERP installation with base and
community-developed modules will be sufficient all by itself. No
additional modules are needed, let alone custom modules containing
hard-coded sensitive business intelligence. In cases where custom
modules are required, much or all of the sensitive business
intelligence can or should be integrated as data, not program code.
(Pricelists, for instance, are data and under normal circumstances
would never need to be distributed with the source code for a
program.) In the rare circumstances where business methods are
implemented by a module, the source code must be available to the
company that performed (or hired) the modifications, and their
users.

Those final three words, “and their users”, contain the key to
understanding the change. The GPL was created in large part to
protect users by ensuring they have access to the source code of
the programs on which they depend, and some companies would not
wish employees and other system users to have access to the source
code.

The AGPL extends that protection to include another class of users,
those that access the system across a network. In this case, that
will include users who subscribe to OpenERP under a
Software as a Service (SaaS)[^saas] model. Under the AGPL, no company
(including OpenERP SA) could offer OpenERP as a hosted service
without offering links to download their service’s source code,
including custom modules. Under the dual license, only the code
which is distributed (sold or given away to other companies) must
include the option to download source.

SaaS is a powerful and lucrative force in the market. OpenERP SA
itself is promoting their
online service at 39€ per month per user[^openerp-saas]. In the US, a company
of merely twenty employees would be paying $11,760.00 a year for
the service. Under the AGPL, OpenERP SA is required to allow me
(assuming I am an online user) to download the source code,
including the source code for any modules they’ve written
exclusively for their online service, which I may then use to
create a competing service. Under the dual license, for some amount
of money starting at 1,950€ per year, I can create a custom module
for SaaS and not offer the source code to my users. Or, if I’m
OpenERP, perhaps I can just do it for free.

### Community Relations

In the two years I’ve been working with OpenERP, I’ve watched
OpenERP SA sink in the estimation of many community members and
developers. The release of the Enterprise edition with a dual
license may have created a new low.

<a href="http://twitter.com/#!/fpopenerp/status/73712952632545280" title="Click the image to view Fabien Pinckaers' tweet at Twitter.com" target="_blank">
  <img src="/static/2011/openerp-no-dual-license-tweet-may-26-2011.png" alt="Fabien's No Dual License tweet" />
</a>

(**Update 23 August 2011:** This tweet has been removed from Fabien Pinckaer's Twitter account, so if you click on the image, you'll see a Twitter 404 page.)

I first heard of the dual license possibility from the transcript
of a Certified Training Partner (CTP) meeting held on IRC in May.
(I am not a CTP, but a link to the transcript was provided by an
attendee.) Some partners in the meeting expressed considerable
opposition to the idea at that time, and Fabien Pinckaers made what
many would consider an unequivocable statement on May 26th that
there would be no dual-license. Nonetheless, the June 24
announcement indicates Enterprise subscribers will have access to
the new dual license.

It could be argued that Fabien’s tweet has not been violated:

-   The new license is a modified AGPL, granting additional
    permissions in limited circumstances.
-   Only undistributed custom modules qualify for the private use
    license. For the rest of the software, the license is modified from
    AGPL only enough to allow for those private modules to be installed
    with the system.
-   Fabien didn’t *actually* say they wouldn’t dual license, only
    that they didn’t have to. (Okay, this one feels like a stretch.)

I haven’t heard these arguments presented by anyone in the
community, but my impression is they are not reassuring. My own
employer tweeted last Friday:

<a href="http://twitter.com/#!/lageekitude/status/84306783111352320" title="Click the image to view @LaGeekitude's tweet at Twitter.com" target="_blank">
  <img src="/static/2011/openerp-tryton-house-tweet-jun-242.png" alt="Ditching OpenERP for Tryton?" />
</a>

## Security Alerts

On the OpenERP ‘Buy’ page[^catalog] showing the options for purchase and
download, the presence of ‘Security Alerts’ under OpenERP
Enterprise, and only under Enterprise, attracted conversation.

[@SharoonThomas][]:

> Acc to [@openerp][] community users will not get security alerts.
> Not needed since community has always found security holes, not
> openerp SA

[@SharoonThomas][1]:

> [@openerp][] how dare u talk about security alerts when u dont know
> why software needs encrypted passwords & not plain text??
> [http://j.mp/lffPGi][]

[@LaGeekitude][]:

> Security alerts should be public announcements. All users deserve
> notice. [@OpenERP][] [@fpopenerp][]

Upon closer review, it’s apparent that OpenERP only promises that
Enterprise customers will receive notices in advance of a public
disclosure. This is detailed on the multiple product pages
describing OpenERP Enterprise, such as
the page describing the 70 to 150 user license[^150users] (emphasis is
mine):

> If we detect a security issue on OpenERP
> ***we develop the patch and warn our customers three weeks before a public announcement***.
> We also provide you with the explanation on how to migrate or apply
> the security patch. After three weeks, we do a public communication
> about the security hole for the rest of the community. We strongly
> advice you to apply the patch to your server within these three
> weeks to avoid any security trouble.

Under the OpenERP Publisher’s Warranty, the promise regarding
security alerts was even less favorable to community users (again,
emphasis is mine):

> As OpenERP manages critical data for your company, it is important
> to be very proactive in case of a vulne­rability issue detection in
> the OpenERP software. Once a security bug is detected by OpenERP sa
> or by the community,
> ***we provide you with a patch to fix the issue one month before the public announce of the security fix***.
> This allows you to update your installation before the public
> announce and release of the patch.

Since the new Enterprise offerings replace the OpenERP Publisher’s
Warranty, it seems likely that the Enterprise policy on security
alerts will become the current practice. In effect, this is an
improvement over the previous practice.

## OpenERP SA and the commercial open source business model

I can certainly relate to the community of developers who are
concerned and frustrated by OpenERP SA’s announcement. Some of the
developers have devoted literally months of their time to make
OpenERP a better product, and have reason to feel used, even
abused, by liberties that may be (or have been) taken with their
hard work. Because of this, I’ve tried to discuss the situation
objectively, and I hope I’ve demonstrated that the situation is not
quite as bad as it seemed at first. There are unanswered questions,
and I trust OpenERP SA will answer those through further
communication and their future actions.

It is important to consider that OpenERP SA is working to cement
their commercial open source business model. We know what to
expect: a difficult transition, especially for early adopters and
contributors as more of the product is brought under the company’s
control. They are master editor of the software, selling services
to end users as well as companies offering services related to
their software. With persistence and planning, OpenERP SA and many
of their partners will enjoy a profitable future.

One freedom often ascribed to the GPL is the freedom to not use the
software. Don’t like the fact you have to release your source code?
Don’t use it. Don’t like the direction the project is going? Fork
it.

**Please don’t hesitate to do your own investigation about the new OpenERP products and licenses.**
Visit their website[^openerp], especially their FAQ on the changes[^openerp-faq]
and community section[^community] for information on all of their
communication channels.

### In related news…

Nicolas Évrard of B2CK[^b2ck] posted to the Tryton mailing list[^groups-general]
last Saturday a
call for comments on the creation of the Tryton Software Foundation[^foundation].
B2CK proposes this foundation as a consensus-based community formed
to promote and protect the freedom of Tryton. As Tryton and OpenERP
share a common lineage (both can be traced back to TinyERP, each
with improvements in different areas), OpenERP users and
contributors frustrated by OpenERP’s business model may find a more
favorable environment among Tryton’s community open source model.

I have been writing a series of articles on Tryton on this blog; consult
them or visit Tryton’s website[^tryton.org] for more information.

### *Updated 28 June 2011*

There has been remarkable conversation on Twitter regarding this
post, and I’m grateful for all the feedback. I’d especially like to
thank Olivier Dony ([@odony][] on Twitter), Community Manager at
OpenERP SA, for his clarifications on some of the points I’ve
raised.

The biggest comes from this tweet, which [@ravlyi][] described as
“the missing OpenERP re-licensing FAQ”:

<a href="http://twitter.com/#!/odony/status/85706734865367040" title="Click the image to view Olivier Dony's tweet at Twitter.com" target="_blank">
  <img src="/static/2011/openerp-relicensing-faq-tweet-from-odony.png" alt="Olivier Dony's Not Compatible tweet" />
</a>

This certainly seems to make clear that no Enterprise edition
customer using private modules may install any AGPL-only modules.
It doesn’t answer concerns about what happens if an Enterprise
edition subscriber installs a community module, or about community
contributions to OpenERP core code, such as the netsvc.py[^netsvc] file
[@cedrickrier][] tweeted from OpenERP-server trunk, as excerpted
here:

	…
	5 \# OpenERP, Open Source Management Solution
	6 \# Copyright (C) 2004-2009 Tiny SPRL (). All Rights Reserved
	7 \# The refactoring about the OpenSSL support come from Tryton
	8 \# Copyright (C) 2007-2009 Cédric Krier.
	9 \# Copyright (C) 2007-2009 Bertrand Chenal.
	10 \# Copyright (C) 2008 B2CK SPRL.
	…

Also, one aspect I did not address in the original post was
OpenERP’s original transition from GPL to AGPL.
Fabien Pinckaers discussed it on his Blogspot blog[^fpblog] and
reviewing this clears any question about his thoughts at that time
on SaaS and OpenERP:

> “Our goal is to better promote and maintain the free and open
> source nature of OpenERP. We think this licence will better protect
> the community to ‘evil’ SaaS offers that do not want to release
> their source code to the community.”

It’s my opinion (and again, I am not a lawyer) that the new
AGPL+Private enables the ‘evil SaaS offers’ Fabien warns about, so
long as the SaaS provider is either a paying OpenERP Enterprise
subscriber, or OpenERP SA themselves.
**I am in no way saying it is OpenERP SA’s intention to support a secondary SaaS market based on private modules, or to create private modules for their own SaaS product.**
I merely point at the license and say I think it could be done
under these terms.

### *Updated 23 August 2011*

I was doing maintenance on this post (moving it to the version2beta.com domain with the rest of my blog) and came across some discrepencies between linked documents when I wrote the post, and how those documents appear today. For example, the netsvc.py[^netsvc] discussion above: Cédric Krier's copyright no longer appears in the header in the trunk source code. I researched the revision and found this:[^revision]

	Committer: Olivier Dony
	Date: 2011-06-29 09:51:38
	Revision ID: odo@openerp.com-20110629095138-hmo91mvk1m8u4643
	[FIX] netsvc: corrected copyright header

	Corrected license to AGPLv3, and removed obsolete copyright lines
	as confirmed by Cedric Krier by email on 2011-06-29.
	These copyright lines referred to a refactoring copied from Tryton
	in revision rev 1439 - stephane@tinyerp.com-20081218235433-cnsc5a4iyfzqvbdx
	All this code has disappeared since then, specifically after
	a major rewrite by xrg, merged at revision 1900
	(mga@tinyerp.com-20091126113653-0ym60nvtjinvp82h).

This was reassuring, that the copyright notice was in error. I believe it is better that my research into the issue exposed an oversight rather than a disagreement over who owns the code. According to Oliver Dony's forum post two weeks later, all such issues are resolved:[^forum]

> …

> OpenERP SA does own the copyright to the server, clients, and all modules whose author is OpenERP/Tiny. And we are exclusively offering the AGPL+PrivateUse option for those pieces of code, and nothing else. If someone believes they own copyright on a contribution within that specific set of source code lines, and are against the AGPL+PrivateUse license, they can contact us, and we'll find a solution. We've only seen one such claim so far (from C.Krier), and it was about code that was long gone from our source, so there was no problem. So if you are such a person, please contact us.

> …

Again, this claim is reassuring. However, I understand these are not the only items in question or the only copyright that has been contested. Here are three more sections of code with conflicted copyright.

In the OpenERP client, widget/view/list.py:[^view-list]

	…
	4 #    OpenERP, Open Source Management Solution
	5 #    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>). All Rights Reserved
	6 #    Copyright (c) 2008-2009 B2CK, Bertrand Chenal, Cedric Krier (D&D in lists)
	…

In the OpenERP base_vat module:[^base-vat]

	…
	4 #    OpenERP, Open Source Management Solution
	5 #    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>). All Rights Reserved
	6 #    Copyright (C) 2008-2009 B2CK, Cedric Krier, Bertrand Chenal (the methods "check_vat_[a-z]{2}"
	…

And in the webdav module:[^webdav]

	…
	4 #    OpenERP, Open Source Management Solution
	5 #    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
	6 #    Copyright (c) 1999 Christian Scholz (ruebe@aachen.heimat.de)
	…

Without a complete audit of the source code, all such copyright discrepencies may not be recognized, and it would seem to me that such an audit should occur before the product is relicensed.

**One last note:** Several people have raised the question whether modules in OpenERP (or, in two cases, themes in Wordpress - a similar but not identical question) are in fact derivative works that must be licensed AGPL. This is a big question, of course, and deserves more than merely a mention in an addendum to a months-old blog post. Here I'd like to point out that I make the statement in my original post that modules must be licensed AGPL, and that this statement is debatable. I hope to question that statement in a future blog post.

*If I’ve inspired a response from you (probably the type of response that deserves an apology), mention [@version2beta][] on [Twitter][] and I’ll see it there. Or, if you can’t comment in less than 126 characters (my handle takes 14 characters with a space), blog about it and tweet that.*

[^headline]: I found the headline to be a little disengenuous. I'm not sure why they decided to launch a significant new product (OpenERP Enterprise) under the headline '[Improved OpenERP Website][headline]'. Nonetheless, they got a lot of attention.

[headline]: http://www.openerp.com/node/836 "OpenERP post about the updates to their website, including a world map of partners and a significant upset to their marketing strategy"

[^private-use]: The [new OpenERP license][private-use], described as a GNU Affero GPL plus more permissive exceptions available under limited circumstances.

[private-use]: http://www.openerp.com/legal "The new OpenERP license."

[^affero]: Read the Free Software Foundation's text of the [Affero General Public License][affero], version 3. It's not long, and it's not full of legalese. It's really pretty accessible.

[affero]: http://www.gnu.org/licenses/agpl.html "The GNU Affero General Public License."

[^gpl]: Read the Free Software Foundation's text of the GNU General Public License, version 3. Really, this stuff is important. How much software do you use that is licensed under the GPL? Have you published under the GPL?

[gpl]: http://www.gnu.org/licenses/gpl.html "The GNU General Public License, version 3"

[^gpl-faq]: The GNU FAQ is useful in understanding the intent of the licenses, too. Read [this answer][gpl-faq] on distributed source code for modified versions that are not publicly redistributed.

[gpl-faq]: http://www.gnu.org/licenses/gpl-faq.html#GPLRequireSourcePostedPublic "The GNU FAQ on distributed source code for modified versions that are not publicly distributed"

[^saas]: Here is the [Wikipedia article about Software as a Service][saas], AKA On-demand software or cloud-based services.

[saas]: http://en.wikipedia.org/wiki/Software_as_a_service "Wikipedia article about Software as a Service, AKA On-demand software or cloud-based services."

[^openerp-saas]: OpenERP offers a SaaS version of their software already. It's in their catalog and costs 39€ per user per month, or if you're in the US, USD$49 per user per month.

[openerp-saas]: http://www.openerp.com/catalog "OpenERP's overview of products, including their online service"
[^catalog]: Again, here is [OpenERP's catalog page][catalog].

[catalog]: http://www.openerp.com/catalog "Three options of OpenERP, and what's not included in the less expensive versions"

[@openerp]: http://twitter.com/openerp

[@SharoonThomas]: http://twitter.com/#!/sharoonthomas/status/84269468506800128 "A Twitter comment by @SharoonThomas"

[1]: http://twitter.com/#!/sharoonthomas/status/84269785071882240 "A follow-up comment by @sharoonthomas"

[http://j.mp/lffPGi]: http://j.mp/lffPGi

[@OpenERP]: http://twitter.com/OpenERP

[@fpopenerp]: http://twitter.com/fpopenerp

[@LaGeekitude]: http://twitter.com/#!/lageekitude/status/84279132279672832 "A Twitter comment by @lageekitude"

[^150users]: Here is the page at OpenERP.com describing what's included with [OpenERP's 15,500€ license package][150users].

[150users]: http://www.openerp.com/node/819 "The page describing what's included with OpenERP's 15,500€ license package"

[^openerp]: [http://www.openerp.com][openerp]: OpenERP SA's website.

[openerp]: http://www.openerp.com "The home page for OpenERP SA"

[^openerp-faq]: [http://www.openerp.com/services/faq-onsite][openerp-faq]: "OpenERP Enterprise and OpenERP Community, Modules and Licensing, Bug fixing, Support and Migrations FAQ"

[openerp-faq]: http://www.openerp.com/services/faq-onsite "OpenERP Enterprise and OpenERP Community, Modules and Licensing, Bug fixing, Support and Migrations FAQ"

[^community]: [http://www.openerp.com/community][community]: OpenERP offers a wide variety of ways to stay connected and join the conversation.

[community]: http://www.openerp.com/community "The OpenERP community section"

[^b2ck]: [http://www.b2ck.com/][b2ck] I've described B2CK as the main driving force behind Tryton. They are certainly a substantial contributor.

[b2ck]: http://www.b2ck.com/ "B2CK SPRL"

[^groups-general]: Tryton has an [English-language Google Groups email discussion list][groups-general]. There are [other language lists][groups-other] available too.

[groups-general]: http://groups.google.com/group/tryton/ "The Tryton Google group discussion list"

[groups-other]: http://www.tryton.org/community.html "The Tryton community page lists Google Groups in other languages."

[^foundation]: Read the [discussion around the creation of the Tryton Software Foundation][foundation] on the Tryton discussion list.

[foundation]: http://groups.google.com/group/tryton/browse_thread/thread/7eda95e01ddd8b3c "Discussion around the creation of the Tryton Software Foundation."

[^tryton.org]: [http://tryton.org][tryton.org]: Tryton home page

[tryton.org]: http://tryton.org "Tryton home page."

[@odony]: http://twitter.com/#!/odony "Olivier Dony on Twitter"

[@ravlyi]: http://twitter.com/#!/rvalyi "Raphaël Valyi on Twitter"

[^netsvc]: Originally this footnote linked to this [source code for netsvc.py][netsvc1], but I have since visited the link and the copyright notice was changed. The [revision note][netsvc2] explains why.

[netsvc1]: http://bazaar.launchpad.net/~openerp/openobject-server/trunk/view/head:/openerp/netsvc.py#L8 "Source code for netsvc.py file in the OpenERP core"

[^revision]: [Olivier Dony's revision note][netsvc2] for openerp/netsvc.py.

[netsvc2]: http://bazaar.launchpad.net/~openerp/openobject-server/trunk/revision/3485 "Revision 3485 to netsvc.py copyright header"

[^forum]: [Olivier Dony's forum posa][forum]t regarding the new license, making clear that OpenERP SA's position is they exclusively own copyright to OpenERP server and client, and all modules whose author is OpenERP or Tiny.

[forum]: http://www.openerp.com/forum/topic26369-30.html#p87266 "OpenERP forum post re: Licensing Community Modules for Private Use."

[@cedrickrier]: http://twitter.com/#!/cedrickrier "Cédric Krier on Twitter"

[^fpblog]: [Fabien Pinckaers' post 15 October 2009 regarding OpenERP's licensing change from GPL to AGPL.][fpblog]

[fpblog]: http://fptiny.blogspot.com/2009/10/openerp-and-agpl.html "Fabien Pinckaers' Blogspot blog post"

[^view-list]:

[http://bazaar.launchpad.net/~openerp/openobject-client/trunk/view/head:/bin/widget/view/list.py#L6](http://bazaar.launchpad.net/~openerp/openobject-client/trunk/view/head:/bin/widget/view/list.py#L6)

[^base-vat]:

[http://bazaar.launchpad.net/~openerp/openobject-addons/trunk/view/head:/base_vat/base_vat.py#L6](http://bazaar.launchpad.net/~openerp/openobject-addons/trunk/view/head:/base_vat/base_vat.py#L6)

[^webdav]:

[http://bazaar.launchpad.net/~openerp/openobject-addons/trunk/view/head:/document_webdav/webdav.py#L6](http://bazaar.launchpad.net/~openerp/openobject-addons/trunk/view/head:/document_webdav/webdav.py#L6)

[@version2beta]: http://twitter.com/version2beta "Me, twitterfied"

[Twitter]: http://twitter.com/ "All of twitter, including me."
