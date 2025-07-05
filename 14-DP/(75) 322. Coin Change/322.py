class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # time complexity: O(amount * n)
        # space complexity: O(n)
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[amount] if dp[amount] != math.inf else -1
