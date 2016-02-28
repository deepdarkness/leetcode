# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        ptr = 1
        st = []
        kt = root
        while st != [] or kt:
            if kt:
                st.append(kt)
                kt = kt.left
            else:
                tmp = st.pop()
                if ptr == k:
                    return tmp.val
                else:
                    ptr += 1
                kt = tmp.right
