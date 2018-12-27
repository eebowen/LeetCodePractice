class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        no1 = 1
        no2 = 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        for i in range(2,n):
            temp1 = no1
            temp2 = no2
            no1 = temp2+temp1
            no2 = temp1
        return no1+no2
a = Solution()
print(a.climbStairs(4))
    
