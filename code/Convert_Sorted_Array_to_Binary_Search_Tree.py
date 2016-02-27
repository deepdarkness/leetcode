# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l < 1:
            return None

        def insertTreeNode(left, right):
            if left > right:
                return None
            t = TreeNode(nums[(right + left) / 2])
            t.left = insertTreeNode(left, (right + left) / 2 - 1)
            t.right = insertTreeNode((right + left) / 2 + 1, right)
            return t

        return insertTreeNode(0, l - 1)
