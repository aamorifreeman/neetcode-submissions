"""
area = 

r = len(heights) - 1
l = 0
max_area = 0
loop through my heights:
    calculate area with smaller height
        min_height = min(heights[r], heights[l])
        length = r - l
        area = length * min_height
    
    if heights[l] < heights[r]:
        l += 1
    else:
        r -= 1


"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        r = len(heights) - 1
        l = 0
        max_area = 0
        while l < r:
            min_height = min(heights[r], heights[l])
            length = r - l
            area = length * min_height
            max_area = max(max_area, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area