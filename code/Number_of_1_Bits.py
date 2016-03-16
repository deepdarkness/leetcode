class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = bin(n)[2:]
        return l.count('1')
