class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        row, col = len(matrix), len(matrix[0])
        values = []
        col_xor = [0] * col
        res = []
        for i in range(row):
            row_xor = 0
            for j in range(col):
                col_xor[j] ^= matrix[i][j]
                row_xor ^= col_xor[j]
                res.append(row_xor)
        return sorted(res,reverse = True)[k-1]
        