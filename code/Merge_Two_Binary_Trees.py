# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        t1v = t1.val if t1 else 0
        t2v = t2.val if t2 else 0
        res = TreeNode(t1v + t2v)
        if t1 and t2:
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
        elif t1 and not t2:
            res.left = self.mergeTrees(t1.left, None)
            res.right = self.mergeTrees(None, t1.right)
        elif t2 and not t1:
            res.left = self.mergeTrees(t2.left, None)
            res.right = self.mergeTrees(None, t2.right)
        return res
