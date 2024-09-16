class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        res = [""] * len(arr)
        for i, a in enumerate(arr):
            check = ','.join(arr[:i]+arr[i+1:])
            for l in range(1,len(a)+1):
                poss = []
                for e in range(1, len(a)+1):
                    sub = a[e-l:e]
                    if sub not in check:
                        poss.append(sub)
                if poss:
                    res[i] = min(poss)
                    break
        return res
