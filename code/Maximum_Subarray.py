class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 1:
            return 0
        maxnotinclude = maxinclude = nums[0]
        for i in range(1, l):
            maxinclude = max(maxinclude + nums[i], nums[i])
            maxnotinclude = max(maxnotinclude, maxinclude)
        return maxnotinclude
