class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1,-1,-1):
	        digits[i] += 1 #从右往左依次对数位上的数加一
	        digits[i] = digits[i]%10 #当末尾是9，加一后除10取余得到0，再次循环直到不为0的位数
	        if (digits[i] !=0):
		        return digits
        digits = [0]*(n+1) # 当循环结束，各个数位上的值加一后都为0，则整个数组加一位数，赋值首位为1
        digits[0] = 1
        return digits
s = Solution()
digits = [8,9,9]
result = s.plusOne(digits)
print(result)