class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row, col = len(board), len(board[0])
        count = 0
        i = 0
        while i < row:
            j = 0
            while j < col:
                if board[i][j] == 'X':
                    count += 1
                    k = i
                    while j+1 < col and board[i][j+1] == 'X':
                        j += 1
                    while k+1 < row and board[k+1][j] == 'X':
                        board[k+1][j] = '.'
                        k += 1
                j += 1
            i += 1

        return count
