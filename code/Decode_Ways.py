class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        prev, curr = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                curr = 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                tmp = curr
                curr += prev
                prev = tmp
            else:
                prev = curr
        return curr


if __name__ == '__main__':
    s = Solution()
    print s.numDecodings("12120")
