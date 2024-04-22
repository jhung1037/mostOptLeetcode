class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i : [] for i in range(n+1)}
        for time in times:
            u, v, t = time
            adj[u].append([t,v])

        heap = []
        visited = set()
        visited.add(k)
        for child in adj[k]:
            heapq.heappush(heap,child)

        res = 0
        while len(visited) != n and heap:
            t, v = heapq.heappop(heap)
            res = t
            if v in visited: continue
            visited.add(v)
            for child in adj[v]:
                ct, cv = child
                if cv in visited: continue
                heapq.heappush(heap,[ct+t, cv])
    
        return res if len(visited) == n else -1
