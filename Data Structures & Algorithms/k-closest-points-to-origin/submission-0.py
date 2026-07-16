class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (-dist, [x, y]))
        
        points = heapq.nlargest(k, heap)
        print(points)
        res = [point for dist, point in points]
        return res
        