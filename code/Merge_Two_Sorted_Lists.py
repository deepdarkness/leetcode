# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        relist = ListNode(None)
        reptr = relist

        if not l1:
            return l2
        if not l2:
            return l1

        f = 0

        while True:
            while ptr1.val <= ptr2.val:
                reptr.next = ListNode(ptr1.val)
                reptr = reptr.next
                if ptr1.next:
                    ptr1 = ptr1.next
                else:
                    f = 1
                    break
            if f == 1:
                break
            while ptr1.val > ptr2.val:
                reptr.next = ListNode(ptr2.val)
                reptr = reptr.next
                if ptr2.next:
                    ptr2 = ptr2.next
                else:
                    f = 2
                    break
            if f == 2:
                break
        if f == 1:
            reptr.next = ptr2
        else:
            reptr.next = ptr1
        return relist.next
