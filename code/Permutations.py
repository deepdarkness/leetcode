class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        answer = []
        if l < 1:
            return answer

        def x(pre, left):
            if len(left) == 1:
                answer.append(pre + left)
                return
            ns = len(left)
            for i in range(ns):
                x(pre + [left[i]], left[:i] + left[i + 1:])

        x([], nums)
        return answer
