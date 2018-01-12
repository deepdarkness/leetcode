# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        travel_ptr = head
        smaller_head = smaller_ptr = ListNode(0)
        bigger_head = bigger_ptr = ListNode(0)

        while travel_ptr:
            if travel_ptr.val < x:
                smaller_ptr.next = travel_ptr
                smaller_ptr = smaller_ptr.next
            else:
                bigger_ptr.next = travel_ptr
                bigger_ptr = bigger_ptr.next
            travel_ptr = travel_ptr.next

        smaller_ptr.next = bigger_head.next
        a = smaller_head.next
        bigger_ptr.next = None
        return a

