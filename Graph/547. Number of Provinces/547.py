class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [False] * len(isConnected)
        N = len(isConnected)

        def go(city):
            for nei, connected in enumerate(isConnected[city]):
                if nei != city and not visited[nei] and connected:
                    visited[nei] = True
                    go(nei)

        for city in range(N):
            if not visited[city]:
                provinces += 1
                visited[city] = True
                go(city)

        return provinces
