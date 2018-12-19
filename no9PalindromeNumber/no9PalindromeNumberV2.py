#  reverting the number itself, 
# and then compare the number with original number
# if the reversed number is larger than int.MAX, we will hit integer overflow.

# python3 need to use //. one / will be floating number
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0 or (x%10 ==0 and x!=0)):
            return False
        reversedNum = 0

        while(x>reversedNum):
            reversedNum = reversedNum*10 + x%10
            x = x//10
        print(x)
        print(reversedNum)
        return x==reversedNum or x == reversedNum//10

a = Solution()
print(a.isPalindrome(10))