class Solution:
    def rob_helper(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[n-1]
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # start at first house to n - 1
        candidate = nums[:n-1]
        amt_0 = self.rob_helper(candidate)

        candidate2 = nums[1:]
        amt_1 = self.rob_helper(candidate2)

        return max(amt_0, amt_1)
