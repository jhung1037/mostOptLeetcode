class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # time complexity = O(n) ~ O(n^2) => AVG. O(nlogn)
        # space complexity = O(L)

        self.res = 0
        def dnc(l, r, k):
            if r - l < self.res or r - l < k:
                return
            counter = Counter(s[l:r])
            invalid = set([c for c in counter if counter[c] < k])
            if not invalid:
                self.res = max(self.res, r - l)
                return

            start = l
            for i in range(l, r):
                if s[i] in invalid:
                    dnc(start, i, k)
                    start = i + 1
            dnc(start, r, k)  # check the last segment

        dnc(0, len(s), k)
        return self.res
