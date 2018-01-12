# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        def valiedTree(isleft, node, left_range, right_range):
            if left_range < node.val < right_range:
                rest = True
                if node.left:
                    rest = rest and valiedTree(True, node.left, left_range, node.val)
                if node.right:
                    rest = rest and valiedTree(False, node.right, node.val, right_range)
                return rest
            else:
                return False

        res = True
        if root.left:
            res = res and valiedTree(True, root.left, float("-inf"), root.val)
        if root.right:
            res = res and valiedTree(False, root.right, root.val, float("inf"))
        return res
