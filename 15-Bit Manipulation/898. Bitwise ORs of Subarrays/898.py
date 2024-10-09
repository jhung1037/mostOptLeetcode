class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # time complexity = O(n*log(max(arr))) < O(32*n)
        # space complexity = O(log(max(arr))) < O(32)
        res, curr = set(), set()
        for a in arr:
            curr = {a | c for c in curr} | {a}
            res |= curr
        return len(res)
