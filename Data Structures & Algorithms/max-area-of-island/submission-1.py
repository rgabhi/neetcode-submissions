class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        area = 0
        vis = set()
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        def dfs(i, j):
            vis.add((i, j))
            area = 1
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 1:
                        if (x, y) not in vis:
                            vis.add((x,y))
                            area += dfs(x, y)
            return area

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
        


        