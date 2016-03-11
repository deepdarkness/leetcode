# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None or q is None:
            if p == q:
                return True
            else:
                return False

        ls = [p]
        ns = [q]
        while len(ls) >= 1:
            a = ls.pop(0)
            if len(ns) == 0:
                return False
            b = ns.pop(0)
            if a.val != b.val:
                return False
            if a.left is None:
                if b.left is not None:
                    return False
            else:
                ls += [a.left]
                ns += [b.left]
            if a.right is None:
                if b.right is not None:
                    return False
            else:
                ls += [a.right]
                ns += [b.right]
        return True
