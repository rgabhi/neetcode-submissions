class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        max_right = prices[n - 1]
        for i in range(n - 2, -1, -1):
            max_right = max(max_right,prices[i])
            max_profit = max(max_profit, max_right - prices[i])
        return max_profit