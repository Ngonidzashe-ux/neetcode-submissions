"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Understand: To find the maximum number of meetings occuring at the same time.
Input: intervals
Output an integer.
Constraints: Can be empty
Match: This is similar to overlapping intervals, but we are not merging them, we just need to track how many 
meetings are overlapping at the same time and this is the minimum number of rooms we need.
Plan:
if not intervals:
    return 0
numRooms = 0
maxRooms = 0
starts = [i.start for i in intervals]
ends = [i.end for i in intervals]
start, end = 0, 0
while start < len(starts):
    if starts[start] < ends[end]:
        numRooms += 1
        start+=1
    elif starts[start] > ends[end]:
        numRooms -= 1
        ends+=1
    else:
        start+=1
        ends+=1
    maxRooms = max(maxRooms, numRooms)
return maxRooms





"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        numRooms = 0
        maxRooms = 0
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()
        start, end = 0, 0
        while start < len(starts):
            if starts[start] < ends[end]:
                numRooms += 1
                start+=1
            elif starts[start] > ends[end]:
                numRooms -= 1
                end+=1
            else:
                start+=1
                end+=1
            maxRooms = max(maxRooms, numRooms)
        return maxRooms
        