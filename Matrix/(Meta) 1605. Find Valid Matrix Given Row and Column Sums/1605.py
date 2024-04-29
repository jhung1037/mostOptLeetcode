class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rs, cs = len(rowSum), len(colSum)
        grid = [[0] * cs for _ in range(rs)]
        r_heap = []
        c_heap = []
        for i in range(rs):
            heapq.heappush(r_heap, (rowSum[i], i))

        for i in range(cs):
            heapq.heappush(c_heap, (colSum[i], i))

        while r_heap and c_heap:
            r, ri = heapq.heappop(r_heap)
            c, ci = heapq.heappop(c_heap)
            if r <= c:
                grid[ri][ci] = r
                if r != c:
                    heapq.heappush(c_heap, (c-r, ci))
            else:
                grid[ri][ci] = c
                heapq.heappush(r_heap, (r-c, ri))

        return grid
