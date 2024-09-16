class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        diag = 0
        for r in range(diag, len(matrix)):
            for c in range(diag, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            matrix[r] = matrix[r][::-1]
            diag += 1
