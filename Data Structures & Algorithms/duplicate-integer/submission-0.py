class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        xset = set()

        for n in nums:
            if n in xset:
                return True
            xset.add(n)
        
        return False

        