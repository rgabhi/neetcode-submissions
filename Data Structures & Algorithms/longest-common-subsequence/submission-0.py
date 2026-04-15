class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        def longest(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = max(longest(i-1, j), longest(i, j-1), longest(i - 1, j - 1))
            if text1[i] == text2[j]:
                dp[i][j] = max(dp[i][j], 1 + longest(i - 1, j - 1))
            return dp[i][j]
        return longest(m -1, n - 1)
            
