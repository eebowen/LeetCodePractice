#  reverting the number itself, 
# and then compare the number with original number
# if the reversed number is larger than int.MAX, we will hit integer overflow.
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
