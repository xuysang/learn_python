# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
class Solution:
	def twoSum(self,nums,target):
		c = {}
		for index,num in enumerate(nums):
			another_num = target - num
			if another_num in c:
				print([c[another_num],index])
				return [c[another_num],index]
			c[num] = index
		return None
a = Solution()
nums = [5,5,11,15]
target = 20
a.twoSum(nums,target)