class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        pre = nums[0]
        for i in range(1, l):
            if nums[i] < pre:
                return nums[i]
        return pre
