class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        kids = [0] * k
        res = math.inf
        l = len(cookies)

        def dfs(kids, ptr):
            nonlocal res
            if ptr == l:
                mxk = max(kids)
                res = min(res, mxk)
                return

            for i in range(k):
                if (kids[i]+cookies[ptr] >= res
                    or (i>0 and kids[i]==kids[i-1])):
                    continue
                kids[i] += cookies[ptr]
                dfs(kids, ptr + 1)
                kids[i] -= cookies[ptr]

        dfs(kids, 0)
        return res
