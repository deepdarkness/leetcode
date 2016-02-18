class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        a = b = float('inf')
        for i in nums:
            if i < a:
                a = i
            elif a < i < b:
                b = i
            elif i > a and i > b:
                return True
        return False
