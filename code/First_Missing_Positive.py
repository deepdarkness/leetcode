class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i = 0
        while i < len(nums):
            if nums[i] != i + 1 and nums[i] > 0 and nums[i] - 1 < len(nums) and nums[i] != nums[nums[i] - 1]:
                tmpx = nums[i]
                tmpy = nums[nums[i] - 1]
                nums[nums[i] - 1] = tmpx
                nums[i] = tmpy

            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        else:
            return i + 1
