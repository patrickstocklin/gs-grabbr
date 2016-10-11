############################################################
#
#	GS-Grabbr.py
#
#	Author: Pat Stocklin
#
#	Date: 8/31/16
#
#	About: Python Project to run through a given thread
#	and display the comment-trees that contain replies
#	with more upvotes than their parent-comments.
#	
#	TO DO:
#		Option Parsing for Specifying Thread/User
#		Logging Results/Destroying Them
#		*** Self-Updating Parameters ***
#
#		How many more upvotes should reply have?
#		How many upvotes should base-comment have?
#		How many comments should there be in thread?
#		Is there a mathematical function?
#		Does the subreddit in particular matter?
#
#	NOTES:
#		Try a mix of camelCase and snake_case,
#			e.g. grab_All_Submission_Comments
#		Use Pickle for storing settings in .p files
#		Might need to authenticate app with OAuth2
#
#
############################################################

import praw
import pickle
import sys
import os
import getpass
import argparse
'''
CONSTANTS
'''

ACCOUNT_SETTINGS_FILENAME = 'account_settings.p'

#Should handle log-in and authentication
def init_Account():
	print "Please Enter Your Reddit Username"
	username = raw_input()
	print "Please Enter %s's Reddit Password" %(username)
	password = getpass.getpass()
	account = { "username":username, "password":password }
	pickle.dump(account, open(ACCOUNT_SETTINGS_FILENAME, "wb"))	

#Return an Account's Username and Password
def grab_Account_Credentials():
	if not os.path.isfile(ACCOUNT_SETTINGS_FILENAME):
		print "No" + ACCOUNT_SETTINGS_FILENAME + "file present!"
		return
	account = pickle.load(open(ACCOUNT_SETTINGS_FILENAME, "rb"))
	return account['username'], account['password']

#Initializes and Returns PRAW Object
def init_Reddit_Wrapper(username, password):
	r = praw.Reddit("Grabbie")
	r.login(username, password, disable_warning=True)
	return r

#Given a thread_id, grab all comment-trees that pass parameters
def grab_Thread_Comments():
	pass

#Driver
def main():
	parser = argparse.ArgumentParser(description="A python script to filter unwanted comments from a Reddit-thread")
	#parser.add_argument('-u', nargs=1, help='The username of your reddit account')
	#parser.add_argument('-s', nargs=1, help='The subreddits you wish to browse')
	#parser.add_argument('-t', nargs=1, help='The thread you wish to browse')
	#parser.add_argument('-n', nargs=1, help='The number of threads you wish to browse given a subreddit')
	#args = parser.parse_args()



	if not os.path.isfile(ACCOUNT_SETTINGS_FILENAME):
		init_Account()
	username, password = grab_Account_Credentials()	
	r = init_Reddit_Wrapper(username, password)	
	
	#If Grab Subreddit, grab top 10/20/25 submissions in that subreddit
	#Elif Grab Submission, grab submission

	#For all submissions in the queue, grab all comments
		#For all comment trees, prune comment trees that do not pass

	#For all submissions in queue, 
		#For all passed comment trees, print neatly to console

	####################################################	
	hot_Submissions = r.get_subreddit('politics').get_hot(limit=5)
	for x in hot_Submissions: print str(x)
	top_Submissions = r.get_subreddit('politics').get_top(limit=5)
	for x in top_Submissions: print str(x)
	new_Submissions = r.get_subreddit('politics').get_new(limit=5)
	for x in new_Submissions: print str(x)
if __name__ == '__main__':
	main()
