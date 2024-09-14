class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hmap = set()
        def dfs(r, c, i):
            if i == len(word): return True

            if (0 > r or r >= len(board)
                or 0 > c or c >= len(board[0])
                or board[r][c] != word[i]
                or (r, c) in hmap):
                return False

            hmap.add((r,c))
            res = (dfs(r-1, c, i+1)
                   or dfs(r, c-1, i+1)
                   or dfs(r, c+1, i+1)
                   or dfs(r+1, c, i+1))
            hmap.discard((r,c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
