from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if len(trust) < n - 1:
        #     return -1

        arr = defaultdict(int)

        for src, dest in trust:
            arr[src] -= 1
            arr[dest] += 1
        
        for i in range(1, n+1):
            if arr[i] == n - 1:
                return i
        
        return -1