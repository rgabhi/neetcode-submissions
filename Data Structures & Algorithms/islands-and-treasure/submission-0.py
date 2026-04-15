class Solution:
    INF = 2147483647
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        def find_min_distance(r, c):
            pq = []
            heapq.heappush(pq, (0, r, c))
            while pq:
                curr_dist, r, c = heapq.heappop(pq)
                if curr_dist == grid[r][c]:
                    for k in range(4):
                        x = r + dx[k]
                        y = c + dy[k]
                        if (
                            (0 <= x < m) and
                            (0 <= y < n) and
                            (grid[x][y] not in (0, -1))
                        ):
                            if grid[x][y] > (1 + curr_dist):
                                grid[x][y] = curr_dist + 1
                                heapq.heappush(pq, (1 + curr_dist, x, y))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    find_min_distance(i, j)
                    
        
        
        