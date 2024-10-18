"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        visited = {}
        def dfs(n):
            if n.val in visited:
                return visited[n.val]

            clone = Node(n.val)
            visited[n.val] = clone
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone
        
        return dfs(node)
