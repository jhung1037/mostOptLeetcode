class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append([v,w])

        heap = [[0,0,src]]
        min_c = [math.inf] * n
        while heap:
            w, c, u = heapq.heappop(heap)
            if u == dst: return w
            if c > k or c >= min_c[u]: continue
            min_c[u] = c
            for v, nw in graph[u]:
                heapq.heappush(heap,[w+nw, c+1, v])
        
        return -1
