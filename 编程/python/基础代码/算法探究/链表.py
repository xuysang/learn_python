
class Node():  # 这只是一个Node类，还不是链表，这里只是介绍了节点的性质
	def __init__(self,data):
		self.data=data  # 构造一个节点，节点有它的元素，也有指向下一个元素的指针
		self.next=None
'''
	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data=newdata

	def setNext(self,newnext):
		self.next=newnext

node=Node(1)
node1=Node(3)
print(node.data)
print(node.next)
node.setData(node1)
node.setNext(node1)
node.setData(2)
print(node.data)
print(node.next.data)
'''

class NodeList():
	def __init__(self,node=None):
		self.head=node

	def isempty(self):
		return self.head==None

	def length(self):
		cur = self.head
		count=0
		while cur:   # cur != None
			count+=1
			cur=cur.next
		return count

	def add(self,item):
		temp=Node(item)
		temp.next=self.head
		self.head=temp
list1=NodeList()
list1.add(2)
list1.add(3)
list1.add(4)
list1.add(5)
list1.add(6)
print(list1.length())

