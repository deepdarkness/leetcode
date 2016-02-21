class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = [float('inf')] * (amount + 1)
        ans[0] = 0
        coins.sort(reverse=True)
        for i in range(1, amount + 1):
            ans[i] = min([ans[i - j] + 1 if i - j >= 0 else float('inf') for j in coins])
        return ans[amount] if ans[amount] != float('inf') else -1
