# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        maxlevel = -1
        tmp = root
        while tmp:
            maxlevel += 1
            tmp = tmp.left
        lastLevelTotal = 2 ** maxlevel
        minans = 0
        maxans = lastLevelTotal

        def check(s):
            tmp = root
            for i in s:
                if i == "0":
                    tmp = tmp.left
                else:
                    tmp = tmp.right
            return tmp

        if minans+1==maxans:
            return 1
        while minans<maxans:
            mid = (minans + maxans) // 2
            s = bin(mid)[2:]
            s = "0" * (maxlevel - len(s)) + s
            if check(s):
                minans = mid+1
            else:
                maxans = mid

        return (2 ** maxlevel - 1) +minans
