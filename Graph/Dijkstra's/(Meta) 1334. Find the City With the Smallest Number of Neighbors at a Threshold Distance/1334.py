class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append([w, v])
            adj[v].append([w, u])

        min_count = n
        for u in range(n):
            heap = [[0,u]]
            count = -1
            visited = [False] * n
            while heap:
                w, v = heapq.heappop(heap)
                if count > min_count or w > distanceThreshold: break
                if visited[v]: continue
                visited[v] = True
                count += 1
                for nw, nv in adj[v]:
                    if not visited[nv]:
                        heapq.heappush(heap,[nw+w,nv])

            if count <= min_count:
                ans = u
                min_count = count

        return ans
