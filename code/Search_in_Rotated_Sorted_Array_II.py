class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        try:
            nums.index(target)
        except:
            return False
        return True
