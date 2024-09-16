class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], t: int) -> int:
        routes = defaultdict(list)
        for src, dst, weight in edges:
            if weight <= t:
                routes[src].append((dst, weight))
                routes[dst].append((src, weight))

        def dijkstra(i):
            v = 0
            dist = [inf] * n
            dist[i] = 0

            heap = []
            heappush(heap, (0, i))

            while heap:
                s, i = heappop(heap)
                if v & (1 << (i + 1)):
                    continue

                v += 1 << (i + 1)
                for j, w in routes[i]:
                    if dist[j] > dist[i] + w:
                        dist[j] = dist[i] + w
                        heappush(heap, (dist[j], j))

            return sum(1 for x in dist if x <= t)

        k, mx = -1, inf
        for i in range(n):
            r = dijkstra(i)
            if r <= mx and i > k:
                k, mx = i, r
        return k
