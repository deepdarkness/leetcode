# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        st = []
        k = root
        while st != [] or k:
            if k:
                st.append(k)
                k = k.left
            else:
                tmp = st.pop()
                res.append(tmp.val)
                k = tmp.right
        return res
