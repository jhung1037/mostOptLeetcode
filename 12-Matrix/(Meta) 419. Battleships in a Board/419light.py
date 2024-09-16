class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row, col = len(board), len(board[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    if (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                        count += 1
        return count