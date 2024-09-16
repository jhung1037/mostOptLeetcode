class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        res = []
        sr, sc = start
        check = [(grid[sr][sc], sr, sc)]
        while check:
            newcheck = []
            for val, row, col in check:
                if not grid[row][col]: continue
                grid[row][col] = 0
                if pricing[0] <= val <= pricing[1]:
                    res.append([row, col])
                    if len(res) == k: return res
                for a, b in [(1,0),(0,1),(0,-1),(-1,0)]:
                    r = row + a
                    c = col + b
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]:
                        newcheck.append((grid[r][c], r, c))
            check = sorted(newcheck)

        return res
