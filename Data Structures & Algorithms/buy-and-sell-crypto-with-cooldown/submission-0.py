class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(n)] for _ in range(2)]
        # action: 1 - buying, 0 - selling
        def dfs(action, i):
            if i >= n:
                return 0
            if dp[action][i] != -1:
                return dp[action][i]
            cooldown = dfs(action, i + 1)
            if action == 1:
                buy = -prices[i] + dfs(1 - action, i + 1)
                dp[action][i] = max(buy, cooldown)
            else:
               sell = prices[i] + dfs(1 - action, i + 2)
               dp[action][i] = max(sell, cooldown)
            return dp[action][i]
            
        return dfs(1, 0)



        