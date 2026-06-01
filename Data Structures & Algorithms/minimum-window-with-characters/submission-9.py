"""
Refined UMPIRE
Understand
Find shortest substring of s containing all characters in t (including duplicates).
Input: s: str, t: str, Output: str.
Edge cases: empty s, empty t, len(t) > len(s), t not in s, duplicates in t.
Constraints: lowercase letters, 0 ≤ len(s), len(t) ≤ 10^5.
Intuition: Slide a window to include all t characters, shrink to minimize.
Match
Like Longest Substring with At Most K Distinct Characters: Frequency-based sliding window.
Like Character Replacement: Tracks frequencies in a window (your previous question).
Pattern: Sliding window with frequency tracking for validity.
Plan
Decision Analogy: Expand window to include t’s characters, shrink to minimize while keeping all required frequencies.
Build countT for t’s frequencies, set required = len(countT).
Use countS for window frequencies, track have (characters with matching frequencies).
For each r:
Add s[r] to countS, increment have if frequency matches countT.
While have == required, update result if shorter, shrink by removing s[l] from countS, update have, increment l.
Return shortest valid substring or "".
Intuition Example: s="ADOBECODEBANC", t="ABC": Window [A,D,O,B,E,C] shrinks to [B,A,N,C].

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        countT = {}
        countS = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        required = len(countT)  # Number of unique characters in t
        l, have, res, resLength = 0, 0, "", float("inf")
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0) + 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            while have == required:
                if r - l + 1 < resLength:
                    resLength = r - l + 1
                    res = s[l:r+1]
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return res