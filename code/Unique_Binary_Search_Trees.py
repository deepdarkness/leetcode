class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dt = {0: 1, 1: 1}
        if n < 2:
            return dt[n]
        for i in range(2, n + 1):
            sum = 0
            for x in range(i):
                sum += (dt[x] * dt[i - 1 - x])
            dt[i] = sum
        return dt[n]
