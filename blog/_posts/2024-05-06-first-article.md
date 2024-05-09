---
layout: post
title:  "First Real Blog Entry"
date:   2024-05-06
categories: testing update
---

![A fancy looking laptop that is entirely unrelated to my blog post, but helps me test out image functionality.](/assets/images/main-bg-img.png)

Alright, after finishing up the main functionality of this website and working on the blog feature for a few hours today, I should probably try writing something real for once to test out its various features.

---

# Summary


TLDR: Working on my website, trying to see if this blog feature works now. Going to need a blog list page (and probably a project showcase page too at some point, but not right now), and then I want to get to other projects like a chess engine and more web development.

## Subheading because these look neat too

You know what, let's try formatting that in list form to see if that needs any tweaking.

TLDR List:

- Working on my website
- Trying to see if the blog works now
- Going to need a blog list page
    - Probably also a project showcase page in the future
- Want to get to other projects
    1. Chess engine
    2. More web development with CS50W
    
List is over now.

# Let's have this be the body

By this point in time, the website is mostly finished. I got the general layout and basic CSS setup a few days ago, and was working for a few hours yesterday on the nice looking animations. 
Once I finished that, I decided that I would rather not host any blog entries or programming guides on Medium because I've had negative experiences with it in the past---namely them deleting half of my "How to use Neovim with Unity on Linux" guide and then ignoring my support ticket---so I thought I might as well implement a blog feature on my own website.
However, one of the main drawbacks I have encountered has been related to web hosting. See, normally I would just go with something like Django or Flask and make a full fledged web application, but because I'm using GitHub Pages to host this site for free, I'm limited to good ol' HTML, CSS, and JavaScript on the front end.
I suppose I could always look into something like Google Firebase or some other hosting solution in the future, but for now, that seemed like it would be overkill for a simple portfolio website with a basic blog feature.

As a result, I started looking for ways to turn Markdown files into HTML code that I could add to a `blogs` folder instead.
One of the first results I came across was `pandoc`, which seemed to be a pretty good option.
I started messing around with its features, but as the number of command line arguments kept growing, I thought it would probably be a good idea to write a python script to insert Pandoc's output into a specified HTML template file.
All seemed well and good for the next hour or two until I realized that *Pandoc already had this feature built in*. Nice, I suppose I don't need to include template functionality in my script.

Once I finally got things up and running, there were a number of CSS bugs I had to work out because this blog is piggybacking off of the CSS I wrote for the main website (where I basically show my various projects and leave a contact page for anyone who wants to reach out).
Once I got those working, things seemed to be going fairly well, and I decided to upgrade my script to include an "update all" feature, so I wouldn't have to manually fix things after changing my HTML template file.
At that point, it was about time to **actually write something** after spending so much time creating a platform that I could use to write blog posts and programming articles, so voilà. 
Here I am, hoping that when I run my `markdownToHtml.py` script, I'll get a fancy new blog post and not a bunch of Pandoc errors.
We'll have to see. 

# Future Projects

Lastly, I guess I can talk about my plans for now.
To start, I need to implement some kind of "list of blogs" HTML page that I can automatically update whenever I publish a new article (probably with another Python script because again, I'm using a static website for simplicity's sake).
After that, I'm looking to be done with this website for now and move onto more interesting projects.
In particular, I'm planning on putting together a chess engine this summer, which should present a bunch of fun challenges from a technical standpoint.
Right now, I'm somewhat torn between making it a desktop app and a browser based game because on the one hand, the web functionality would make it possible to play the game with other people on my phone, but then I would have to look into setting up multiplayer, so we'll have to see.
Besides that, since my regular classes are finishing up in a few weeks, I started taking Harvard's freely available CS50W to get more familiar with web development, and I need to get back to that pretty soon.
(Hmm, I wonder what gave me the inspiration to build this site).

---

In any case, this is probably good enough for a real blog post, so I'm going to try generating the HTML now and go from there.