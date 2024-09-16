class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12: return []
        ans = []

        def recur(start, curr):
            if len(curr) > 4: return
            if start == n and len(curr) == 4:
                ans.append('.'.join(curr))
                return

            num = 0
            for i in range(start, min(start + 3, n)):
                num = num * 10 + int(s[i])

                if num > 255: break

                recur(i+1, curr + [str(num)])

                if num == 0: break

        recur(0,[])
        return ans
