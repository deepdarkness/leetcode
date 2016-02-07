class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        l1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        l2 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
              "Nineteen"]
        l3 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        l4 = ["", "Thousand", "Million", "Billion"]
        num_bit = []
        result = ''
        if num == 0:
            return 'Zero'
        while num > 0:
            k = num % 10
            num //= 10
            num_bit = [k] + num_bit
        l = len(num_bit)
        num_bit = (10 * [0] + num_bit)[-15:]

        def resolve3bit(a, b, c):
            prefix = ''
            subfix = ''
            if b == 0:
                subfix = l1[c]
            elif b == 1:
                subfix = l2[c]
            else:
                subfix = l3[b] + ' ' + l1[c]
            if a == 0:
                prefix = ''
            else:
                prefix = l1[a] + ' Hundred '
            return prefix + subfix

        l4bit = 0
        while True:
            s = resolve3bit(num_bit[-3 - l4bit * 3], num_bit[-2 - l4bit * 3], num_bit[-1 - l4bit * 3])
            if s != '':
                result = (s + ' ' + l4[l4bit] + ' ' + result)
            if l >= 0:
                l4bit += 1
                l -= 3
            else:
                break
        lk = result.split()
        result = ''
        for i in lk:
            result += i + ' '
        return result[:-1]
