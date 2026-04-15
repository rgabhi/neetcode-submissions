class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = {}
        def get_coins(total):
            if total in dp:
                return dp[total]
            if total == 0:
                dp[total] = 0
                return 0
            dp[total] = float('inf')
            for coin in coins:
                if coin <= total:
                    dp[total] = min(dp[total], 1 + get_coins(total - coin))
            return dp[total]
        get_coins(amount)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]