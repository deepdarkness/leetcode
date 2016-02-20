class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        r = len(height) - 1
        l = 0
        maxv = 0
        while True:
            if r == l:
                break
            maxv = max(maxv, (r - l) * min(height[r], height[l]))
            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1
        return maxv

