import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = [] # store (processingTime, index)
        pending = [] # store (enqueueTime, processingTime, index)
        res = []
        for i, (eqt, prt) in enumerate(tasks):
            heapq.heappush(pending, (eqt, prt, i))
        
        time = 0

        while pending or available:
            while pending and pending[0][0] <= time:
                enqueueT, processingT, idx = heapq.heappop(pending)
                heapq.heappush(available, (processingT, idx))
            
            if not available:
                time = pending[0][0]
                continue
            
            processingT, idx = heapq.heappop(available)
            time += processingT
            res.append(idx)

        return res