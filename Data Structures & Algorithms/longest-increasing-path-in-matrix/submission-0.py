class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = 1
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if (0 <= x < m) and (0 <= y < n) and (matrix[i][j] > matrix[x][y]):
                    dp[i][j] = max(dp[i][j], 1 + dfs(x, y))
            
            return dp[i][j]
            
        ans = 1
        for r in range(m):
            for c in range(n):
                if dp[r][c] == -1:
                    ans = max(ans, dfs(r, c))
                else:
                    ans = max(ans, dp[r][c])
        print(dp)
        return ans
        