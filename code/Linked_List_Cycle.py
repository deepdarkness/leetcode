# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next or not head.next.next:
            return False
        onestep = head.next
        twostep = head.next.next
        while onestep != twostep:
            if not onestep or not twostep:
                return False
            if not twostep.next:
                return False
            onestep = onestep.next
            twostep = twostep.next.next
        return True
