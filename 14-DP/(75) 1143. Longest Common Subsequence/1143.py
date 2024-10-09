class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # time complexity = O(m*n)
        # space complexity = O(m*n)
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
