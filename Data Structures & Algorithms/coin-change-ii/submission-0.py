class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        n = len(coins)
        def get_ways(curr_amount, i):
            if curr_amount < 0 or i >= n:
                return 0
    
            if dp[curr_amount][i] != -1:
                return dp[curr_amount][i]
            
            if curr_amount == 0:
                return 1

            dp[curr_amount][i] = 0
            dp[curr_amount][i] = (
                get_ways(curr_amount - coins[i], i) + 
                get_ways(curr_amount, i + 1)
            )
            return dp[curr_amount][i]
            
        return get_ways(amount, 0)
        