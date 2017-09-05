class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resSum = 0
        nums.sort()
        for i in range(len(nums) // 2):
            resSum += min(nums[i * 2], nums[i * 2 + 1])
        return resSum
