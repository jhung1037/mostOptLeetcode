class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time complexity: O(E + V)
        # space complexity: O(E + V) = adjacency list O(E) +  recursion stack O(V)
        adj = collections.defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)

        def check_loop(pre):
            if pre not in adj:
                return False
            visited.add(pre)
            for crs in adj[pre]:
                if crs in visited:
                    return True
                if check_loop(crs):
                    return True
            adj[pre] = []
            visited.remove(pre)
            return False

        visited = set()
        for pre in adj:
            if check_loop(pre):
                return False
        return True
