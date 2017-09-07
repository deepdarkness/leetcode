# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        max_num = nums[0]
        max_ptr = 0
        for ptr in range(len(nums)):
            if nums[ptr] > max_num:
                max_num = nums[ptr]
                max_ptr = ptr
        thisNode = TreeNode(max_num)
        thisNode.left = self.constructMaximumBinaryTree(nums[:max_ptr])
        thisNode.right = self.constructMaximumBinaryTree(nums[max_ptr + 1:])
        return thisNode
