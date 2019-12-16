class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
def rightSide(root):
	result = []
	queue = [root]
	while len(queue) > 0:
		length = len(queue)
		print(length)
		for i in range(length):
			node = queue.pop(0)
			print(node.val)
			if i == length-1:
				result.append(node.val)
				print(result)
			if node.left != None:
				queue.append(node.left)
			if node.right != None:
				queue.append(node.right)

	return result
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.right = node6
node2.left = node4
node2.right = node5
node5.left = node7
print(rightSide(node1))
