"""
Understand:
Return the shortest substring in s such that every character in t is included
Input: str s, str t and Output str
Constaints: Duplicates in t should also be present in s
Edge cases: Empty t, empty s, t longer than s, s duplicate elements alone, t duplicate elements too.

Match:
This is similar to Longest Repeating Character or something
We need to keep track of a window efficienty, expand until we get the characters we need, shrink it until we only have what we need
Seems to me that if we have these subsequence, substring, subarray questions and we have two inputs, most of the time its sliding window and then if we just have one input, maybe DP
Plan:

        
        
        

        
    

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
        
            






        