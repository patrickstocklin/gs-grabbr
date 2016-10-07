import praw
import sys

r = praw.Reddit("Playing Around")
r.login('DontKillTheMedic')

subreddit = r.get_subreddit('Python')
print(dir(subreddit))
print(vars(subreddit))
print '====================================='
submission = subreddit.get_hot(limit=1)
print(dir(submission))
id = []
for art in submission:
	id.append(art.id)	
print '====================================='
one_sub = r.get_submission(submission_id = id[0])
print(dir(one_sub))
print(vars(one_sub))
print '====================================='
comms = one_sub.comments
print(dir(comms))
print comms.count
print len(comms)
print '====================================='
for comment in comms:
	#print(dir(comment))
	print '===='
	print comment.body
	print comment.score
	#print(vars(comment))
