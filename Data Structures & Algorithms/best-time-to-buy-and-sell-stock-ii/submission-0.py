class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        curr = prices[n-1]
        for i in range(n-2, -1, -1):
            if prices[i] > curr:
                curr = prices[i]
            else:
                profit += (curr - prices[i])
                curr = prices[i]
        return profit

        