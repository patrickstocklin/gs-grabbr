import praw
import sys
from NTree import NTree, Node 

r = praw.Reddit("Playing Around")
r.login('DontKillTheMedic', disable_warning=True)

subreddit = r.get_subreddit('Python')
submission = subreddit.get_hot(limit=1)
id = []
for art in submission:
	id.append(art.id)	
one_sub = r.get_submission(submission_id = id[0])
#might need to parameterize this
one_sub.replace_more_comments(limit=None, threshold=0)
comments = one_sub.comments

ourTree = NTree()
ourTree.populateTopLevelComments(comments)

ourTree.printTopLevelComments()

i = len(comments)
for comment in comments:
	print i
	print comment.body
	print comment._replies
	print len(comment._replies)
	i += len(comment._replies) 

print i 

flat_comms = praw.helpers.flatten_tree(one_sub.comments)
print len(flat_comms)
