class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [i for i in range(left, right + 1) if self.isSelfDividingNumbers(i)]

    def isSelfDividingNumbers(self, num):
        for i in str(num):
            pt = int(i)
            if pt == 0:
                return False
            if num % pt != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.selfDividingNumbers(1, 22))
