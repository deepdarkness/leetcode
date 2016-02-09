class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}

        def str_sort(word):
            s = sorted(word)
            res = ""
            for i in s:
                res += i
            return res

        for pos, word in enumerate(strs):
            rword = str_sort(word)
            if rword not in d:
                d[rword] = [pos]
            else:
                d[rword].append(pos)

        ans = []
        for lst in d.values():
            tmp = []
            for pos in lst:
                tmp.append(strs[pos])
            ans.append(sorted(tmp))
        return ans
