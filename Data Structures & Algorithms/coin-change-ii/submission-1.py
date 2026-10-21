class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                if c <= i:
                    dp[i] += dp[i - c]
        print(dp)
        return dp[amount]
        
        # 1 1 1
        # 1 2
        # 2 1 
        # 3