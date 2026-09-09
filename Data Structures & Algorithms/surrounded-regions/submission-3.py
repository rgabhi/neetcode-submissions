class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        def dfs(i, j, vis):
            vis.add((i, j))
            board[i][j] = '#'
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in vis:
                        if board[x][y] == 'O':
                            dfs(x, y, vis)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0, set())
            if board[i][n -1] == 'O':
                dfs(i, n - 1, set())
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j, set())
            if board[m-1][j] == 'O':
                dfs(m-1, j, set())
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
            
        