class Solution:
    def dfs(self, graph, src, parent, visited, time, disc, low, conn):
        visited[src] = True

        disc[src] = time
        low[src] = time

        for nbr in graph[src]:
            if parent==nbr:
                continue
            elif visited[nbr]:
                low[src] = min(low[src],disc[nbr])
            else:
                self.dfs(graph,nbr,src,visited,time+1,disc,low,conn)
                low[src] = min(low[src],low[nbr])

                if low[nbr]>disc[src]:
                    conn.append((src,nbr))

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for vtx in range(n)]

        conn = []

        for con in connections:
            vtx1 = con[0]
            vtx2 = con[1]

            graph[vtx1].append(vtx2)
            graph[vtx2].append(vtx1)
        
        disc = [0]*n
        low = [0]*n
        
        self.dfs(graph,0,-1,[False]*n,0,disc,low,conn)

        return conn