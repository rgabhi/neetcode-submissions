class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        minPaths = [[-1 for j in range(n)] for i in range(m)]

        minPaths[0][0] = grid[0][0]

        for i in range(1, m):
            minPaths[i][0] = minPaths[i - 1][0] + grid[i][0]
        for j in range(1, n):
            minPaths[0][j] = minPaths[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                minPaths[i][j] = grid[i][j] + min(minPaths[i-1][j], minPaths[i][j-1])
        return minPaths[m - 1][n - 1]
                


        