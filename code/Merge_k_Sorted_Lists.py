# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        ListNode.__lt__ = lambda s, f: True
        import heapq
        head = ListNode(0)
        ptr = head
        h = []
        for i in lists:
            if i:
                x = (i.val, i)
                heapq.heappush(h, x)
        while True:
            try:
                (_, p) = heapq.heappop(h)
                ptr.next = p
                ptr = p
                if p.next:
                    heapq.heappush(h, (p.next.val, p.next))
            except IndexError:
                break
        return head.next
