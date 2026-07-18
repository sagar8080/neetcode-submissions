class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort() # nlogn

        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
                
            l = i+1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + nums[i]
                if curr_sum == 0:
                    res.add(tuple([nums[l], nums[r], nums[i]]))
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
        result = [list(x) for x in res]
        return result