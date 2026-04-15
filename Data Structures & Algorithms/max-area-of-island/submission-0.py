class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        def bfs(r, c):
            tmp_area = 0
            q = deque()
            grid[r][c] = -1
            q.append((r, c))
            while q:
                r, c = q.popleft()
                tmp_area += 1
                for k in range(4):
                    x = r + dx[k]
                    y = c + dy[k]
                    if (0 <= x < m) and (0 <= y < n) and (grid[x][y] == 1):
                        grid[x][y] = -1
                        q.append((x, y))

            return tmp_area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    max_area = max(area, max_area) 
        return max_area        
        