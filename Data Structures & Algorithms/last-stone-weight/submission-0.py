import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)
            if x == y:
                continue
            elif x > y or y > x:
                remaining_weight = -1 * abs(x - y)
                heapq.heappush(heap, remaining_weight)
        
        return -1 * heap[0] if len(heap) == 1 else 0