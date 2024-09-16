class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, t in times:
            adj[u].append((t, v))

        heap = [(0, k)]
        min_d = [math.inf] * (n+1)
        min_d[k] = 0
        while heap:
            t, u = heapq.heappop(heap)
            if min_d[u] < t: continue
            for nt, v in adj[u]:
                if min_d[v] > (md:=nt+t):
                    min_d[v] = md
                    heapq.heappush(heap,(md, v))

        res = max(min_d[1:])
        return res if res != math.inf else -1
