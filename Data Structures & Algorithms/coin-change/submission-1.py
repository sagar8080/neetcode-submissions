class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                diff = i - c
                if diff < 0:
                    break
                dp[i] = min(dp[i], dp[diff] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1