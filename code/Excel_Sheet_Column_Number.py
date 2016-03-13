class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 1:
            return 0
        s = s[::-1]
        result = 0
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for pos, alpha in enumerate(s):
            result += ((26 ** pos) * (uppercase.index(alpha) + 1))

        return result
