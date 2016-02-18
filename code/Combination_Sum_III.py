class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k > 9 or k < 1:
            return []
        ans = []

        def travel(current, sum, leftk, pos):
            if pos == 0:
                for i in range(1, 10):
                    travel(current + [i], i, leftk - 1, pos + 1)
                return
            if pos == k:
                if sum == n and leftk == 0:
                    ans.append(current)
                return
            for i in range(current[-1] + 1, 10):
                travel(current + [i], sum + i, leftk - 1, pos + 1)

        travel([], 0, k, 0)
        return ans
