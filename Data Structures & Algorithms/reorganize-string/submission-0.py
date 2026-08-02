from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxheap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(maxheap)

        res = ""
        prev = None

        while maxheap or prev:
            if prev and not maxheap:
                return ""
            
            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            
            if cnt != 0:
                prev = (cnt, char)
        return res