"""
Understand:
Figure out if s2 contains a permutation of s1.
Return true if it exists and return false otherwise
Edge cases:
if len(s1) > len(s2):
    return false
if not s1:
    return true

Plan:
Count the occurence of each character in s1 and maintain the count
Maintain a sliding window of len(s1) elements on s2 starting from the left.
let diff = number of characters in target that are not in currernt:
for r in range(len(s1), len(s2)):
    while diff:
        add 1 to occurence of s2[r]
        if this makes current[s2[r]] == target:
            diff -=1
        subtract 1 from occurence of s2[l] in current:
            if this makes that value less than target by 1, then 
            increment diff


note the number of target characters that are not in the window :2
while di



"""



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if len(s1) > len(s2):
            return False
        
        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1
        
        current = {}
        for i in range(len(s1)):
            current[s2[i]] = current.get(s2[i], 0) + 1

        diff = 0
        for key in target:
            if current.get(key, 0) < target[key]:
                diff += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if not diff:
                return True
            else:
                newChar = s2[r]
                current[newChar] = current.get(newChar, 0) + 1
                if current[newChar] == target.get(newChar, 0):
                    diff -= 1

                oldChar = s2[l]
                current[oldChar] = current.get(oldChar, 0) - 1
                if current[oldChar] == target.get(oldChar, 0) - 1:
                    diff += 1
                l+=1
        return diff == 0



        