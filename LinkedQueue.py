'''
Program: Linked Queue Stack
Author: Christian M. Adams

Notes: Builds a Linked Queue using the framework of LinkedList.py

'''

#Linked Stack

from LinkedList import LinkedList

class LinkedQueue:
	def __init__(self):
		self.queue = LinkedList()
	
#push(item) - adds a new item to the front of the stack
	def enqueue(self, item):
		self.queue.add(item)
	
	#pop(): item - removes and returns the last item aded.
	def dequeue(self):
		return self.queue.pop()
		
	#peek(): item - returns the item at the front of the stack, stack is unchanged
	def peek(self):
		return self.queue.peek()
		
	#isEmpty() - returns True when the stack is empty.
	def isEmpty(self):
		self.queue.isEmpty()
			
	#size() - returns the number of items in the stack.
	def size(self):
		self.queue.size()
		
	#printStack() - prints the items in the stack.	
	def printQueue(self):
		self.queue.printList("Items in Stack")
		
def main():
	myQueue = LinkedQueue()
	for i in range(10):
		myQueue.enqueue(2*i)
	myQueue.printQueue()
	
	for i in range(1,10,2):
		myQueue.dequeue()
		
	myQueue.printQueue()
		
	
	
main()

		
	