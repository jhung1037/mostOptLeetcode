class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        check = []
        for i in range(n):
            if indegree[i] == 0:
                check.append(i)

        res = [set() for _ in range(n)]
        while check:
            root = check.pop()
            for child in adj[root]:
                res[child].add(root)
                res[child].update(res[root])
                indegree[child] -= 1
                if indegree[child] == 0:
                    check.append(child)

        return list(map(sorted, res))