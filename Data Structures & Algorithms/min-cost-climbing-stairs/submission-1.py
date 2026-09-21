class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n + 1)
        dp[0] = 0
        dp[1] = min(cost[0], 0)
        
        def getCost(i):
            if i < 0:
                return 0
            if i <= 1:
                return dp[i]
            if dp[i] == -1:
                dp[i] = min(cost[i-1] + getCost(i - 1), cost[i - 2] + getCost(i-2))
            return dp[i]
        return getCost(n)