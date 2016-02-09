class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapdict = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        ans = []
        for i in digits:
            tmp = int(i)
            if ans == []:
                ans += mapdict[tmp]
            else:
                tans = []
                for letter in mapdict[tmp]:
                    tans += [n + letter for n in ans]
                ans = tans
        return ans
