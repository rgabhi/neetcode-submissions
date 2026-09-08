class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        vis = set()
        cnt1 = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    vis.add((i, j))
                elif grid[i][j] == 1:
                    cnt1 += 1
        if cnt1 == 0:
            return 0
        time = -1 #because first level in already wrotten, time starts from second level.
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        while q:
            l = len(q)
            while l > 0:
                r, c = q.popleft()
                for k in range(4):
                    x = r + dx[k]
                    y = c + dy[k]
                    if 0 <= x < m and 0 <= y < n:
                        if (x, y) not in vis:
                            if grid[x][y] == 1:
                                grid[x][y] = 2
                                vis.add((x, y))
                                q.append((x, y))
                l -= 1
            time += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        # print(grid)
        return time



            
    
        