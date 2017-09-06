class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(list(s))
        t = sorted(list(t))
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

