
"""
Understand:

Return the area of the largest rectangle that can be formed 

Plan:

Go through each bar:
    let h = height of the current bar:
    let w = 1
    while the height of the next bar is > h:
        w+=1
    while the height of the previous bar > h:
        w
    area = h * w
    maxArea = max(maxArea, area)
return maxArea

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            w, h = 1, heights[i]
            j = i + 1
            while j < len(heights) and heights[j] >= h:
                w+=1
                j+=1
            j = i - 1
            while j >= 0 and heights[j] >= h:
                w+=1
                j-=1
            maxArea = max(maxArea, w * h)
        return maxArea
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                curIndex, curHeight = stack.pop()
                if stack:
                    leftBoundary = stack[-1][0]
                else:
                    leftBoundary = -1
                
                width = i - leftBoundary - 1
                maxArea = max(maxArea, (curHeight * width))
            stack.append((i, h))

        while stack:
            curIndex, curHeight = stack.pop()
            if stack:
                leftBoundary = stack[-1][0]
            else:
                leftBoundary = -1
            width = len(heights) - leftBoundary - 1
            maxArea = max(maxArea, curHeight * width)

        return maxArea

        