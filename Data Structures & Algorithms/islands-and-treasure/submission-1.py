class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m = len(grid)
        n = len(grid[0])
        vis =  set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    vis.add((i, j))
        dist = 0
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        while q:
            curr_len = len(q)
            while curr_len:
                r, c = q.popleft()
                grid[r][c] = dist
                for k in range(4):
                    x = r + dx[k]
                    y = c + dy[k]
                    if 0 <= x < m and 0 <= y < n:
                        if (x, y) not in vis:
                            if grid[x][y] == INF:
                                q.append((x, y))
                                vis.add((x, y))
                curr_len -= 1
            dist += 1

        
        