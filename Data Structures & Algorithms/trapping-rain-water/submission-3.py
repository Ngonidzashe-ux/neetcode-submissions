
"""
Understand:
1. Find the all the independent containers that can be formed by 2 bars
2. Return the total amount of water that can be contained by those containers
Edge cases: if you have one bar or two bars, then water is 0

Plan:
start out with the first two bars. so left and right.
move the right bar
ask yourself if the bar you moved from is smaller than current right.
if smaller than current right, then check if smaller than current left in whcih case that is a container. current container. 
Then move the right bar forward, if bar is bigger, then thats an extension of a conatiner but if not, let the left move to previous right.


Initialise l=0, r=1
if these two bars are a container:
    record the current water 
else:
    if right bar >= left bar:
        leftbar = rightbar
        rightbar++
        add the curretn water to the total 
        set currentwater to 0 since its now trying to find new container
        this is so that we try to find anotther container
    else:
        rightbar++

return total amount


checkContainer():
we have two boundaries.
container is when the two bars are bigger than the bars inside
for each bar in the boundary, it can hold water that is min(leftbar, rightbar) - its height

The problem:
Containers can overlap, so summing the water held by each valid container can double-count water above the same bar.

New plan.
For each bar, find the tallest bars on the right and left of it, that could allow it to hold the maximum water possible



"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        
        for i in range(len(height) -2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        
        total = 0
        for i in range(len(height)):
            total += max(0, (min(leftMax[i], rightMax[i]) - height[i]))
        return total


                

        