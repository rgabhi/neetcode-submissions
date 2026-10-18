class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def max_profit(i, buy):
            if i < 0:
                return 0
            if i == 0:
                return -prices[i] if buy else 0
                
            # if last sold
            if (i, buy) not in dp:
                # buy today or skip
                if buy:
                    dp[(i, buy)] = max(
                        max_profit(i - 2, False) - prices[i], 
                        max_profit(i - 1, True)
                    )
                # sell today (buy == False)
                else:
                   dp[(i, buy)] = max(
                        max_profit(i - 1, True) + prices[i], 
                        max_profit(i - 1, False))
            
            return dp[(i, buy)]

        return max(max_profit(n - 1, True), max_profit(n-1, False))
            
            
        