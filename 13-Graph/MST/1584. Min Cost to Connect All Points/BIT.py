class BIT:
    def __init__(self, n: int):
        self.nums = [(inf, -1) for _ in range(n + 1)]
        self.n = n
    
    def find(self, max_rank: int):
        min_dist = inf
        res = -1
        while max_rank:
            curr_dist, curr_id = self.nums[max_rank]
            if curr_dist < min_dist:
                min_dist = curr_dist
                res = curr_id
            max_rank -= max_rank & -max_rank
        return res

    def update(self, rank: int, dist: int, point_id: int):
        while rank <= self.n:
            curr_dist, _ = self.nums[rank]
            if dist < curr_dist:
                self.nums[rank] = dist, point_id
            rank += rank & -rank

class UnionFind:
    def __init__(self):
        self.root_lookup = {}
        self.rank_lookup = defaultdict(lambda: 1)
    
    def find(self, num: int):
        root = self.root_lookup.setdefault(num, num)
        path = []
        while root != self.root_lookup[root]:
            path.append(root)
            root = self.root_lookup[root]
        for node in path:
            self.root_lookup[node] = root
        return root

    def union(self, num1: int, num2: int):
        root1, root2 = self.find(num1), self.find(num2)
        if root1 == root2:
            return False
        rank1, rank2 = self.rank_lookup[root1], self.rank_lookup[root2]
        if rank1 < rank2:
            root1, root2 = root2, root1
            rank2 = rank1
        self.root_lookup[root2] = root1
        self.rank_lookup[root1] += rank2
        return True

def build_graph(points: List[List[int]]):
    n = len(points)
    edges = []
    def intercept(point_id: int):
        x, y = points[point_id]
        return x - y, -x

    for iteration in range(4):
        if iteration == 1 or iteration == 3:
            for point in points:
                point.reverse()
        elif iteration == 2:
            for point in points:
                point[0] = -point[0]
        

        sorted_by_x = sorted(enumerate(points), key=itemgetter(1), reverse=True)
        sorted_by_intercept = sorted(range(n), key = intercept)
        rank_lookup = [0] * n
        for rank, point_id in enumerate(sorted_by_intercept, 1):
            rank_lookup[point_id] = rank
        bit = BIT(n)
        for point_id, (x, y) in sorted_by_x:
            rank = rank_lookup[point_id]
            sw_most_id = bit.find(rank)
            if sw_most_id != -1:
                sw_x, sw_y = points[sw_most_id]
                dist = abs(x - sw_x) + abs(y - sw_y)
                edges.append((dist, point_id, sw_most_id))
            bit.update(rank, x + y, point_id)
    return edges

def kruskal(edges: List[Tuple[int, int, int]]):
    edges = list(set(edges))
    edges.sort()
    uf = UnionFind()
    return sum(cost for cost, a, b in edges if uf.union(a, b))

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = build_graph(points)
        return kruskal(graph)