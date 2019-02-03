import praw
import pdb
import re
import os

#Open and load comhist as list of comments commented on before
if not os.path.isfile("comhist.txt"):
    comhist = []
else:
    with open("comhist.txt", "r") as f:
        comhist = f.read()
        comhist = comhist.split("\n")
        comhist = list(filter(None, comhist))

#initialize praw
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("canucks")

for comment in  subreddit.comments(limit=20):
	print("Author: ", comment.author)
	print("Created: ", comment.created_utc)
	print("Body: ", comment.body)
        #check if comment is in comhist list
        if comment.id not in comhist and comment.author.name != 'TemporaryPromise9':
            if re.search("messier", comment.body, re.IGNORECASE):
                newcomment = comment.reply("FUCK MESSIER!")
                print("********* Bot replied **********")
                #Add new comment and commented comment ids into list
                comhist.append(comment.id)
        #write updated list back to file
        with open("comhist.txt", "w") as f:
            for comment_id in comhist:
                f.write(comment_id + "\n")
        print("-------------------------\n")
