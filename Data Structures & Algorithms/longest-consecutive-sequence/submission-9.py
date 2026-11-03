"""
Understand.
The longest consecutive sequence.
For each element, say the longest consecutive sequence ends here and therfore its lenght one.
Then increment that lenght as long as element-- is in a set. then after done, add element to the set and do the same thing for each elemtn

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mySet = set(nums)
        maxLength = 1
        for num in nums:
            length = 0
            if num+1 not in mySet:
                while num in mySet:
                    length += 1
                    num -= 1
                    maxLength = max(maxLength, length) 
        return maxLength 
        