class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        size = len(grid)
        row_max = [max(r) for r in grid]
        col_max = [max(c) for c in zip(*grid)]

        res = 0
        for i in range(size):
            for j in range(size):
                res += min(row_max[i],col_max[j]) - grid[i][j]

        return res
