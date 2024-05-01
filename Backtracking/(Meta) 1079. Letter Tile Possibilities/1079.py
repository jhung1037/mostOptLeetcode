class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        record = collections.defaultdict(int)
        for t in tiles:
            record[t] += 1
            
        def dfs(record):
            s = 0
            for k in record:
                if record[k]:
                    record[k] -= 1
                    s += dfs(record) + 1
                    record[k] += 1
            return s

        return dfs(record)
