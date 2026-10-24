class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l =len(word)
        vis = set()
        def check(i, j, idx):
           
            if idx == l:
                return True
            if  not((0 <= i < m) and (0 <= j < n)) or (i, j) in vis or word[idx] != board[i][j]:
                return False
            vis.add((i, j))
            ans = check(i + 1, j, idx + 1) or check(i - 1, j, idx + 1) or\
                check(i, j - 1, idx + 1) or check(i, j + 1, idx + 1)
            vis.remove((i, j))
            return ans

        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False
               
         
                
            


        