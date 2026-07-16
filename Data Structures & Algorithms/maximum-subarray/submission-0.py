class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the current sum to be 0
        currSum = 0
        # The max sum at the start is -infinity
        maxSum = -float('inf')
        # We initialize left pointer to the start of array
        L = 0

        for R in range(len(nums)):
            if currSum < 0:
                currSum = 0
            
            currSum += nums[R]
            maxSum = max(currSum, maxSum)
        return maxSum