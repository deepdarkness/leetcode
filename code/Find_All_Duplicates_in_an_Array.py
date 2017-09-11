class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans = []
        if not nums:
            return ans
        pre_num = nums[0]
        for now_num in nums[1:]:
            if pre_num == now_num:
                ans.append(now_num)
            else:
                pre_num = now_num
        return ans
