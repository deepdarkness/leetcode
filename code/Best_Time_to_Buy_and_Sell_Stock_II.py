class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0
        buy_list = []
        ptr = 0
        status = 1
        for i in range(1, l):
            if status == 1:
                if prices[i - 1] > prices[i]:
                    status = 0
                    if i - 1 != ptr:
                        buy_list.append((ptr, i - 1))
            else:
                if prices[i - 1] < prices[i]:
                    status = 1
                    ptr = i - 1
        profile = 0
        for i in buy_list:
            profile += (prices[i[1]] - prices[i[0]])
        if status == 1:
            profile += (prices[-1] - prices[ptr])
        return profile
