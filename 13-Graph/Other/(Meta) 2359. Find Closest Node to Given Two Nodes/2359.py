class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1
        check = [(node1, 1), (node2, 2)]
        group = [0] * len(edges)
        res = math.inf
        flag = False
        while check:
            nxt = []
            for node, gp in check:
                if group[node] == 0:
                    group[node] = gp
                    if edges[node] != -1:
                        nxt.append((edges[node], gp))
                elif group[node] != gp:
                    flag = True
                    res = min(res, node)

            if flag: return res
            check = nxt

        return -1
