# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def travel(point):
            left_side = []
            tmp = point
            while tmp:
                left_side.append(tmp)
                tmp = tmp.left
            if len(left_side) == 1:
                xt = point.right
                while xt:
                    if xt.left:
                        travel(xt)
                        break
                    else:
                        xt = xt.right
            while len(left_side) != 1:
                t = left_side.pop()
                tend = t
                while tend.right:
                    tend = tend.right
                tprev = left_side[-1]
                tend.right = tprev.right
                tprev.right = t
                tprev.left = None
                xt = t.right
                while xt:
                    if xt.left:
                        travel(xt)
                        break
                    else:
                        xt = xt.right

        travel(root)
