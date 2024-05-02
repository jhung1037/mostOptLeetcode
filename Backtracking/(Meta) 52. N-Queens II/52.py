class Solution:
    def totalNQueens(self, n: int) -> int:
        if n <= 3: return 1 if n == 1 else 0

        avl_col = [True] * n
        avl_pos = [True] * n * 2
        avl_neg = [True] * n * 2

        res = [0]
        def dfs(row):
            if row == n:
                res[0] += 1
                return

            for col in range(n) if row or (n%2) else range(n//2):
                if avl_col[col] and avl_pos[row+col-n] and avl_neg[row-col+n]:
                    avl_col[col] = avl_pos[row+col-n] = avl_neg[row-col+n] = False
                    dfs(row+1)
                    avl_col[col] = avl_pos[row+col-n] = avl_neg[row-col+n] = True
        dfs(0)
        return res[0] if n % 2 else res[0] * 2
