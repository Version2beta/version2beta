---
pagetitle: Freaky shadow
longtitle: According to my logs, I was being followed.
author: Rob Martin
published: 2011-06-09 13:21
snippet: The webserver logs showed I was being followed on my path through a website by a computer at an IP address in Texas. It trailed two seconds behind me, on every page.
---

The webserver logs showed I was being followed on my path through a website by a computer at an IP address in Texas. It trailed two seconds behind me, on every page.

It was a dark and stormy day, and a strange thing happened while I
was debugging some PHP code.

I was using [error\_log][] to pass some variables and values to the
standard Apache log, and tailing it to make sure PHP was seeing
what I wanted it to see. That was when I saw something I didn’t
expect to see.

    [Thu Jun 09 13:37:54 2011] [error] [client 24.xxx.xx.xxx] Carrier: ...
    [Thu Jun 09 13:37:54 2011] [error] [client 24.xxx.xx.xxx] Returning ...
    [Thu Jun 09 13:37:56 2011] [error] [client 75.xxx.xx.xxx] Carrier: ...
    [Thu Jun 09 13:37:56 2011] [error] [client 75.xxx.xx.xxx] Returning ...

Each time I hit the page, my code logged the access. Then, a second
or two later, another entry *from a different IP address* was also
logged.

Everything I did was being shadowed by a server in Texas.

It took a few minutes of research to discover that the IP address
belongs to one of [ClickTale’s servers][], and that the page I was
modifying runs their analytic code. Freakiness abated.

  [error\_log]: http://php.net/manual/en/function.error-log.php "PHP manual page for error_log"
  [ClickTale’s servers]: http://www.clicktale.com/ "Clicktale does experience analytics"
