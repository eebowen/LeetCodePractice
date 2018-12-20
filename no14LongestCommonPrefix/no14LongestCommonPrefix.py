class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        assert isinstance(strs,list)
        if strs == []:
            return ""
        commonPrefix = ""
        smallest = len(strs[0])

        for i in range(len(strs)):
            if len(strs[i]) < smallest:
                smallest = len(strs[i])
        for j in range(smallest):
            flag = False
            same = strs[0][j] # the chars in first string.
            for k in range(len(strs)):
                if same != strs[k][j]:
                    return commonPrefix
                else:
                    flag = True
            if flag == True:
                commonPrefix += strs[k][j]
        return commonPrefix

a = Solution()
inputList = ["flower","flow","flight"]
inputList1 = ["dog","racecar","car"]
print(a.longestCommonPrefix(inputList1))
