class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        N = len(grid[0])

        def bins(lis):
            l, h = 0, N-1
            while l <= h:
                m = (l+h) // 2
                if lis[m] < 0 and lis[m-1] > 0:
                    return m
                if lis[m] < 0:
                    h = m - 1
                else:
                    l = m + 1
            return l

        c = 0
        for row in grid:
            c += N - bins(row)

        return c
