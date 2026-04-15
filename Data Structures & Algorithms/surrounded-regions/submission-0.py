class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        q = deque()
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][n - 1] == 'O':
                q.append((i, n - 1))
        
        for j in range(n):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[m - 1][j] == 'O':
                q.append((m - 1, j))

        
        while q:
            ux, uy = q.popleft()
            if board[ux][uy] == '#':
                continue
            board[ux][uy] = '#'

            for k in range(4):
                vx = ux + dx[k]
                vy = uy + dy[k]
                if ((0 <= vx < m) and (0 <= vy < n) and
                    (board[vx][vy] == 'O')) :
                        q.append((vx, vy))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
        

                    
    



        