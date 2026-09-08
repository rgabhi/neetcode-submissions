class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = set()
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        def dfs(i, j):
            vis.add((i, j))
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == "1":
                        if (x, y) not in vis:
                            vis.add((x, y))
                            dfs(x, y)

        cnt = 0  
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in vis:
                    dfs(i, j)
                    cnt += 1
        return cnt
                