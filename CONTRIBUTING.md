# Contributing #

## Before you open a pull request, please try to do the following ##

[Squash](http://git-scm.com/book/en/Git-Tools-Rewriting-History#Squashing-Commits) your commits, so we can quickly determine what changes you're proposing. This isn't mandatory, but please try to do it.

If you're adding a new address, try to add it to the existing list in the correct place, i.e., in **ascending alphabetical order**.

Example:

    @abc-recruit.com OR 
    @def-workers.net OR 
    @geb-resources.co.uk 

You'd like to add `@enterprise-weasels.com`, so it goes in position 3. The list now looks like:

    @abc-recruit.com OR 
    @def-workers.net OR 
    @enterprise-weasels.com OR 
    @geb-something.co.uk 

Addresses should have the following format:


    @domain[space]OR[space]

Example:

    @recruiter.co.uk OR 

The only exception to this rule is when adding a domain to the end of the list. In that case, the `OR` is omitted, and the format becomes:

    @recruiter.co.uk[space]

Remember to add an `OR` to the penultimate line.

**Please ensure that the last line in your file is blank**
