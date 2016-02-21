class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        f = math.factorial(n)
        l = [i + 1 for i in range(n)]
        ans = ""
        while l:
            f /= len(l)
            for i in range(len(l)):
                if i * f < k <= (i + 1) * f:
                    ans += str(l[i])
                    l = l[0:i] + l[i + 1:]
                    k -= (i * f)
        return ans
