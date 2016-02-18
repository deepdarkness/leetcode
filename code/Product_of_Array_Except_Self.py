class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        res = [1] * l
        for i in range(1, l):
            res[i] = nums[i - 1] * res[i - 1]
        tmp = nums[-1]
        for i in range(l - 2, -1, -1):
            res[i] = res[i] * tmp
            tmp = tmp * nums[i]
        return res
