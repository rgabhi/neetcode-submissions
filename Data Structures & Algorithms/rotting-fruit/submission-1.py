class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        cnt_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    cnt_fresh += 1
        time = 0
        if (len(q) == 0) and (cnt_fresh == 0):
            return 0
        while q:
            sz = len(q)
            time += 1
            while sz > 0:
                r, c = q.popleft()
                for k in range(4):
                    x = r + dx[k]
                    y = c + dy[k]
                    if (
                        (0 <= x < m) and
                        (0 <= y < n) and 
                        (grid[x][y] == 1)
                    ):
                        cnt_fresh -= 1
                        grid[x][y] = 2
                        q.append((x, y))
                sz -= 1

        if cnt_fresh > 0:
            return -1
        return time - 1
                    



        