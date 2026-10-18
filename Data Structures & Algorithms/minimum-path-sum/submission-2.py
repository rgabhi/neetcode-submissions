class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        MAX = float('inf')
        dp = {}
        m = len(grid)
        n = len(grid[0])

        def minpath(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
           
            if not (i, j) in dp:
                if i == 0:
                    dp[(i, j)] = grid[i][j] + minpath(i, j - 1)
                elif j == 0:
                    dp[(i, j)] = grid[i][j] + minpath(i - 1, j)
                else:
                    dp[(i, j)] = grid[i][j] + min(minpath(i -1, j), minpath(i, j - 1)) 
            return dp[(i, j)]
        return minpath(m-1, n - 1)
