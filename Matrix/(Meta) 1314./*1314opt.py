class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        # Calculate prefix sum for each cell in the matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]

        # Calculate block sums for each cell
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m, i + k + 1), min(n, j + k + 1)
                result[i][j] = prefix_sum[r2][c2] - prefix_sum[r2][c1] - prefix_sum[r1][c2] + prefix_sum[r1][c1]

        return result
