class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_ans = 0
        max_ans = x
        if x == 1:
            return 1
        while True:
            tmp = (min_ans + max_ans) // 2
            xtmp = tmp * tmp
            if xtmp == x:
                return tmp
            elif xtmp > x:
                max_ans = tmp
            else:
                if max_ans - min_ans <= 1:
                    return min_ans
                else:
                    min_ans = tmp
