# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        answer = ListNode(None)
        answer.next = head
        N = answer
        while N.next and N.next.next:
            F = N.next.next.next
            tmp = N.next
            N.next = N.next.next
            N.next.next = tmp
            tmp.next = F
            N = tmp
        return answer.next
