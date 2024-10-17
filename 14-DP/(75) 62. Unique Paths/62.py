class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # time complexity: O(m * n)
        # space complexity: O(n)
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]
