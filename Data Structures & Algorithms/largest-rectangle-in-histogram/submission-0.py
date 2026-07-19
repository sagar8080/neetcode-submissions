class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # store index, height
        n = len(heights)
        for curr_idx, height in enumerate(heights):
            start = curr_idx

            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                maxArea = max(maxArea, h * (curr_idx - i))
                start = i
            
            stack.append((start, height))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))
        
        return maxArea