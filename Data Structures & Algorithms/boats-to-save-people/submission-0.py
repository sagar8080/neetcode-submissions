import math

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            available_weight = limit - people[r]
            r -= 1
            boats += 1

            if l <=r and limit > available_weight and available_weight >= people[l]:
                l += 1
        
        return boats