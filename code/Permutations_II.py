class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict = {}
        l = len(nums)
        if l < 1:
            return []

        def x(pre, left):
            if len(left) == 1:
                tmp = tuple(pre + left)
                if tmp not in dict:
                    dict[tmp] = True
                return
            ns = len(left)
            for i in range(ns):
                x(pre + [left[i]], left[:i] + left[i + 1:])

        x([], nums)
        return [list(x) for x in dict.keys()]


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
