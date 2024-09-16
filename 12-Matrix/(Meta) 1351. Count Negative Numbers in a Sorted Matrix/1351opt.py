class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        s = 0
        count = 0
        for row in range(rows-1, -1, -1):
            for col in range(s, cols):
                if grid[row][col] < 0:
                    count += cols - col
                    break
                s += 1

        return count
