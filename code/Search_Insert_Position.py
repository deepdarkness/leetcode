class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if l < 1:
            return 0
        left, right = 0, l - 1
        flag = 0
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
                flag = 0
            if nums[mid] < target:
                left = mid + 1
                flag = 1
        return mid if flag == 0 else mid + 1
