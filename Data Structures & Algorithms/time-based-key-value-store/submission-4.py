"""
Understand:

Plan

Lets have something like this

"""

class TimeMap:

    """
    valueStore = defaultdict(list)
    timeStore = defaultdict(list)
    """
    def __init__(self):
        self.valueStore = defaultdict(list)
        self.timeStore = defaultdict(list)
        
    """
    1. Append the value to valueStore[key]
    2. Append the timestamp to timeStore[key]
    """
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.valueStore[key].append(value)
        self.timeStore[key].append(timestamp)
        

    """
    1. Get the timeStore[key] to get all the timestamps
    2. Find the timestamp in there such that <= timestamp
    3. Determine its index
    4. Return the value at that index in the value store or "" if not in there.
    5
    """
    def get(self, key: str, timestamp: int) -> str:
        if not key:
            return ""
        times = self.timeStore[key]
        l, r = 0, len(times) - 1
        index = len(times)
        while l <= r:
            mid = (l + r) // 2
            if times[mid] > timestamp:
                r = mid - 1
            else:
                index = mid
                l = mid + 1
        if index == len(times):
            return ""
        return self.valueStore[key][index]
                

        

        
