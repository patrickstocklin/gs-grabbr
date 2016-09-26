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
#		Authentication of User Account
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
############################################################

import praw
import pickle
import sys
import os

#Should handle log-in and authentication
def init_Account():
	account = { "username":"TestUserName", "password":"TestPassWord" }
	pickle.dump(account, open("accountsettings.p", "wb"))	

#Given a thread_id, grab all comment-trees that pass parameters
def grab_Thread_Comments():
	pass

#Driver
def main():
	#init
	#grab

	#While !exit:
	#	display results and capture user-input for recs

	init_Account()	

if __name__ == '__main__':
	main()
