class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        xStr = str(x)
        for i in range(len(xStr)):
            if(xStr[i] != xStr[-i-1]):
                return False
        return True

a = Solution()
print(a.isPalindrome(-101))