class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        reachable = {0}
        reorder = 0
        stack = []
        while connections:
            u, v = connections.pop()
            if v in reachable:
                reachable.add(u)
            elif u in reachable:
                reachable.add(v)
                reorder += 1
            else:
                stack.append([u, v])
            if not connections:
                connections = stack
                stack = []
        return reorder
