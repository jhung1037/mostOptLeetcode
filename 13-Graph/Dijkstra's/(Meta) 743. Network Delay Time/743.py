class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, t in times:
            adj[u].append((t, v))

        heap = [(0, k)]
        visited = set()
        while len(visited) != n and heap:
            t, u = heapq.heappop(heap)
            res = t
            if u in visited: continue
            visited.add(u)
            for nt, v in adj[u]:
                if v in visited: continue
                heapq.heappush(heap,(nt+t, v))

        return res if len(visited) == n else -1
