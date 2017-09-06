class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dis_order_amount = 0
        nums = [-1] + nums
        pre_num = nums[0]
        pre_pre_num = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] < pre_num:
                dis_order_amount += 1
                if dis_order_amount > 1:
                    return False
                if nums[i + 1] >= pre_pre_num:
                    pre_num = nums[i + 1]
            else:
                pre_pre_num = pre_num
                pre_num = nums[i + 1]
        return True

