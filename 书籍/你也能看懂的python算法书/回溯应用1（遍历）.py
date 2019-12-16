class Solution():
	def solvePermutation(self,array):
		self.helper(array,[])
	def helper(self,array,solution):
		if len(array)==0:
			print(solution)
			return
		for i in range(len(array)):
			newSolution = solution + [array[i]]
			newArray = array[:i] + array[i+1:]
			self.helper(newArray,newSolution)
Solution().solvePermutation(["红","黄","蓝","绿"])