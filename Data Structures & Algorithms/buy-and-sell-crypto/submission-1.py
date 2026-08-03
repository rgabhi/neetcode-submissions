class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        maxp = 0
        while r < n:
            if prices[r] >  prices[l]:
                maxp = max(maxp, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return maxp