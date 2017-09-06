class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < 1:
            return True
        s_ptr = 0
        for i in t:
            if i == s[s_ptr]:
                s_ptr += 1
                if len(s) == s_ptr:
                    return True
        return False



s = Solution()
print(s.isSubsequence("axc", 'ahbgdc'))
