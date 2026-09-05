class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        peri = 0
        vis = [[0 for _ in range(n)]  for _ in range(m)]
        s = (-1, -1)
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s = (i, j)
                    break
            if s != (-1, -1):
                break
        q.append(s)
        vis[s[0]][s[1]] = 1
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
            
        while q:
            u = q.popleft()
            cnt1 = 0
            for k in range(4):
                x = u[0] + dx[k]
                y = u[1] + dy[k]
                
                if (0 <= x < m) and (0 <= y < n):
                    if grid[x][y] == 1:
                        cnt1 += 1
                        if not vis[x][y]:
                            vis[x][y] = 1
                            q.append((x, y))
                        
            peri += (4 - cnt1)
        return peri

                
                        

                



        