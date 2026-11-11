"""
Understand:
Replace  k characters with one upper case english character in a way that gives us the longest substring that contains one disctinct character:
Return the length and not the substring
if s = 0, then return the 0


Plan:
The general idea would be to mantain a sliding window such that there is only k different characters.


if not s:
    return 0
let l = 0 #beginning of the slding window
let maxLength = 0 #current maxLength of the window
charSet = set() #track the characters in the sliding window

maintain a sliding window
track the number of each type of element in that window while keeping the maximum one
if the window - max elemnt > k:
    reset the window by moving the left pointer till we are good.
if its not, keep enlarging the window
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        l, maxLength = 0, 0
        maxDict = {}
        maxOccuring = 0
        for r in range(len(s)):
            char = s[r]
            maxDict[char] = maxDict.get(char, 0) + 1
            maxOccuring = max(maxDict[char], maxOccuring)
            while ((r - l + 1) - maxOccuring > k):
                maxDict[s[l]]-=1
                l+=1

            maxLength = max(r - l + 1, maxLength)
        return maxLength

        