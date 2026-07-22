import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            val = heapq.heappop(self.heap)
            print(val)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            val = heapq.heappop(self.heap)
            print(val)
        print(self.heap)
        return self.heap[0]