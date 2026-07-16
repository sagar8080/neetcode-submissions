from math import ceil

class Solution:
    def feasible(self, bananas, h, h_max):
        t = sum([ceil(i / h) for i in bananas])
        return t <= h_max
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r) // 2
            time_taken = 0
            if self.feasible(piles, mid, h):       
                r = mid
            else:
                l = mid + 1
        return l


        
        