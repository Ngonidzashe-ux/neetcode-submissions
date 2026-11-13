"""
Understand:
Given two strings, s and t, return the shortest substring in s that contains every character in t including duplicates.
This seems like the permutation problem but with a variable window


Plan:
    if length of s or length of t is equal to 0:
        return ""
    if length of t > length of s:
        return ""
    
    minString = s
    minLength = len(s) + 1
    l = 0

    target = Counter(t)
    window = Counter(s[:len(t)])

    diff = 0
    for key in target:
        if window.get(key, 0) >= target[key]:
            diff+=1
    if not diff:
        return s[:len(t)] 
    for r in range(len(t), len(s)):
        if diff > 0:
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] == target.get(s[r], 0):
                diff -=1
            while diff == 0:
                if (r - l + 1) < minLength:
                    minString = s[l:r+1]
                    minLength = r - l + 1
                l+=1
                window[s[l]] = window.get(s[l], 0) - 1
                if window[s[l]] == target.get(s[l], 0) - 1:
                    diff+=1
                


    If we dont have enough of the target characters, expand the window to the right:
    if we have enough of the target characters:
        while we have them:
            shrink the window
            if this is the smallest window we have seen:
                update the minString
                
    
    if minLength == len(s) + 1:
        return ""
    else:
        return minString


"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not len(s) or not len(t):
            return ""
        if len(t) > len(s):
            return ""
        
        minString = s
        minLength = len(s) + 1

        target = Counter(t)
        window = Counter(s[:len(t)])

        diff = 0
        for key in target:
            if window.get(key, 0) < target[key]:
                diff+=1
                
        if not diff:
            return s[:len(t)] 
        
        print(target)
        print(window)
        print(minString)
        print(minLength)
        print(diff)
        l=0
        for r in range(len(t), len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] == target.get(s[r], 0):
                diff -=1
            while diff == 0:
                if (r - l + 1) < minLength:
                    minString = s[l:r+1]
                    minLength = r - l + 1

                window[s[l]] = window.get(s[l], 0) - 1
                if window[s[l]] == target.get(s[l], 0) - 1:
                    diff+=1
                l+=1
                    

        
        if minLength == len(s) + 1:
            return ""
        else:
            return minString

        