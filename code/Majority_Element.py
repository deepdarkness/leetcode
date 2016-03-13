class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dt = {}
        for i in nums:
            if i in dt:
                dt[i] += 1
                if dt[i] > (l // 2):
                    return i
            else:
                dt[i] = 1
                if dt[i] > (l // 2):
                    return i
