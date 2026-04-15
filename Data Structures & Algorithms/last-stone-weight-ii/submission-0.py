class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumW = sum(stones)
        target = math.ceil(sumW/2)
        n = len(stones)

        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
        
        def dfs(i, total):
            if (total >= target) or (i == n):
                return abs(total - (sumW - total))
            
            if dp[i][total] != -1:
                return dp[i][total]

            dp[i][total] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return dp[i][total]

        return dfs(0, 0)
            
        