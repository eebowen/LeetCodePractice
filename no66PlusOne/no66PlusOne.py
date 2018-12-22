class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] <9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits = [1] + digits
        return digits

a = Solution()
print(a.plusOne([9,9,9,9]))