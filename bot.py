# -*- coding: utf-8 -*-
#iBooie Tech Support Bot
#This is a TEMPLATE. Based off the tutorial at http://pythonforengineers.com/build-a-reddit-bot-part-2-reply-to-posts/ and modified to allow for multiple lines and UTF-8 
#Note: this requires PRAW to work.
#!/usr/bin/python
import praw
import pdb
import re
import os
from config_bot import * ##This is calling a seperate file for the login information.

# Check that the file that contains our username exists
if not os.path.isfile("config_bot.py"):
    print "You must create a config file with your username and password."
    print "Please see config_bot.py"
    exit(1)

# Create the Reddit instance
user_agent = ("InsertUserAgentHere")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

# Get the top 5 values from our subreddit
subreddit = r.get_subreddit('jailbreak') ##Subreddit this bot lives on.
for submission in subreddit.get_new(limit=5): #Gets newest posts and replies.
    # print submission.title

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("SEARCH_TERM", submission.selftext, re.IGNORECASE): #Looks for SEARCH_TERM in a post's text.
            # Reply to the post
            submission.add_comment('''
Here, put your text for the bot. I put my tutorial here.
**Supports basic markup, like links and formatting**.
Blah Blah Blah.

**I am a bot! [[Information]](https://www.reddit.com/r/jailbreak/comments/3sqmab/meta_i_created_a_bot_to_help_people_with_boot/) [[Creator]](https://reddit.com/u/HeyItsShuga) [[Feedback]](https://www.reddit.com/message/compose/?to=HeyItsShuga&subject=iBootie Feedback)**
''') ##Message
            print "Bot replying to : ", submission.title

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")



