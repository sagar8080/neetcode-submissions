import heapq
from collections import defaultdict, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1
        maxheap = [-c for c in counter.values()]
        heapq.heapify(maxheap)
        time = 0
        queue = deque() # store count, idletime
        while maxheap or queue:
            time += 1

            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt != 0:
                    queue.append([cnt, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])
        
        return time



