# Advent of Code 2021

## Plan of action

My solutions for the advent of code 2021

Scaffold.py is just a shell to save myself time when making my main executable file.  I just copy it into each puzzle.

All inputs generated with cyberchef.  Here's a sample cyberchef that turns a newline separated list of things into an array of strings:
https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'%5C%5Cn'%7D,'%22,%20%22',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'%5B%22',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'$'%7D,'%22%5D',true,false,true,false)&input=b25lCnR3bwp0aHI

Each folder is a number based on the day it's a solution for.  Shared code will live in the root here.

So, yeah, I think that's everything.  If you have any questions, feel free to message me.

Thanks!

## New wave input parsing

I've decided that cyberchef was cumbersome, so I decided to create a magic python thing that would pull inputs for me.  See pull_input.py.
That script lets you just provide a day, and it will reach out and pull the stuff for you.
It even massages it into a format that doesn't suck to work with.

Syntax is `./pull_input.py -d <your target day> > data.py`

Only caveat is that you need to pull your session id out of the browser, and drop that into a file called session_id.dat.
Sample file included here.

To get the session id, just look in your cookies in your browser.  It should be keyed as "session" and just be a long hex string.

This left me with a pickle when it came to formatting the little examples though, so I made parse_tiny_input.py.  To use that, do the following:

```
./parse_tiny_input.py << HEREDOC
your
input
goes
here
HEREDOC
```

And that will parse it for you no problem, the same way as if it was pulled from the web.
That obviously works with the full input as well, if you don't want to bother with the session id.
