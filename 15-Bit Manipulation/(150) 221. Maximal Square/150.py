class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # time complexity: O(m * n)
        # space complexity: O(1)
        m = 0
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    matrix[i][j] = 1
                    if i > 0 and j > 0:
                        matrix[i][j] = 1 + min(matrix[i-1][j],
                                            matrix[i][j-1],
                                            matrix[i-1][j-1])
                    m = max(m, matrix[i][j])
                else:
                    matrix[i][j] = 0

        return m * m