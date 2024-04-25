class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = [[] for _ in range(n)]
        for i  in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adj[u].append([p,v])
            adj[v].append([p,u])

        visited = [False] * n
        heap = [[-1, start_node]]
        while heap:
            p, u = heapq.heappop(heap)
            p = -p
            if u == end_node: return p
            if visited[u]: continue
            visited[u] = True
            for np, v in adj[u]:
                if visited[v]: continue
                heapq.heappush(heap, [-(p * np), v])

        return 0
