class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None
		
class LinkedList(object):

	def __init__(self):
		self.head = None
		self.size = 0
		
	# O(1) !!!	
    
	def insertStart(self, data):
	
		self.size = self.size + 1
		newNode = Node(data)
		
		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode
    
    	
		
	# O(N)
    	def insertEnd(self,data):
        	self.size=self.size+1
       	 	newNode=Node(data)
        	
        	actualNode=self.head
        
        	if not self.head:
            		self.head=newNode
        	else:
            		while actualNode.nextNode is not None:
                		actualNode=actualNode.nextNode
           	 		actualNode.nextNode=newNode

	def remove(self, data):
	
		if self.head is None:
			return
			
		self.size = self.size - 1
		
		currentNode = self.head
		previousNode = None
		
		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode
			
		if previousNode is None:										#Search node is the first node
			self.head = currentNode.nextNode

		else:
			previousNode.nextNode = currentNode.nextNode		


		
	def traverseList(self):
	
		actualNode = self.head
		
		while actualNode is not None:
			print("%d " % actualNode.data,end=" ")
			actualNode = actualNode.nextNode



linkedlist=LinkedList()
b=1
while(b):
    b=int(input("\nEnter choice\n 1 to insert at start \n 2 to insert at end \n 3 to delete a node \n 4 to traverse \n 0 to exit: \n "))
    
    if(b==1):
        a=int(input("Enter a number: "))
        linkedlist.insertStart(a)
    elif b==2:
        a=int(input("Enter a number: "))
        linkedlist.insertEnd(a)
    elif b==3:
        a=int(input("Enter a number: "))
        linkedlist.remove(a)
    elif b==4:
        linkedlist.traverseList()
