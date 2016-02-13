class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numdict={}
        for i in nums:
            if i not in numdict:
                numdict[i]=1
            else:
                del numdict[i]
        for i in numdict:
            return i