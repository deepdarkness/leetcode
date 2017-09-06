class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = sorted(set(nums))
        if len(tmp) < 3:
            return max(tmp)
        else:
            return tmp[-3]
