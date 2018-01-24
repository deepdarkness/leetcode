class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        mark_pos = 1
        step_mark = [0] * len(nums)
        for pos in range(len(nums)):
            now_step = step_mark[pos]
            now_val = nums[pos]
            for mark_range in range(mark_pos, min(now_val + pos + 1, len(nums))):
                step_mark[mark_range] = now_step + 1
                mark_pos = min(now_val + pos + 1, len(nums))
            if mark_pos == len(nums):
                return step_mark[-1]