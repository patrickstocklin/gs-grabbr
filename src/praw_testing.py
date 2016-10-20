import praw
import sys
from NTree import NTree, Node 

r = praw.Reddit("Playing Around")
r.login('DontKillTheMedic', disable_warning=True)

subreddit = r.get_subreddit('Python')
#print '====================================='
submission = subreddit.get_hot(limit=1)
#print(dir(submission))
id = []
for art in submission:
	id.append(art.id)	
#print '====================================='
one_sub = r.get_submission(submission_id = id[0])
#print(dir(one_sub))
#print(vars(one_sub))
#print '====================================='
comments = one_sub.comments
#print(dir(comms))
#print comms.count
#print len(comms)
#print '====================================='

ourTree = NTree()
ourTree.populateTopLevelComments(comments)

#for comment in comms:
	#print(dir(comment))
	#print '====*&^$#%^%$#%&%$&^%$*^%#*^%$*^%$*^%$*^%$*^%$*^%$*^%$*^%$*^%$*'
	
	#print comment.body
	#print comment.score
	#print comment._replies
	#print len(comment._replies)
	#print id[0]
	#print comment.parent_id
	#print(vars(comment))
	#ourTree.topLevelComments.append(Node(comment.body))

#print len(comms)
ourTree.printTopLevelComments()

#Grab Subreddit
#Grab Submission
#For all comments in Submission
	#Pass Through
	#

#I think I should make a tree out of this
#Root Node points to all Top Level Comments








