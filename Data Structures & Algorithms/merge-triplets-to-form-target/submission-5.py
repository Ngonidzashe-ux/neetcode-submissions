"""
Understand:
- Given a 2d array containing triplets and a target triplet, return true if we can apply an operation 0 or more times to a triplet to get the target triplet
Input: 2D Array of triplets, target triplet, return True/False
Edge cases: Empty triplets and target is emtpy = True
Emptry triplets = false
Empty target = False
Constraints = ONly numbers involved

Plan:
if not triplets and not target:
    return True
if not triplets:
    return False
if not target:
    return False
for each triplet:
    take every triplet in front of it
    for each position:
        do the operation
        if the result is not the same as the the target:
            stop immediately, that is true
    if here, return True

Its too abstract, I cant think of how I can 
"""

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if not triplets and not target:
            return True
        if not triplets:
            return False
        if not target:
            return False
        if len(triplets) == 1:
            return True if triplets[0] == target else False
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for pos in range(len(t)):
                if t[pos] == target[pos]:
                    good.add(pos)
        return len(good) == 3
