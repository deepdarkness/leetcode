class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        maxres = ''

        i = 0
        while i < len(s):
            # for single
            start = i
            end = i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            lens = end - start + 1
            if lens >= 1:
                if lens > maxlen:
                    maxlen = lens
                    maxres = s[start + 1:end]

            # for double center
            dstart = i - 1
            dend = i
            while dstart >= 0 and dend < len(s) and s[dstart] == s[dend]:
                dstart -= 1
                dend += 1
            lens = dend - dstart + 1
            if lens >= 2:
                if lens > maxlen:
                    maxlen = lens
                    maxres = s[dstart + 1:dend]

            i += 1

        return maxres


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("a"))
