
#Linked List Class
from Node import Node


class LinkedList:
	def __init__(self):
		self.head = None
 
	# Add item to the front of the linked list
	def add(self, data):
		node = Node(data)
		if(node != None):
			node.next = self.head
			self.head = node
		   
	#adds item to the end of the linked list.
	def append(self, data):
		#find the last node
		if(self.head == None):  #list is empty
			self.head = Node(data)
		else:
			probe = self.head
			while(probe.next != None):
				probe = probe.next
			probe.next = Node(data)

 
	#size() –returns the number of items in the list.
	def size(self):
		count = 0 
		probe = self.head
		while (probe != None): #there are more nodes in the list
			count += 1
			probe = probe.next
		return count
		
		
 
	#insert(pos, item) – adds item to position pos >= 1.
	def insert(self, pos, item):
		size = self.size()
		if(pos <= 0 or (size - pos )< -1):
			print("Not enough itsms in list to insert in that position. Size =",\
				  size, "position = ", pos)
			return False
		if(pos == 1):
			newNode = Node(item)
			newNode.next = self.head
			self.head = newNode
		else:
			count = 2
			probe = self.head
			while(probe != None and count != pos):
				probe = probe.next
				count += 1
			newNode = Node(item)
			newNode.next = probe.next
			probe.next = newNode
			return True
 
	#popFirst() – removes and returns the first item in the list.
	def popFirst(self):
		if(self.head == None): #list is empty
			return None
		else:
			curr = self.head
			self.head = curr.next
			curr.next = None
			return curr.data
		   
	#pop() – removes and returns the last item in the list.
	def pop(self):
		if(self.head == None): #list is empty
			return None
		else:
			probe = self.head
			prev = None
			while(probe.next != None):
				prev = probe
				probe = probe.next
			if(prev == None):  #only 1 item in list
				self.head = None  # list is empty
				return probe
			else:
				prev.next = None
				return probe
	
	#peek() - looks at the value at the top of the stack
	def peek(self):
		if(self.head == None):  #list is emmpty
			return None
		else:
			return self.head.data
	def isEmpty(self):
		return self.head == None
 
	def printList(self, msg):
		temp = self.head
		print(msg, end = ": ")
		while(temp != None):
			print(temp.data, end=" ")
			temp = temp.next
		print()
		
	#Prints all items LIFO, like a stack
	def printList(self):
		node = self.head
		while node != None:
			print(node.data)
			node = node.next
			
	#Prints all items FIFO, like a queue (This is a work around, if needed for application, a doubly-linked list should be used.
	def printListFIFO(self):
		node = self.head
		a = []
		while node != None:
			a.append(node.data)
			node = node.next
		a.reverse()
		for item in a:
			print(item)
		return a

def main():
	ls = LinkedList()
	print(ls.isEmpty())
	ls.add(4);
	ls.add("JoJo");
	ls.printList()
	ls.printListFIFO()

if __name__ == '__main__':  #Everything below this line will execute if this program is run, but if used as a module, it will not.  
	main()
