class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_res = 0
        max_one_now = 0
        is_in_one_area = 0
        for n in nums:
            if is_in_one_area == 0:
                if n == 1:
                    max_one_now = 1
                    is_in_one_area = 1
            else:
                if n == 1:
                    max_one_now += 1
                else:
                    is_in_one_area = 0
                    max_res = max(max_res, max_one_now)
        max_res = max(max_res, max_one_now)
        return max_res
