class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dt = {}
        if n == 0 or n == 1:
            return 1
        dt[0] = dt[1] = 1
        for i in range(2, n + 1):
            dt[i] = dt[i - 1] + dt[i - 2]
        return dt[n]
