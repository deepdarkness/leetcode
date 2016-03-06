# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = 0
        list_vet = [root]
        while len(list_vet) != 0:
            for i in range(len(list_vet)):
                a = list_vet.pop(0)
                if a.left is not None:
                    list_vet += [a.left]
                if a.right is not None:
                    list_vet += [a.right]
            depth += 1
        return depth
