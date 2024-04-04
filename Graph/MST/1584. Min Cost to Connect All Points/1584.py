class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        rest = {i for i in range(N)}
        shortest_d = [math.inf] * N
        heap = [[0,0]]
        ans = 0
        while rest:
            d, u = heapq.heappop(heap)
            if u not in rest: continue
            rest.remove(u)
            ans += d
            x1, y1 = points[u]
            for v in rest:
                x2, y2 = points[v]
                d = abs(x1 - x2) + abs(y1 - y2)
                if d < shortest_d[v]:
                    shortest_d[v] = d
                    heapq.heappush(heap, [d, v])
        
        return ans
