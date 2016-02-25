class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for str, n in zip(symbol, roman_nums):
            num = self.roman(num, n, str, result)
        return ''.join(result)

    def roman(self, num, n, char, result):
        result.append(char * (num // n))
        return num - n * (num // n)
