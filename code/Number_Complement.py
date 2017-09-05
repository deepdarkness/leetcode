class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int('0b' + ''.join([str(abs(int(i) - 1)) for i in bin(num)[2:]]), 2)


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))
