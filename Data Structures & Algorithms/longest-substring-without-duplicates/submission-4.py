"""
Understand:
Input = string
Return = int 
Find any contiguous set of characters that start any where and and end anywhere and do not have duplicates within them. Then give us the length
if length of input = 0, then return 0

Plan:
if length of s = 0, return 0
start with two pointers at the beginning character
Record that character into a set
increment the right pointer. 
Check if the new character is in the set.
if it is, then we have to start a new sliding window and we do that by increment the left pointer till we remove the duplicate character
if it is not, then increment the current sliding window.


Plan 2:
if length of s = 0:
    return 0

longest = 0
let l = 0 #Initialise our starting sliding window
windowSet = myset #Keep track of the elements in our current window
for r in range(len(s)):
    char = s[r]
    if char not in windowSet:
        windowSet.add(char)
        longest = max(longest, r - l + 1)
    else:
        while char in windowSet:
            windowSet.remove(s[l])
            l+=1



"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, longest = 0, 0
        windowSet = set()
        for r in range(len(s)):
            char = s[r]
            if char not in windowSet:
                windowSet.add(char)
                longest = max(longest, r - l + 1)
            else:
                while char in windowSet:
                    windowSet.remove(s[l])
                    l+=1
                windowSet.add(char)
        return longest

        