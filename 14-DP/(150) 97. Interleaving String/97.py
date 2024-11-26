class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # time complexity = O(m * n)
        # space complexity = O(min(len(s1), len(s2)))
        if len(s1) + len(s2) != len(s3): return False

        if len(s1) < len(s2):
            s1, s2 = s2, s1

        dp = [True]
        
        for j in range(1, len(s2)+1):
            dp.append(dp[j-1] and s2[j-1] == s3[j-1])

        for i in range(1, len(s1)+1):
            dp[0] &= s1[i-1] == s3[i-1]
            for j in range(1, len(s2)+1):
                dp[j] = ((dp[j] and s1[i-1] == s3[i+j-1]) or 
                         (dp[j-1] and s2[j-1] == s3[i+j-1]))

        return dp[-1]
