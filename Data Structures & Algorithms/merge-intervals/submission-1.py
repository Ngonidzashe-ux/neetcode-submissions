"""
Understand: Given an array of intervals, merge any overlapping interval and return an array of intervals with no overlap
Input: Array of arrays
Ouput: Array of arrays
Edge Cases: None
Constraints: Common point is overlap

Match. This is similar to insert intervals. Instead of checking overlap between newinterval and 
current interval, we need to check overlap between current interval and the previous.

Plan.
if not intervals:
    return []
output = intervals[0]
for each interval from i=1 to the end:
    check for overlap with whats in the output.
    if there is overlap, combine and update the last value in output
    if not, then just append current interval
return output


"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1] = [ min(output[-1][0], intervals[i][0]),
                            max(output[-1][1], intervals[i][1])] 
            else:
                output.append(intervals[i])
        return output

        