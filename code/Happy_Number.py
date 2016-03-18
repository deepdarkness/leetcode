class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        di = []
        total = n
        for i in range(10):
            while True:
                t = total % 10
                total //= 10
                di.append(t)
                if total == 0:
                    break
            for t in di:
                total += t ** 2
            if total == 1:
                return True
            else:
                di = []
        return False
