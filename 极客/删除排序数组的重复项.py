# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
class Solution:
	def removeDuplicates(self,nums):
		i = 0
		for num in nums:
			if num != nums[i]:
				i += 1
				nums[i] = num
		print(nums)
		return len(nums) and i+1
a=Solution()
nums = [1,1,2,2,2,3,3]
print(a.removeDuplicates(nums))