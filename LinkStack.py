#A simple linked list stack class 
'''
a.	push(item) - adds a new item to the front of the stack.
b.	pop(): item - removes and returns the last item added.
c.	peek(): item - returns the item at the front of the stack, stack is unchanged
d.	isEmpty() - returns True when the stack is empty.
e. 	size() - returns the number of items in the stack.
f. 	printStack() - prints the items in the stack.		
'''

from LinkedList import LinkedList


class LinkStack():
	def __init__(self):
		self.stack = LinkedList() # my stack object
		
	#push(item) - adds a new item to the front of the stack
	def push(self, item):
		self.stack.add(item)
	
	#pop(): item - removes and returns the last item aded.
	def pop(self):
		return self.stack.popFirst()
		
	#peek(): item - returns the item at the front of the stack, stack is unchanged
	def peek(self):
		return self.stack.peek()
		
	#isEmpty() - returns True when the stack is empty.
	def isEmpty(self):
		self.stack.isEmpty()
			
	#size() - returns the number of items in the stack.
	def size(self):
		self.stack.size()
		
	#printStack() - prints the items in the stack.	
	def printStack(self):
		self.stack.printList("Items in Stack")
		
def main():
	myStack = LinkStack()
	for i in range(10):
		myStack.push(2*i)
	myStack.printStack()
	
	for i in range(1,10,2):
		myStack.pop()
		
	myStack.printStack()
		
	
	
main()
