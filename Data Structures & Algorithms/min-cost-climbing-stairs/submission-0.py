class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # One can start at 0, 1 index
        n = len(cost)
        if cost and n <= 2:
            return cost[n]

        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 0

        for i in range(2, n+1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            print(i, dp[i])
        
        return dp[n]
        