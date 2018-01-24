# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        res = ListNode(0)
        res.next = head
        pre_node = res
        now_node = head
        next_node = head.next

        while next_node:
            if now_node.val == next_node.val:
                while next_node:
                    next_node = next_node.next
                    if next_node and now_node.val != next_node.val:
                        now_node = next_node
                        pre_node.next = next_node
                        if next_node:
                            next_node = next_node.next
                        break
                    elif not next_node:
                        pre_node.next = None
            else:
                pre_node, now_node, next_node = now_node, next_node, next_node.next

        return res.next
