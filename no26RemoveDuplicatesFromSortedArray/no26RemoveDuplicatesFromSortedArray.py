class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        r = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[r]:
                r+=1
                nums[r] =nums[i]
        return r+1
        
a = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(a.removeDuplicates(nums))