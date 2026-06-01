""""
Understand:
- Data structure that stores key value pairs at specific time stamps and the key might be repeated multiple times
- Edge cases. Repeat of the keys, getting a key never inputted

Match?

Plan:
init
dataHashmap = {key: [value1, value2, ..]}
timeHashmap = {key: [timestamp1, timestamp2..]}

set.
Locate the key and append the valuees of the data and timestamp

get
Check if the key is there, if not retrun ""
If yes, return the last value of the data and then do binary search on the time stamp
"""

from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.keyStore = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.keyStore:
            return res
        values = self.keyStore[key]
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][-1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

        
