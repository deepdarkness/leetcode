class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bought=-99999
        sale=0
        cooldown=0
        for i in prices:
            bought,sale,cooldown=max(bought,sale-i),max(sale,cooldown),bought+i
        return max(sale,cooldown)

