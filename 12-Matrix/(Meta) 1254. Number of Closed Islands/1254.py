class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def is_island(x, y):
            island = True
            for a, b in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
                if grid[a][b]: continue
                grid[a][b] = 1
                if 0 < a < row-1 and 0 < b < col-1:
                    if not is_island(a, b):
                        island = False
                else:
                    island = False
            return island

        row, col = len(grid), len(grid[0])
        count = 0
        for i in range(1,row-1):
            for j in range(1,col-1):
                if grid[i][j]: continue
                grid[i][j] = 1
                if is_island(i,j): count += 1
        return count
