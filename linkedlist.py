class Node(object):
	def __init__(self, data, next = None):
		self.data = data
		self.next = next


class LinkedList(object):
	def __init__(self, head, tail):
		self.head = head 
		self.tail = tail 
	#Instance methods below
	#returns the integer length of the linkedlist
	def getLength(self):
		current = self.head 
		if self.head == None:
			return 0 
		i = 0
		while current:
			current = current.next 
			i += 1
		return i 
	def prtlist(self):
		current = self.head
		if self.head == None:
			return 0 
		while current:
			print current.data
			current = current.next

	#returns the head, which is an instance of a Node object 
	def getHead(self):
		return self.head
	#returns the tail, which is an instance of a Node object
	def getTail(self):
		return self.tail
	# inserts a node at the end and returns the head 
 	def insertAtEnd(self,head,data):
 		newnode = Node(data)
 		if self.head == None:
 			self.head = newnode
 		else:
 			current = self.head
 			while current.next:
 				current = current.next
 			current.next = Node(data)
 		return self.head
	def insertAtHead(self,head,data):
		if head == None:
			head = Node(data)
		else:
			newnode = Node(data)
			newnode.next = head
			head = newnode 
		return head

	def Delete(head, position):
	    current = head 
	    index = 0
	    if position == 0:
	        head = head.next
	        return head 
	    while index < position:
	        previous = current
	        current = current.next
	        index += 1
	    previous.next = current.next
	    return head 
	def Reverse(head):
	    current = head 
	    previous = None
	    while current != None:
	        next = current.next
	        current.next = previous
	        previous = current
	        current = next
	    head = previous
	    return head

def checkequal(headA,headB):
	if headA == None:
		if headB == None:
			return True
		else:
			return False
	if headB == None:
		if headA == None:
			return True
		else: 
			return False

	currentA = headA
	currentB = headB

	while currentA.next:
		if currentA == currentB:
			currentA = currentA.next
			currentB = currentB.next
			continue
		else:
			return False
	return True

def removedups(head):
	dic = {}
	current = head
	while current.next:
		if current.data not in dic:
			dic[current.data] = current.next.data
			temp = current
			current = current.next
		else:
			temp = current
			current = current.next
			temp.next = current.next
	return head



c = Node(3)
x = Node(3)
y = Node(7)


a = LinkedList(x,c)
# b = LinkedList(x,c)
a.insertAtEnd(a.head,8)
a.insertAtEnd(a.head,10)
a.insertAtEnd(a.head,10)




removedups(a.head)

a.prtlist()