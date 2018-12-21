# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if (not l1) and (not l2): #both empty
            return l1
        if (not l1) and (l2): # l1 empty
            return l2
        if (l1) and (not l2): # l2 empty
            return l1


        if l1.val <= l2.val:
            lCurrent = ListNode(l1.val)
            l1 = l1.next
        else:
            lCurrent = ListNode(l2.val)
            l2 = l2.next
        lHead = lCurrent
        while l1 and l2: # while their next are not None.
            if l1.val <= l2.val:
                lCurrent.next = l1
                l1 = l1.next
            else:
                lCurrent.next = l2
                l2 = l2.next
            lCurrent = lCurrent.next
        if l1:
            lCurrent.next = l1
        else:
            lCurrent.next = l2
        return lHead



# create linked list
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
# while list1:
#     print(list1.val)
#     list1 = list1.next

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
# while list2:
#     print(list2.val)
#     list2 = list2.next
a = Solution()
lHead = a.mergeTwoLists(list1,list2)
while lHead:
    print(lHead.val)
    lHead = lHead.next 
# list2 = ListNode(2)
# list1.next = list2

# print(list1.next.val)