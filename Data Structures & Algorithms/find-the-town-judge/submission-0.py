class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = defaultdict(int)

        for src, dst in trust:
            degrees[src] -= 1
            degrees[dst] += 1
        
        for i in range(1, n+1):
            if degrees[i] == n-1:
                return i
        
        return -1