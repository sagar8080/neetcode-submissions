class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minWindow = float("inf")

        l, r = 0, 0
        
        currSum = 0

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                windowLen = r - l + 1
                minWindow = min(minWindow, windowLen)
                currSum -= nums[l]
                l += 1
        
        return minWindow if minWindow != float("inf") else 0