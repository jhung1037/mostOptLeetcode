class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        empty_line = '.' * n
        board = [empty_line for _ in range(n)]
        taken_col = [False] * n
        taken_pos_diag = [False] * (2*n)
        taken_neg_diag = [False] * (2*n)

        res = []
        def dfs(row):
            if row == n:
                res.append(board.copy())
                return
            for col in range(n):
                if taken_col[col] or taken_pos_diag[row+col-n] or taken_neg_diag[row-col+n]: continue
                taken_col[col] = taken_pos_diag[row+col-n] = taken_neg_diag[row-col+n] = True

                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                dfs(row+1)

                board[row] = empty_line
                taken_col[col] = taken_pos_diag[row+col-n] = taken_neg_diag[row-col+n] = False
                
        dfs(0)
        return res
