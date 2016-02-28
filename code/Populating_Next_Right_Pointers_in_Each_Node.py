# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        st = [root, None]
        while st != [None]:
            tmp = st.pop(0)
            if tmp.left:
                st.append(tmp.left)
            if tmp.right:
                st.append(tmp.right)
            while tmp:
                tmp.next = st.pop(0)
                tmp = tmp.next
                if tmp:
                    if tmp.left:
                        st.append(tmp.left)
                    if tmp.right:
                        st.append(tmp.right)
            st.append(None)
