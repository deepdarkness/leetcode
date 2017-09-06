class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def find_around(x, y):
            around_point = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
            res = 0
            for xptr, yptr in around_point:
                if xptr < 0 or yptr < 0 or xptr == len(grid) or yptr == len(grid[0]) or grid[xptr][yptr] == 0:
                    res += 1
            return res

        total_pamt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_pamt += find_around(i, j)
        return total_pamt
