class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        l = len(nums)
        a = b = c = 0
        ans = target
        diff = float('inf')
        while a < l - 2:
            b = a + 1
            c = l - 1
            while b < c:
                s = nums[a] + nums[b] + nums[c]
                if s == target:
                    return target
                elif s > target:
                    if s - target < diff:
                        diff = s - target
                        ans = s
                    c -= 1
                else:
                    if target - s < diff:
                        diff = target - s
                        ans = s
                    b += 1
            a += 1
        return ans
