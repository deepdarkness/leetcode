# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        h = ListNode(0)
        h.next = head

        hvar = head.val
        preptr = head
        while preptr.next:
            if preptr.next.val < hvar:
                break
            preptr = preptr.next
            hvar = preptr.next.val

        ptr = preptr.next
        preptr.next = None  # h --> head --> None  ptr --> head.next --> ...

        while ptr:
            tmp = h
            while tmp.next:
                if tmp.next.val > ptr.val:
                    b = tmp.next
                    tmp.next = ListNode(ptr.val)
                    tmp.next.next = b
                    break
                tmp = tmp.next
            else:
                tmp.next = ListNode(ptr.val)
            ptr = ptr.next

        return h.next
