class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        dit = {}
        for i in nums:
            if i not in dit:
                dit[i] = 1
            else:
                return True
        return False
