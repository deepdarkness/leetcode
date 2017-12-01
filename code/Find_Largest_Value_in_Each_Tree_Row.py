# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        preList = [root]
        valueList = []
        sufList = []
        res = []
        while preList:
            for i in preList:
                valueList.append(i.val)
                if i.left: sufList.append(i.left)
                if i.right: sufList.append(i.right)
            if not valueList:
                return res
            res.append(max(valueList))
            preList = sufList
            sufList = []
            valueList = []
