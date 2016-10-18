import sys
import os
import time

class Node():
	def __init__(self, comment, score):
		self.comment = comment
		self.children = []
		self.score = score
		self.parent = None
	
	def printNode(self):
		print str(self.score) + ':' + self.comment

	def addChild(self, Node):
		self.children.append(Node)

	def printChildren(self):
		print "There are %s children" %str(len(self.children))
		for child in self.children:
			child.printNode()

class NTree():	
	def __init__(self):
		self.root = Node("", 0)
		self.topLevelComments = []		

	def populateTopLevelComments(self, comments):	
		for topLevelComment in comments:
			node = Node(topLevelComment.body, topLevelComment.score)
			self.root.addChild(node)		

	def printTopLevelComments(self):
		print "Printing"
		for comment in self.root.children:
			comment.printNode()
def main():
	print "begin"
	a = Node("Node A", 0)
	a.printNode()
	b = Node("Node B", 0)
	b.printNode()
	a.addChild(b)
	a.printChildren()
	print "end"

if __name__ == '__main__':
	main()
