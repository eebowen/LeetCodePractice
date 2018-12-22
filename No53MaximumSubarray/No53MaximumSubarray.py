class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax = nums[0]
        maxSum = curMax
        for num in nums[1:]:

            curMax = max(num,curMax+num)
            maxSum = max(maxSum,curMax)
        return maxSum






    '''
    O(n^2) solutions: too solw.
    max = nums[0]
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum >= max:
                max = sum
    '''

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
