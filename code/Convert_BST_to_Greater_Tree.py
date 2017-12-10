# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.node_link = []
        self.trave(root)
        add_num = 0
        for i in self.node_link:
            old_num = i.val
            i.val += add_num
            add_num += old_num
        return root

    def trave(self, node):
        if not node:
            return
        self.trave(node.right)
        self.node_link.append(node)
        self.trave(node.left)
