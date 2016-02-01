class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ans = [0] * (len(triangle) + 1)
        tmp = [0] * (len(triangle) + 1)
        level = len(triangle) - 1
        for i in range(level, -1, -1):
            for j in range(i + 1):
                tmp[j] = min(ans[j], ans[j + 1]) + triangle[i][j]
                ans = tmp
        return ans[0]
