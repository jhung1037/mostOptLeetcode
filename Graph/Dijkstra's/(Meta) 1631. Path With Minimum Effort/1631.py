class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        end = (row-1, col-1)
        heap = [[0,0,0]]
        visited = [[False for _ in range(col)] for _ in range(row)]
        
        res = 0
        while heap:
            abd, ur, uc = heapq.heappop(heap)
            res = max(res, abd)
            if (ur, uc) == end: return res
            visited[ur][uc] = True
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                vr, vc = ur+dr, uc+dc
                if 0 <= vr < row and 0 <= vc < col and not visited[vr][vc]:
                    heapq.heappush(heap,[abs(heights[ur][uc]-heights[vr][vc]), vr, vc])

        return -1
