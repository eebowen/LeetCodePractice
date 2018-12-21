class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        for i in range(len(s)):
            # print('s[i]:' , s[i])
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                self.add(s[i])
                # print('add ',s[i])
            else:
                if s[i] == ")":
                    if self.peak() == "(":
                    # print('remove ',s[i], 'pair')
                        self.remove()
                    else:
                        return False
                if s[i] == "]":
                    if self.peak() == "[":
                    # print('remove ',s[i], 'pair')
                        self.remove()
                    else:
                        return False
                if s[i] == "}": 
                    if self.peak() == "{":
                    # print('remove ',s[i], 'pair')
                        self.remove()
                    else:
                        return False

        if not self.stack:
            return True
        else:
            return False



    def __init__(self):
        self.stack = []
    def add(self,data):
        if data:
            self.stack.append(data)
            return True
        else:
            return False
    def peak(self):
        return self.stack[-1]
    def remove(self):
        if len(self.stack) == 0:
            return("No element in stack")
        else:
            return self.stack.pop()
    def printStack(self):
        print(self.stack)



stack1 = Solution()
# stack1.isValid("()()[]")
print(stack1.isValid('[[[]]]{}()'))
# print(stack1.printStack())
# print(stack1.peak())
# stack1.add("1")
# stack1.add("2")
# stack1.add("3")
# stack1.printStack()
# stack1.remove()
# stack1.remove()
# stack1.printStack()
