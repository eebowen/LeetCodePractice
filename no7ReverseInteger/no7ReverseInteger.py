class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x<-2147483648 or x > 2147483647):
            return 0
        else:
            self.x = x
            xStr = str(x)
            xStrInv = ""
            if(xStr[0] =='-'):
                xStrInv+= '-'
                xStr = xStr[1:]
                xStrInv+= xStr[::-1]
            else:
                xStrInv = xStr[::-1]
            # print(xStrInv)
            if(int(xStrInv) < -2147483648 or int(xStrInv) > 2147483647):
                return 0
            else:
                return int(xStrInv)
        

a = Solution()
print(a.reverse(-123))
