class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        ans = 0
        def check_island(r, c):
            for dr, dc in (-1, 0), (0, -1), (0, 1), (1, 0):
                if 0 <= r+dr < rows and 0 <= c+dc < cols and grid[r+dr][c+dc] == '1':
                    grid[r+dr][c+dc] = '0'
                    check_island(r+dr, c+dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    ans+=1
                    grid[row][col] = '0'
                    check_island(row, col)

        return ans
