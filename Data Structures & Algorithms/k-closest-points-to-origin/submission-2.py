import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = [] # store tuple (distance_from_origin, (points))
        # min heap
        heapq.heapify(heap)
        for i in range(len(points)):
            xi, yi = points[i]
            dist = math.sqrt(xi ** 2 + yi ** 2)
            heapq.heappush(heap, (dist, (xi, yi)))
        i = 0
        while i < k:
            x, y = heapq.heappop(heap)[1]
            res.append([x, y])
            i += 1

        return res