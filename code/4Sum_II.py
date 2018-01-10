class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res_dict = {}
        res = 0
        for i in A:
            for j in B:
                p = (i + j)
                if p not in res_dict:
                    res_dict[p] = 1
                else:
                    res_dict[p] += 1
        for i in C:
            for j in D:
                p = (i + j)
                if -p in res_dict:
                    res += res_dict[-p]
        return res
