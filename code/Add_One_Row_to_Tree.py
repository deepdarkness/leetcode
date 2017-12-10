# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        preList = [root]
        afterList = []

        res = root

        if d == 1:
            newHead = TreeNode(v)
            newHead.left = root
            res = newHead
            return res

        for i in range(d - 2):
            for p in preList:
                if p.left:
                    afterList.append(p.left)
                if p.right:
                    afterList.append(p.right)
            preList = afterList
            afterList = []

        for p in preList:
            if p.left:
                tmp = p.left
                new_node = TreeNode(v)
                new_node.left = tmp
                p.left = new_node
            else:
                new_node = TreeNode(v)
                p.left = new_node

            if p.right:
                tmp = p.right
                new_node = TreeNode(v)
                new_node.right = tmp
                p.right = new_node
            else:
                new_node = TreeNode(v)
                p.right = new_node
        return res
