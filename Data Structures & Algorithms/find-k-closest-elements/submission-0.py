import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapq.heapify(heap)

        for element in arr:
            target = abs(element - x)
            heapq.heappush(heap, (-target, -element))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [-element for target, element in heap]
        res.sort()
        return res        