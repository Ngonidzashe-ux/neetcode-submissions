"""
Understand:
Given an array of intervals, find the minimum number of intervals that we can remove to remain with non overlapping array
Input= Array
Output = int
No edge cases

1. Match
This is similar to the previous merge overlapping intervals. We should greedily choose 
smaller duration or quick to finish jobs first, in that way we minimise the overlap.
Choosing a large interval, we maximise the overlapp, so we want to choose smallest.

Plan.
Sort by finish time
Keep track of a prev variable that tracks the last admitted interval
Every time there is a merge or we have to merge, we increment a counter by one


"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1]))
        minIntervals = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start >= prevEnd:
                prevEnd = end
            else:
                minIntervals += 1
        return minIntervals

