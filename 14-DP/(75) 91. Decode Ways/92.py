class Solution:
    def numDecodings(self, s: str) -> int:
        # time complexity: O(n)
        # space complexity: O(n)
        cache = {}
        def dfs(st):
            if st.startswith("0"):
                return 0
            
            if len(st) <= 1:
                return 1
            
            if st not in cache:
                one = dfs(st[1:])
                two = 0
                if int(st[:2]) <= 26:
                    two = dfs(st[2:])
                cache[st] = one + two
            return cache[st]

        return dfs(s)
