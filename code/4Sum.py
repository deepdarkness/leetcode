class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        self.results = []
        self.NSum(target, nums, 4, [])
        return self.results

    def NSum(self, res_target, res_num, res_pos, result):
        if res_pos == 1:
            for i in res_num:
                if i == res_target:
                    if result + [i] not in self.results:
                        self.results.append(result + [i])
                    return
                elif i > res_target:
                    return
        else:
            for l in range(len(res_num)):
                if res_num[l] * res_pos <= res_target <= res_num[-1] * res_pos:
                    self.NSum(res_target - res_num[l], res_num[l + 1:], res_pos - 1, result + [res_num[l]])
                else:
                    return


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([0,0,0,0], 0))
