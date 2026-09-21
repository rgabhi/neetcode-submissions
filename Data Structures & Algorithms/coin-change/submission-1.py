class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        dp = [0]*(n + 1)
        dp[0] = 0
        for i in range(1, n+1):
            dp[i] = float('inf')
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(1 + dp[i - coins[j]], dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1