class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row(row):
            st = set()
            for j in range(9):
                if board[row][j] == '.':
                    continue
                if board[row][j] in st:
                    return False
                else:
                    st.add(board[row][j])
            return True
        def is_valid_col(col):
            st = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in st:
                    return False
                else:
                    st.add(board[i][col])
            return True
        def is_valid_box(row, col):
            st = set()
            for i in range(3):
                for j in range(3):
                    if board[(row//3)*3 + i][(col//3)*3 + j] == '.':
                        continue
                    if board[(row//3)*3 + i][(col//3)*3 + j] in st:
                        return False
                    else:
                        st.add(board[(row//3)*3 + i][(col//3)*3 + j])
            return True
        ans = True
        for i in range(9):
            ans = ans and is_valid_row(i)
            if not ans:
                return False
        for j in range(9):
            ans = ans and is_valid_col(j)
            if not ans:
                return False
        for i in range(9):
            for j in range(9):
                ans = ans and is_valid_box(i, j)
                if not ans:
                    return False
        return ans

        