class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        l = len(nums)
        count = 0
        for i in range(l):
            if nums[i] == 0:
                count += 1
            else:
                nums[i - count] = nums[i]
        for i in range(l - count, l):
            nums[i] = 0
