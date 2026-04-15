class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            grid[r][c] = "-1"
            for k in range(4):
                x = r + dx[k]
                y = c + dy[k]
                if (0 <= x < m) and (0 <= y < n) and (grid[x][y] == "1"):
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1            

        return cnt   
        