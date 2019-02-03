import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("canucks")

for comment in subreddit.comments(limit = 5):
    print comment.author.name
    if comment.author.name == 'TemporaryPromise9':
        print "this is temporary promise"
    print ("----------------\n")

