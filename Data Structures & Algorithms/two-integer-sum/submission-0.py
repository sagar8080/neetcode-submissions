class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = dict()
        
        # store the index of the nums
        for idx, num in enumerate(nums):
            complement_dict[num] = idx

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                if complement_dict[complement] != idx:
                    return [idx, complement_dict[complement]]