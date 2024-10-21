class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time complexity: O(E + V)
        # space complexity: O(E + V)
        adj = {i : set() for i in range(numCourses)}
        indegree = [0] * numCourses
        for prerequisite in prerequisites:
            u, v = prerequisite
            adj[u].add(v)
            indegree[v] += 1
        
        visited = set()
        check = []
        for u, d in enumerate(indegree):
            if d == 0:
                check.append(u)
        
        while check:
            root = check.pop()
            visited.add(root)
            for v in adj[root]:
                if v in visited: return False
                indegree[v] -= 1
                if indegree[v] == 0:
                    check.append(v)

        return True if len(visited) == numCourses else False