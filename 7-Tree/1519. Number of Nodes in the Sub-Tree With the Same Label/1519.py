from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        label_count = defaultdict(int)
        ans = [0] * n
        def dfs(node, parent):
            label = labels[node]
            ancestor = label_count[label]

            label_count[label] += 1
            for v in graph[node]:
                if v == parent: continue
                dfs(v, node)
            subtree = label_count[label]
            ans[node] = subtree - ancestor

        dfs(0, -1)
        return ans
