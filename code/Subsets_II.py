class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_dict = {}
        l = len(nums)
        nums.sort()

        def pick(pre_ans, left_nums, left_pos):
            if left_nums == 0:
                ans = tuple(pre_ans)
                if ans not in res_dict:
                    res_dict[ans] = True
            else:
                for i in range(left_pos, l):
                    pick(pre_ans + [nums[i]], left_nums - 1, i + 1)

        for i in range(len(nums) + 1):
            pick([], i, 0)

        return [list(i) for i in res_dict.keys()]
