#冒泡排序
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def sortArray(self, nums=[]) :
        for i in range(len(nums)-1,0,-1):
            for j in range(0,i):
                if nums[j]>nums[j+1]:
                    temp=nums[j+1]
                    nums[j+1]=nums[j]
                    nums[j]=temp
        return nums
    def B(self,nums=[]):
      	ex=True
      	i=len(nums)-1
      	while i>0 and ex:
      		ex=False
      		for j in range(i):
      			if nums[j]>nums[j+1]:
      				ex=True
      				temp=nums[j+1]
      				nums[j+1]=nums[j]
      				nums[j]=temp
      		i=i-1
      	return nums
    def C(self,head):
    	
    	p,rev=head,None
    	while p:
    		rev,rev.next,p=p,rev,p.next
    	return rev

A=Solution()
nums=[5,4,3,2,1]
b=A.sortArray(nums)
c=A.B(nums)
d=A.C(nums)
print(b,c,d)
