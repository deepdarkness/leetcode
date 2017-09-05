class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = 'qwertyuiop'
        line2 = 'asdfghjkl'
        line3 = 'zxcvbnm'
        res = []
        for word in words:
            now_line = ''
            i = word[0].lower()
            if i in line1:
                now_line = line1
            elif i in line2:
                now_line = line2
            else:
                now_line = line3
            flag = True
            for l in word.lower()[1:]:
                if l not in now_line:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
