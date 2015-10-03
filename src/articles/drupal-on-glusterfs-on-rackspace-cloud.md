---
pagetitle: Drupal, on GlusterFS, on Rackspace Cloud
longtitle: I ran Drupal on GlusterFS for a few days. I didn't like it. Here's why.
author: Rob Martin
published: 2011-11-28 16:12
snippet: I ran Drupal on GlusterFS for a few days. I didn't like it. Here's why.
---

I ran Drupal on GlusterFS for a few days. I didn't like it. Here's why.

I'm building an eight-node server cluster on Rackspace Cloud for a Drupal site. Clearly, I want it to go fast.

It is a busy site, peaking at 20,000 unique visitors a day, maybe 100,000 pageviews. But the real fun part is that it has 1.6 million users.

Putting it on Drupal is a decision that predates me (and I withhold judgement - I don't have nearly enough Drupal experience yet), but the rest of the structure has been up to me. I have specific goals, like 1.5 second response times even for users who are logged in.

My architecture goes like this:

* Two load balancers, running nginx. Nginx is also serving all static content and boost cache from Drupal. Upstream servers are selected by ip_hash.

* Two application servers upstream of nginx run lighttpd and fastcgi. Hello, Drupal.

* A dual-master pair of MySQL servers back up the application servers. I wanted to run PostgreSQL, and I was really happy when I remembered that Drupal works with PostgreSQL. But Drupal only works with Postgres for some values of the word "works". Modules may or may not support it. CCK has some issues too.

* Two MongoDB servers hold up the rear and contain user-specific information for all 1.6 million users. A custom Python program manages authentication and data interface.

Originally, I intended to use DR:BD[^drbd] much like I do with my high-availability Linode virtual private servers.[^linode-ha] It turns out that you can do that on Rackspace a couple different ways, neither of which are recommended. The first requires you to make a loopback device, since it's really difficult to get more than one block-level device on a Rackspace cloud server. The second requires you to get more than one block-level device on a Rackspace cloud server, which is not (as you might guess) only really difficult to accomplish, but it can also break things like backups and snapshots.

So bzzzzt to DR:BD, this time.

Next, I tried GlusterFS.[^gluster] The docs sucked[^docs]. At least I think they would have sucked if I'd read them, nearly all of them, because that's how far you have to get into them before you can see what really needs to be done. In part, this highlights the absence of a useful quickstart guide. But there's this sad thing, too. Once you manage to infer the organization of the configuration, it's really rather elegant. You could think of it as a string of Unix pipes, each volume handing off to the next, but I picture it like a stack of matryoshka dolls. This volume (the littlest doll) provides a POSIX device. This volume (the next littlest doll) provides locks. The next volume (we're getting bigger now) provides multiple I/O threads. And so on.

When all the dolls were stacked, I had a working GlusterFS filesystem across four servers.

Since I'm not the only person on this project (which is a good thing, or else we'd really be in trouble) we also had a development server at WebEnabled.[^we] I compared the Drupal devel module timing between the two systems and realized that I had a serious problem. What WebEnabled was doing in 1,200ms, my setup was taking 4,200ms.

Ultimately I tracked this down to GlusterFS. It appears (and I haven't really tested this) that Drupal is I/O intensive enough that the delays of GlusterFS made a noticeable (and unacceptable) difference.

Here's the timing for one page (logged into Drupal, so boost isn't helping) with GlusterFS:

	Executed 229 queries in 294.47 milliseconds. Page execution time was 3820.92 ms.

Here's the same page without GlusterFS:

	Executed 229 queries in 325.98 milliseconds. Page execution time was 839.68 ms.

Now I'm not here saying you can't run Drupal on GlusterFS. I'm not even saying I had it configured right. (Remember, I didn't read the docs - at least not all of them.) But I'm reasonably confident I had it configured and optimized well, and I got considerably better results when not using GlusterFS. In my case, I got acceptable results only without GlusterFS.

I still need to synchronize filesystems, so I tried another new-to-me program, lsyncd.[^lsyncd] I like it, and it works well for this application, where the file system is not changing all that often. Perhaps I'll write something up on lsyncd another day.

[^drbd]: I still recommend [DR:BD][drbd], it's cool beans. RAID-1 across a network. Nice.

[drbd]: http://www.drbd.org "Block storage devices distributed, even mirrored, across servers."

[^linode-ha]: I've blogged about this before, including a how-to for [building high availability Linode pairs][linode-ha].

[linode-ha]: http://version2beta.com/articles/high-availability-linode-pairs "A how-to of sorts for high-availability Linode pairs."

[^gluster]: GlusterFS provides multi-master file systems, much like OCFS, but without the poisonous "Oracle" in it's name. (Actually it's now owned by RedHat.)

[gluster]: http://www.gluster.com/ "Private cloud storage"

[^docs]: **Important note:** RedHat bought GlusterFS shortly before I started using it, and even though it was only a week ago I was bitching and moaning about the documentation, the new docs are up. Also, when I took my moaning to Twitter, someone almost immediately tweeted back at me that the new docs were coming very soon.

[^we]: [WebEnabled][we] is a development-platform-as-a-service-provider.

[we]: http://www.webenabled.com "Instant development servers with zero systems administration."

[^lsyncd]: Live sync'ing daemon. [Lsyncd][] watches the directories you tell it to, and when something changes, it rsync-ssh's the changes around to other machines. Kinda like a DIY Dropbox.

[lsyncd]: http://code.google.com/p/lsyncd/ "Live syncing daemon"
