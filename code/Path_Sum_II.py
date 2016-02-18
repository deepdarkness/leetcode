# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans

        def travel(node, s, trace):
            # leaf node
            if not node.left and not node.right:
                if s + node.val == sum:
                    ans.append(trace + [node.val])
            if node.left:
                travel(node.left, s + node.val, trace + [node.val])
            if node.right:
                travel(node.right, s + node.val, trace + [node.val])

        travel(root, 0, [])
        return ans
