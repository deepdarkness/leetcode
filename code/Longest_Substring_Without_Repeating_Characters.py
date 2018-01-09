class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = []
        maxlen = 0
        for i in s:
            if i not in d:
                d.append(i)
            else:
                maxlen = max(maxlen, len(d))
                d = d[d.index(i) + 1:] + [i]
        return max(maxlen, len(d))


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
