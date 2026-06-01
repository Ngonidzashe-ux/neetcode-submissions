"""
UMPIRE
1. Understand. Given an a new interval, add it to the existing interval list and ensure no overlapping intervals exists
Input = Array and an interval
Output = Array
Base Case. return empty list if there is no intervals
2. Match. This is like insert intervals
3. Plan
output = []
for each interval in the intervals:
    if interval finishes first with no overlapping with newinterval, then add interval
    if it starts after the newinterval finishes, then add new interval in and then just add the rest and return
    else there is overlap and we need to merge
    so update the new interval with so that its one big new interval

add the new interval 
return the output
4. Implement

"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and not newInterval:
            return []
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        output = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if end < newInterval[0]:
                output.append(intervals[i])
            elif newInterval[1] < start:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval = [min(start, newInterval[0]),  max(end, newInterval[1])]
        output.append(newInterval)
        return output


        

        