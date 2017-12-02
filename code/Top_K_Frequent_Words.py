class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        resdict = {}
        for w in words:
            if w in resdict:
                resdict[w] += 1
            else:
                resdict[w] = 1
        def cmpf(a,b):
            if a[1]<b[1]:
                return -1
            elif a[1]>b[1]:
                return 1
            else:
                return -1 if a[0]<b[0] else 1

        sortedResList = sorted(resdict.iteritems(), cmp= cmpf, reverse=True)
        return [i[0] for i in sortedResList[:k]]