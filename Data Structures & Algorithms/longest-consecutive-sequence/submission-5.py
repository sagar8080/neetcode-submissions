class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        maxstreak = 1
        streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                streak += 1
            else:
                streak = 1
            maxstreak = max(maxstreak, streak)
        
        return maxstreak

        