import math

class Solution:
    def feasible(self, piles, hours, speed):
        if sum([math.ceil(i / speed) for i in piles]) <= hours:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        l, r = 1, max_speed

        while l < r:
            mid = (l + r) // 2
            if self.feasible(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        