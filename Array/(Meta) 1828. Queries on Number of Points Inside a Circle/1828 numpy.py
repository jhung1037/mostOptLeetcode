import numpy as np
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points = np.array(points)
        return [
            np.sum((x-points[:,0])**2+(y-points[:,1])**2 <= r**2)
            for i, (x, y, r) in enumerate(queries)
            ]