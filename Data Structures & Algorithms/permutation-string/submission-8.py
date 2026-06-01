"""
Understand:
- Return true if s2 contains a permutation of s1 and false otherwise
- Input: str, str, output = bool
- Constraints: lowercase letters only
- Edge cases: empty strings, same letters, s1 longer than s2


Match: 
Like Minimum Window Substring, we want to find the smallest window containing
all the s1 characters in exactly the same frequencies, without extra characters

Plan.
expand until we get everything we need, then contract. We need to make sure we only have the s1 characters though


if not s1:
    return True
if len(s1) > len(s2):
    return False
countS1, window = {}, {}
have, required, l = 0, 0, 0
for c in s1:
    countS1[c] = 1 + countS1.get(c, 0) + 1
required = len(countS1)

for r in range(len(s2)):
    window[s2[r]] = 1 + window.get(s2[r], 0)
    if window[s2[r]] >= countS1.get(s2[r], 0):
        have += 1
    if have == required:
        return true
    while have > required:

    


"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True
        if len(s1) > len(s2) or not s2:
            return False
        countS1, window = {}, {}
        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1
        required = len(countS1)
        have, l = 0, 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if s2[r] in countS1 and window[s2[r]] == countS1[s2[r]]:
                have += 1
            while r - l + 1 == len(s1):
                if have == required:
                    return True
                if s2[l] in countS1 and window[s2[l]] == countS1[s2[l]]:
                    have -= 1
                window[s2[l]] -= 1
                l += 1
        return False

   

        