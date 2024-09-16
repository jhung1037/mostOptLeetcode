class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for i in range(n+1)]
        for u, v, w in edges:
            adj[u].append((w,v))
            adj[v].append((w,u))

        heap = [(0,n)]

        curr_shortest = [math.inf for _ in range(n)] + [0]
        counts = [0 for i in range(n)] + [1]
        visited = [False for i in range(n + 1)]
        while heap:
            d, u = heapq.heappop(heap)
            if u == 1: break
            if visited[u]: continue
            visited[u] = True
            for w, v in adj[u]:
                if not visited[v]:
                    if d+w < curr_shortest[v]:
                        curr_shortest[v] = d+w
                        heapq.heappush(heap, (d+w,v))
                    if curr_shortest[v] > curr_shortest[u]:
                        counts[v] = (counts[v] + counts[u]) % (10 ** 9 + 7)

        return counts[1]
