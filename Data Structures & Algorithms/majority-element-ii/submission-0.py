from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = int(n/3)
        count = defaultdict(int)
        res = set()

        for n in nums:
            count[n] += 1

            if count[n] > threshold and n not in res:
                res.add(n)
        
        return list(res)

