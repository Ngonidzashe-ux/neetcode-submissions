"""
Understand:
Given a temperatures array where temperatures[i] is the temp of the ith day, return the number of days before the next hotter day
Output: List[int], same as input
Edge cases: Empty array, one element, the same element multiple times, then mix of positive and negative temperatures

Match:
No match it does not seem right now

Plan:
Brute Force:
For temp in temperatures.
    Search on the right for a temp strictly higher

Smarter way is to keep a monotonic stack
if not temperatures:
    return []
res = [0 for i in range(len(temperatures))]
stack = []
for ind, temp in enumerate(temperatures):
    while stack:
        fromStack = stack.pop()
        if temp <= fromStack[1]:
            stack.append((ind, temp))
            break
        else:
            res[ind] = ind - fromStack[0]






"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        res = [0 for i in range(len(temperatures))]
        stack = [] #keep indices and temperature
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackInd, stackT = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((i, t))
        return res
        
        return res
        


