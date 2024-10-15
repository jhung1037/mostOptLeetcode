class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # time complexity: O(len(n) * len(wordDict))
        # space complexity: O((len(s)))
        '''
        Checking char by char will take O(n*n).
        Since len(wordDict) <= 20. We will check every word in wordDict for O(n*m)
        '''
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break

        return dp[0]
