class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = [False] * n
        seen[source] = True
        thorough = False
        while not (thorough or seen[destination]):
            thorough = True
            for u, v in edges:
                if seen[u] ^ seen[v]:
                    seen[u] = seen[v] = True
                    if seen[destination]: return True
                    thorough = False
        return seen[destination]