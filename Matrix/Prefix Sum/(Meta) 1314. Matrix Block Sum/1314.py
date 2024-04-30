class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        presum = [[0] * (col+1) for _ in range(row+1)]
        for i in range(1,row+1):
            for j in range(1 ,col+1):
                presum[i][j] = mat[i-1][j-1] + presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1]
        for i in range(row):
            for j in range(col):
                ru, rd = max(0, i-k), min(row,i+1+k)
                cl, cr = max(0, j-k), min(col,j+1+k)
                mat[i][j] = presum[rd][cr] - presum[rd][cl] - presum[ru][cr] + presum[ru][cl]

        return mat
