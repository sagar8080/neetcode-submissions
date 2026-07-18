class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_sum = 0
        prefix_map = {0: 1}

        for i in range(len(nums)):
            current_sum += nums[i]
            diff = current_sum - k
            res += prefix_map.get(diff, 0)
            prefix_map[current_sum] = 1 + prefix_map.get(current_sum, 0)
        
        return res