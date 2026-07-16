import math

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we will use 2 pointers
        # left, right pointer -> 0, last element
        # area to be maximum: length * height
        # height is the dynamic factor: 
        # start with l=0, r = len
        # if height[r] > height[l]: l++ : min(heights) * (r-l)
        # if height[r] < heigh[l]: r-- : min(heights) * (r-l)

        l, r = 0, len(heights) - 1
        max_area = -1
        while l < r:
            left_height = heights[l]
            right_height = heights[r]

            if right_height >= left_height:
                area = (r-l) * left_height
                max_area = max(area, max_area)
                l += 1
            
            if right_height < left_height:
                area = (r-l) * right_height
                max_area = max(area, max_area)
                r -= 1

        return max_area

        