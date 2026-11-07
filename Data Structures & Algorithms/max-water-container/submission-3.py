"""
Approaches

Move the bar that is smaller of the two current ones



"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while (l < r):
            currentArea = (r - l) * min(heights[l], heights[r])
            maxArea = max(currentArea, maxArea)
            if (heights[l] <= heights[r]):
                l+=1
            else:
                r-=1
        return maxArea