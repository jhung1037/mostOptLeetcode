class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        n = len(roads) + 1

        graph = {i : [] for i in range(n)}
        edge = [0] * n
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            edge[u] += 1
            edge[v] += 1

        check = []
        for i in range(n):
            if edge[i] == 1:
                check.append(i)

        ppl  = [1] * n
        ttl = 0
        while check:
            node = check.pop()
            if node == 0: continue
            ttl += math.ceil(ppl[node] / seats)
            des = graph[node][0]
            graph[des].remove(node)
            ppl[des] += ppl[node]
            edge[des] -= 1
            if edge[des] == 1:
                check.append(des)

        return ttl
