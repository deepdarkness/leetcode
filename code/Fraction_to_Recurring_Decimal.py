class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator * denominator == 0: return '0'
        isPositive = (numerator * denominator) >= 0
        s = numerator % denominator
        if s == 0:
            return str(numerator / denominator)
        n, d = abs(numerator), abs(denominator)
        firstPart = n // d
        n %= d
        dt = []
        yushu = []
        pre = []
        circle = True
        while True:
            yushu.append(n)
            n *= 10
            bit = n / d  # 0<=bit<=9
            n = n % d
            dt.append(bit)
            if n == 0:
                circle = False
                break
            # if len(dt)%2==0:
            #     if dt[:len(dt)/2]==dt[len(dt)/2:]:
            #         dt=dt[:len(dt)/2]
            #         break
            if n in yushu:
                l = len(yushu) - 1
                while True:
                    if n == yushu[l]:
                        pre = dt[:l]
                        dt = dt[l:]
                        break
                    else:
                        l -= 1
                break

        midpart = '.'
        lastpart = ''
        result = ''
        for i in pre:
            midpart += str(i)
        for i in dt:
            lastpart += str(i)
        lastpart = "(" + lastpart + ")" if circle else lastpart
        if not isPositive:
            result = '-' + str(firstPart) + midpart + lastpart
        else:
            result = str(firstPart) + midpart + lastpart
        return result
