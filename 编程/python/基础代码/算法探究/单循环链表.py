class Node:
	def __init__(self,item):
		self.item = item
		self.next = None

class SinCycLinkedlist:
	def __init__(self):
		self.head = None

	def is_empty(self):
		return None == self.head

	def add(self,item):
		temp=Node(item)
		temp.next=self.head
		self.head = temp

	def lengt(self):
		if self.is_empty():
			return 0
		n = 1
		cur = self.head
		while cur.next != None:
			cur = cur.next
			n += 1
		return n
	'''
	def ergodic(self):
		if self.is_empty():
			raise ValueError('error null')
		cur = self.head
		# print(cur.item)
		while cur.next != None:
			cur = cur.next
			# print(cur.item)
	'''
	def search(self,item):
		if self.is_empty():
			raise ValueError('error null')
		cur = self.head
		found = False
		while cur != None and not found:
			if cur.item == item:
				found = True
			else:
				cur = cur.next
		print(found)

	def remove(self,item):
		cur = self.head
		previous = None
		found = False
		while not found:
			if cur.item == item:
				found = True
			else:
				previous = cur
				cur = cur.next
		if previous == None:
			self.head=cur.item
		else:
			previous.next=cur.item
	

list_01=SinCycLinkedlist()
list_01.add(1)
list_01.add(2)
list_01.add(4)
list_01.add(5)
list_01.add(6)
list_01.add(7)
list_01.add(8)
k=list_01.lengt()
print(k)
# list_01.ergodic()

list_01.remove(2)
# list_01.ergodic()