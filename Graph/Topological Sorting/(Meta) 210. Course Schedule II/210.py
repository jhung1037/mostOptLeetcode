class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        check = []
        for i in range(numCourses):
            if indegree[i] == 0:
                check.append(i)
        if check == []: return []

        res = []
        while check:
            remove = check.pop()
            res.append(remove)
            for child in adj[remove]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    check.append(child)

        return res if len(res) == numCourses else []
