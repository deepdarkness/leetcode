class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def travel(current, lleft, rleft):
            if lleft + rleft == 0:
                ans.append(current)
                return
            if lleft == rleft and lleft > 0:
                travel(current + '(', lleft - 1, rleft)
                return
            if rleft > lleft > 0:
                travel(current + ')', lleft, rleft - 1)
                travel(current + '(', lleft - 1, rleft)
            elif rleft > lleft == 0:
                travel(current + ')', lleft, rleft - 1)

        travel('', n, n)
        return ans
