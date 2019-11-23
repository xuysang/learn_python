#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
class Solution1:
	def rotate(self,nums,k):
		for i in range(k):
			nums.insert(0,nums.pop())
		print(nums)
class Solution2:
	def rotate(self,nums,k):
		n = len(nums)
		k %= n
		def swap(l,r):
			while l<r:
				nums[r],nums[l]=nums[l],nums[r]
				r -= 1
				l += 1
		swap(0,n-k-1)
		swap(n-k,n-1)
		swap(0,n-1)
		print(nums)
class Solution3:
	def rotate(self,nums,k):
		n = len(nums)
		k %= n
		nums[:]=nums[::-1]
		nums[:k]=nums[:k][::-1]
		nums[k:]=nums[k:][::-1]
		print(nums)

a=Solution1()
b=Solution2()
c=Solution3()
list1=[1,2,3,4,5,6,7]
list2=[1,2,3,4,5,6,7]
list3=[1,2,3,4,5,6,7]
k=3
a.rotate(list1,k)
b.rotate(list2,k)
c.rotate(list3,k)
