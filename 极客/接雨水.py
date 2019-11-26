class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        n = len(height)
        max_left = [0]*n
        max_right =[0]*n
        min = 0
        
        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i+1])
        for i in range(1,n):
            sum = sum + (min(max_left[i],max_right[i]) - height[i])