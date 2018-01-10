# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k < 2:
            return head

        now_point = now_point_bak = head
        res = None
        pre_tail = None
        is_first = True

        while True:
            # check if it can reverse

            can_reverse = True
            for i in range(k):
                if not now_point:
                    can_reverse = False
                    break
                else:
                    now_point = now_point.next

            now_point = now_point_bak

            if can_reverse:
                p_point = now_point
                n_point = now_point.next
                nx_point = n_point.next
                for i in range(k - 1):
                    n_point.next = p_point
                    p_point = n_point
                    n_point = nx_point
                    nx_point = nx_point.next

                if is_first:
                    res = p_point
                    is_first = False
                else:
                    pre_tail.next = p_point
                pre_tail = now_point
                now_point = now_point_bak = n_point
            else:
                pre_tail.next = now_point
                break
        return res


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)

    s = Solution()
    s.reverseKGroup(a, 2)
