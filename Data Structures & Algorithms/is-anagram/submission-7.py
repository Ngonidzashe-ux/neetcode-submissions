"""
Understand:
Return true or false
edge cases: if they are not the same length, they are not anagrams

Plan:
sort both and compare if they are equal

create a hashmap that has the the counts for each character for s and do the same for t, then go through one hashmap comparing the value of each key with the other hashmap.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap, tMap = {}, {}
        for char in s:
            sMap[char] = sMap.get(char, 0) + 1
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        for char in sMap:
            if sMap[char] != tMap.get(char, 0):
                return False
        return True