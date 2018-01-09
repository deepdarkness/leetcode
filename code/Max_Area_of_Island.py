class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.height = len(grid)
        self.weight = len(grid[0])
        self.mark_finding = []
        for i in range(self.height):
            self.mark_finding.append([0] * self.weight)
        max_area = 0
        for x, y in [(x, y) for x in range(self.height) for y in range(self.weight)]:
            if self.mark_finding[x][y] == 1 or grid[x][y] == 0:
                continue
            else:
                max_area = max(max_area, self.deep_area(x, y))
        return max_area

    def deep_area(self, x, y):
        if self.grid[x][y] == 1:
            if self.mark_finding[x][y] == 1:
                return 0
            self.mark_finding[x][y] = 1
            res_num = 1
            if x + 1 < self.height:
                res_num += self.deep_area(x + 1, y)
            if y + 1 < self.weight:
                res_num += self.deep_area(x, y + 1)
            if x - 1 >= 0:
                res_num += self.deep_area(x - 1, y)
            if y - 1 >= 0:
                res_num += self.deep_area(x, y - 1)
            return res_num
        else:
            return 0
