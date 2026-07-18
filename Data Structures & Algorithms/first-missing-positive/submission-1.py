class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_num = max(nums)

        for i in range(1, max_num):
            if i not in unique_nums:
                return i
        
        return max(1, max_num + 1)
