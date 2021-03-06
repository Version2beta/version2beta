---
pagetitle: The developers will fix it
longtitle: How to introduce library updates to production
author: Rob Martin
tags: devops
published: 2013-06-17 18:00
snippet: Much of our code depends on an ecosystem of open source libraries built by third party developers. Here's my take on getting library updates into production, at least when you have a small team of developers.
---

I'm pretty sure my dev team thinks I have it out for them. It's because I always give them the latest and greatest version of every library, regardless of whether our code is tested with that version.

My job includes responsibility for managing development, continuous integration, customer acceptance, and production environments. I wrote an installer that will build any of these environments. It uses Opscode Chef-solo[^chef] with a dynamically-generated JSON definition file that varies based on how the environment will be used. For example, every developer makes their own environment on one or more local virtual machines. Each developer can configure that environment using a Python program I wrote that manipulates the JSON to suit his or her[^hisher] needs.

I made a design decision in creating this environment-builder that impacts our development workflow. Only production environments lock libraries to a given version. In other words, everything but production always gets the latest and greatest versions of all third party libraries.

In an ideal world, this is probably not the right way to do this. An comfortably funded and staffed development team would probably prefer to lock libraries at a "known-to-be-working" version so that devs only deal with problems they've created, not problems some third party open source developer introduced in their latest update. When a new version of a dependent library is released, a ticket gets generated and someone introduces it to a unit testing or continuous integration environment where the new library can be vetted properly, and any required changes to the code can be made.

Or maybe the ideal is to wait for a new release of our software, and then slam ourselves with all the updates at once. Code it with the known-working libraries, then update everything in one fell swoop. Make it, break it, fix it, ship it.

Not all teams can work this way. The company I'm working for right now is funded by accounts receivables, not angels or venture capitalists. We push a lot of code, and when something is billable, it's often done. Refactoring - hell, sometimes even unit testing - is a luxury. I'm not saying we're short-sighted. We want unit tests and have started writing them. We want continuous integration and we've started building that environment. But the primary target is business viability, not code maintainability. And even though I'm writing about current experience, it is worth noting that *every* development company I've worked for has been funded this way, with many of the same practices.

I know from experience across multiple teams that updated versions of third party libraries get attention only when there's a major reason to include them, usually a bug we can't work around. When we get around to using the new version, it may be one or more major releases ahead of what we've been using. There's a good chance it will be a non-trivial task to deploy the upgrade.

My solution was to create an environment that can be reprovisioned quickly and painlessly. Every time we reprovision, the installer updates virtually everything - except in the production environment, which has its own list of packages that specify versions explicitly. Any developer who reprovisions his or her local development environment (a virtual machine) gets the latest and greatest of everything, and that might break what they've been coding. If it does, they deal with it. Every night, the CI environment reprovisions and runs tests automatically. This may also catch incompatibilities and other issues related to libraries. If it breaks, I deal with it, or find a developer who can.

This system definitely catches issues. An ETL[^etl] library we're using is currently borked. Our code works with the library as of three releases ago, but not with any release since. There are five bug fixes, quite a few new features, and some significant performance improvements we're not getting because our code fails with the new versions. We back-burnered that upgrade while a dev scrambles to make the newest version work.

Getting new releases into the workflow improves our overall quality and reduces our technical debt. Mine is a practical solution, pragmatic even. I don't think that following best practices is an ivory-tower endeavor, but I recognize that it's a journey for a lot of small companies, especially when you already have a code base that evolved over years of hard work, often the product of passion more than programmers.

[^chef]: [Chef][chef] is a tool for building infrastructure automatically. It's based on Ruby, is reasonably easy to learn, and runs stand-alone, with a central server, or with a hosted environment at Opscode.

[chef]: http://www.opscode.com/chef/ "Chef at Opscode.com."

[^hisher]: I say 'his or her' because I think it's an important habit to use language that recognizes diversity in the workplace, especially in tech. I actually work with all men.

[^etl]: [ETL stands for Extract, Transform, Load][etl] and it refers to the process of getting data out of one system and into another. It's often used for data warehousing.

[etl]: http://en.wikipedia.org/wiki/Extract,_transform,_load "Extract, transform, load at Wikipedia"
