class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numdict = {}
        for i in nums:
            if i not in numdict:
                numdict[i] = 1
            else:
                del numdict[i]
        answer = []
        for i in numdict:
            answer.append(i)
        return answer
