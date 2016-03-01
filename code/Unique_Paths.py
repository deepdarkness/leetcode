class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        elif m == 1 or n == 1:
            return 1

        answer = []
        for i in range(m):
            if i == 0:
                answer.append([1] * n)
            else:
                answer.append([1] + [0] * (n - 1))

        for x in range(1, m):
            for y in range(1, n):
                answer[x][y] = answer[x - 1][y] + answer[x][y - 1]
        return answer[m - 1][n - 1]
