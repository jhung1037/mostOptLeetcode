from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        link = defaultdict(list)
        for u, v in edges:
            link[u].append(v)
            link[v].append(u)
        visited = [False] * n
        queue = deque()
        queue.append(source)
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            if not visited[node]:
                visited[node] = True
                for neighbor in link[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        
        return False
