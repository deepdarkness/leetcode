class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def cmpfunc(x1, x2):
            if int(x1 + x2) > int(x2 + x1):
                return 1
            else:
                return -1

        nums = map(str, nums)
        nums.sort(cmpfunc, reverse=True)
        tmp = ''.join(nums).lstrip("0")
        if not tmp:
            tmp = "0"
        return tmp
