class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c = 'abcdefghijklmnopqrstuvwxyz'
        l = len(words)
        bitmap = []
        for i in words:
            k = 0
            for char in i:
                k |= 1 << c.find(char)
            bitmap.append(k)
        maxlen = 0
        for i in range(l):
            for j in range(i + 1, l):
                if bitmap[i] & bitmap[j] == 0:
                    tmp = len(words[i]) * len(words[j])
                    maxlen = max(tmp, maxlen)
        return maxlen
