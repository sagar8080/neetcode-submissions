import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        # initialize a heap
        heap = []

        for val, count in counts.items():
            heapq.heappush(heap, (count, val))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]

       