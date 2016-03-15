class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mappedDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        mappedS = [mappedDict[x] for x in s]
        ret = sum(mappedS)
        for index in range(len(mappedS) - 1):
            if mappedS[index] < mappedS[index + 1]:
                ret -= 2 * mappedS[index]
        return ret
