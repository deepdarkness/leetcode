class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numdict = {}
        for n in nums:
            if n in numdict:
                numdict[n] += 1
            else:
                numdict[n] = 1
        resAll = sorted(numdict.iteritems(),key = lambda i:i[1],reverse=True)
        print(resAll)
        res = []
        for i in xrange(k):
            res.append(resAll[i][0])
        return res

if __name__ == '__main__':
    slu = Solution()
    print(slu.topKFrequent([1,2,2,2,3,3],3))