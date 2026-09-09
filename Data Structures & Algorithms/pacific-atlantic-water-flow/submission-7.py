class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def dfs(i, j, ocean):
            ocean.add((i, j))  
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in ocean:
                        if heights[x][y] >= heights[i][j]:
                            dfs(x, y, ocean)
        
        for j in range(n):
            dfs(0, j, pacific)
        
        for i in range(m):
            dfs(i, 0, pacific)
                

        for j in range(n):
            dfs(m-1, j, atlantic)
        
        for i in range(m):
            dfs(i, n-1, atlantic)
        
        return [(r, c) for r, c in (atlantic & pacific)]
            

