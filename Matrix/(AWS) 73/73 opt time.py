class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        sub = [0] * len(matrix[0])
        hp = set()
        for r, row in enumerate(matrix):
            find = False
            for c, col in enumerate(row):
                if col == 0:
                    hp.add(c)
                    find = True
            if find:
                matrix[r] = sub
        for c in hp:
            for i in range(len(matrix)):
                matrix[i][c] = 0
