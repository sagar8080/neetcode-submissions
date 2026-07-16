import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        res = []
        heap = []
        
        for n in nums:
            counts[n] += 1

        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res