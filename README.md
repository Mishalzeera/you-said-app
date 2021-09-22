One main page per user, with tasks to accept/work on and tasks that they have
assigned.

Inbox.

Interesting bug: Started a manual commit in VSCode without a message, then left
the console without following with the prompted message. I couldn't commit
after that, getting an error that a lock file exists and that I would have to
manually remove it. On Stack Overflow I found the solution - rm .git/index.lock
and then it worked again.

Dont forget Debug=True.
