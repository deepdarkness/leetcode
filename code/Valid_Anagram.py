class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        wd = {}
        for i in s:
            if i in wd:
                wd[i] += 1
            else:
                wd[i] = 1
        for i in t:
            if i not in wd:
                return False
            else:
                if wd[i] > 1:
                    wd[i] -= 1
                else:
                    del wd[i]
        if not len(wd):
            return True
        else:
            return False
