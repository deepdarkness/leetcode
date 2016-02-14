class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = []
        sadd = 0
        ans = 0
        for i in nums:
            sadd += i
            l.append(i)
            if sadd >= s:
                ans = len(l)
                break
        else:
            return 0
        size = len(nums)
        ptr = minans = ans
        while ptr < size:
            tmp = nums[ptr]
            l.append(tmp)
            sadd += tmp
            ptr += 1
            ans += 1
            while True:
                j = l[0]
                if sadd - j >= s:
                    sadd -= j
                    l.pop(0)
                    ans -= 1
                    minans = min(ans, minans)
                else:
                    break
        else:
            while True:
                j = l[0]
                if sadd - j >= s:
                    sadd -= j
                    l.pop(0)
                    ans -= 1
                    minans = min(ans, minans)
                else:
                    break

        return minans
