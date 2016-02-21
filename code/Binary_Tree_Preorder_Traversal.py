# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        if not root:
            return res
        st = [root]
        while st:
            tmp = st.pop(0)
            res.append(tmp.val)
            if tmp.right:
                st = [tmp.right] + st
            if tmp.left:
                st = [tmp.left] + st
        return res
