class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        check = set()
        ttl = 0
        for i,row in enumerate(grid):
            c = sum(row)
            ttl += c
            if c == 1:
                check.add(row.index(1))

        res = 0
        for i, col in enumerate(zip(*grid)):
            if sum(col) == 1:
                if i in check:
                    res += 1
        return ttl - res
