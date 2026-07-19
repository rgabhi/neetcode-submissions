class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])
        self.pre = [[0]*(self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            prefix = 0
            for j in range(self.n):
                prefix += self.matrix[i][j]
                self.pre[i + 1][j + 1] = prefix + self.pre[i][j + 1]
       
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r2, c2 = row2 + 1, col2 + 1
        r1, c1 = row1 + 1, col1 + 1
        br = self.pre[r2][c2]
        above = self.pre[r1 - 1][c2]
        left = self.pre[r2][c1 - 1]
        tr = self.pre[r1 -1][c1 - 1]
        return br - above - left + tr

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)