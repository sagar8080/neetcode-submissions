class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0
        while l < r:
            base = r - l
            if heights[r] > heights[l]:
                curr_water = base * min(heights[r], heights[l])
                max_water = max(max_water, curr_water)
                l += 1
            else:
                curr_water = base * min(heights[r], heights[l])
                max_water = max(max_water, curr_water)
                r -= 1
        return max_water