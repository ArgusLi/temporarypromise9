import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("canucks")

for comment in  subreddit.comments(limit=10):
	print("Author: ", comment.author)
	print("Created: ", comment.created_utc)
	print("Body: ", comment.body)
	#if submission.num_comments>0:
	#	print (">0 Comments")
	print("-------------------------\n")
