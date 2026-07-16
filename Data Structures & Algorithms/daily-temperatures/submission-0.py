class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp, idx
        n = len(temperatures)
        res = [0] * n

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, i = stack.pop()
                res[i] = idx - i
            stack.append((temp, idx))
        
        return res

