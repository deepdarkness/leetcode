class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dt = {}
        for i in nums:
            if i in dt:
                dt[i] += 1
            else:
                dt[i] = 1
        for i in dt:
            if dt[i] != 3:
                return i
