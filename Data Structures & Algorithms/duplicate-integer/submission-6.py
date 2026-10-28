
"""
Understand:
- Empty array is the edge cases here

Plan
- For each number, if its in the set, return we have a duplicate, if its not, then add it into the set. Return false at the end

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False
        