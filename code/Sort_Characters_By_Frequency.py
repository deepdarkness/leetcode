class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        letter_dict = {}
        for l in s:
            if l in letter_dict:
                letter_dict[l] += 1
            else:
                letter_dict[l] = 1
        sorted(letter_dict.items(), lambda x, y: cmp(x[1], y[1]))
        res = ""
        for ou in sorted(zip(letter_dict.values(),letter_dict.keys()), reverse=True):
            res += ou[1]*ou[0]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort("aaaabbbccccccc"))