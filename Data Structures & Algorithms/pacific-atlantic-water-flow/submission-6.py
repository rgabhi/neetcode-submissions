class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        vis_p = set()
        vis_a = set()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        def dfs(i, j, vis):
            vis.add((i, j))
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if (0 <= x < m) and (0 <= y < n):
                    if heights[x][y] >= heights[i][j]:
                        if (x, y) not in vis:
                            vis.add((x, y))
                            dfs(x, y, vis)
                            
        ans = []
        for r in range(m):
            dfs(r, 0, vis_p)
            dfs(r, n - 1, vis_a)
        
        for c in range(n):
            dfs(0, c, vis_p)
            dfs(m - 1, c, vis_a)

        for r in range(m):
            for c in range(n):
                if (r, c) in vis_p and (r, c) in vis_a:
                    ans.append([r, c])
        return ans


        