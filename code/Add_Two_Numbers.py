# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ptr = ans
        spilth = 0
        while l1 or l2:
            if l1:
                spilth += l1.val
                l1 = l1.next
            if l2:
                spilth += l2.val
                l2 = l2.next
            ptr.next = ListNode(spilth % 10)
            ptr = ptr.next
            spilth //= 10
        while spilth:
            ptr.next = ListNode(spilth % 10)
            ptr = ptr.next
            spilth //= 10
        return ans.next
