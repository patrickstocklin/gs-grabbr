import sys
import os
import time

class Node():
	def __init__(self, comment):
		self.comment = comment
		self.children = []
		self.parent = None	

	def printNode(self):
		print self.comment

	def addChild(self, Node):
		self.children.append(Node)

	def printChildren(self):
		print "There are %s children" %str(len(self.children))
		for child in self.children:
			child.printNode()

class NTree():	
	def __init__(self):
		self.root = Node()

	def printTree(self):
		print "Printing"

def main():
	print "begin"
	a = Node("Node A")
	a.printNode()
	b = Node("Node B")
	b.printNode()
	a.addChild(b)
	a.printChildren()
	print "end"

if __name__ == '__main__':
	main()
