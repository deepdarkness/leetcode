# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pre_level_node_list = [root]
        aft_level_node_list = []
        while True:
            aft_level_node_list = []
            for i in pre_level_node_list:
                if i.left:
                    aft_level_node_list.append(i.left)
                if i.right:
                    aft_level_node_list.append(i.right)
            if not aft_level_node_list:
                break
            else:
                pre_level_node_list = aft_level_node_list
        return pre_level_node_list[0].val
