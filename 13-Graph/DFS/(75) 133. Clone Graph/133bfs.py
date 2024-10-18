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
        # time complexity: O(n) = O(E+V)
        # space complexity: O(n)
        if not node: return None

        q = collections.deque([node])
        visited = {node.val: Node(node.val)}

        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei.val not in visited:
                    visited[nei.val] = Node(nei.val)
                    q.append(nei)
                visited[n.val].neighbors.append(visited[nei.val])
                
        return visited[node.val]
