class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(l, r):
            if l > r:
                cache[(l,r)] = max(l,r)
                return 0
            elif (l, r) in cache:
                return cache[(l,r)]
            
            even = True if (l-r)%2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            cache[(l,r)] = max(dfs(l+1,r) + left,
                               dfs(l,r-1) + right)
            return cache[(l,r)]

        return dfs(0, len(piles)-1)
