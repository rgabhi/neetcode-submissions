class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            dp[i][i + 1] = (s[i] == s[i + 1])
        
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
        cnt = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    cnt += 1
        return cnt

            
        
        
        