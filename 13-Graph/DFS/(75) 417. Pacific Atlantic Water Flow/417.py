class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # time complexity: O(m * n)
        # space complexity: O(m * n)
        m, n = len(heights), len(heights[0])
        pc, al = set(), set()

        def dfs(r, c, ocean):
            ocean.add((r, c))
            for row, col in (r-1, c),(r, c-1),(r, c+1),(r+1, c):
                if (row, col) in ocean: continue
                if (0 <= row < m and 0 <= col < n and
                    heights[row][col] >= heights[r][c]):
                    dfs(row, col, ocean)

        for i in range(n):
            dfs(0, i, pc)
            dfs(m-1, i, al)
        
        for i in range(m):
            dfs(i, 0, pc)
            dfs(i, n-1, al)

        return list(pc & al)
