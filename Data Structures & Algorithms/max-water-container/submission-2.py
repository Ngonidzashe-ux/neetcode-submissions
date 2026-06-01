"""
Understand:
- Have two pointers, l, r at the end of the arrays
- Have a maxWater variable to keep track of the max
- Calculate the current area by taking the min height of the two bars and multiply by the width, diff between their indices
- Update maxWater
- Shift the pointers and do that while l<r
"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = 0
        while l < r:
            curArea = min(heights[l], heights[r]) * (r - l)
            maxWater = max(curArea, maxWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
        