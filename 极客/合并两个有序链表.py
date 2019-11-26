# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution1:
	def mergeTwoLists(self,l1:ListNode,l2:ListNode):
		res = ListNode(None)
		node = res
		while l1 and l2:
			if l1.val < l2.val:
				node.next,l1 = l1,l1.next
			else:
				node.next,l2 = l2,l2.next
			node = node.next
		if l1:
			node.next = l1
		if l2:
			node.next = l2
		return res.next

class Solution2:
	def mergeTwoLists(self,l1:ListNode,l2:ListNode):
		if l1 == None: return l2
		if l2 == None: return l1
		if l1.val > l2.val: l1,l2 = l2,l1
		l1.next = self.mergeTwoLists(l1.next,l2)
		return l1

s1 = Solution1()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
s1.mergeTwoLists(l1,l2)