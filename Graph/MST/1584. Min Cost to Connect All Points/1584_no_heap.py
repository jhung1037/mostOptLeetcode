class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        rest = {i for i in range(1,N)}
        min_cost = [math.inf] * N

        ans = 0

        u = 0
        while rest:
            x1 = points[u][0]
            y1 = points[u][1]
            min_cost_index = -1
            for v in rest:
                x2 = points[v][0]
                y2 = points[v][1]
                d = abs(x1-x2) + abs(y1-y2)
                if d < min_cost[v]:
                    min_cost[v] = d
                if min_cost_index == -1 or min_cost[v] < min_cost[min_cost_index]:
                    min_cost_index = v
            
            u = min_cost_index
            rest.remove(u)
            ans += min_cost[u]

        return ans
