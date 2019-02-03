import praw
import pdb
import re
import os

subreddits = ['news', 'worldnews', 'futurology', 'photoessay', 'politics', 'nottheonion', 'upliftingnews']

#open and load history of crossposted submissions
if not os.path.isfile("xposthist.txt"):
    xposthist=[]
else:
    with open("xposthist.txt", "r") as f:
        xposthist = f.read()
        xposthist = xposthist.split("\n")
        xposthist = list(filter(None, xposthist))

#initialize praw
reddit = praw.Reddit('bot1')

for x in range(0,len(subreddits)):
    sr = reddit.subreddit(subreddits[x])
    for submission in sr.top(time_filter = 'day', limit=3):
        if submission.id not in xposthist:
            #crosspost
            cross_post = submission.crosspost(subreddit = "newscollection", send_replies = False)
            #setflair
            cross_post.mod.flair(text=sr)
            print( "subreddit: ", sr)
            #add submission id to xposthist
            xposthist.append(submission.id)

#write updated list back to file
with open("xposthist.txt", "w") as f:
        for submission_id in xposthist:
            f.write(submission_id + "\n")


