class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[-1][-1] or obstacleGrid[0][0] == 1:
            return 0

        height = len(obstacleGrid)
        weight = len(obstacleGrid[0])

        obstacleGrid[-1][-1] = -1
        for h in range(height - 1, -1, -1):
            for w in range(weight - 1, -1, -1):
                if obstacleGrid[h][w] == 0:
                    tmp = 0
                    if h < height - 1:
                        tmp += obstacleGrid[h + 1][w] if obstacleGrid[h + 1][w] != 1 else 0
                    if w < weight - 1:
                        tmp += obstacleGrid[h][w + 1] if obstacleGrid[h][w + 1] != 1 else 0
                    obstacleGrid[h][w] = tmp
        return -obstacleGrid[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
