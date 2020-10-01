# Pydriller Test


Playing around with [pydriller](https://github.com/ishepard/pydriller).

The current project looks at a bunch of different github repositories and then
check for commits referencing words related to GDPR, Privacy etc, and saves
these.

The end result will try to visualize these on a timeline and see if there is a
significant spike in commits around that time, and also if it is still relevant.

Ideally we want to not use the manually currated list, but rather the top 1000
repositories on github, however we have currently not been able to find an API
that lists these, so this is a temporary solution.

