"""
Understand:
Given an array of numbers, return the longest consecutive sequence that can be formed from the array elements
Input: array of numbers, retturn an int
Constraints: O(n)
Edge Cases: nums=[], mix of negative and positive numbers


Match:
- There is need for efficient lookup, so anything that uses a set
- Its an array question so it has to be array manipulation

Plan:
if not lists:
    return 0
mySet = set()
res = 0
for num in nums:
    length = 1
    while num - 1 in mySet:
        length+=1
    res= max(length, res)
return res

"""



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num -  1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length+=1
                longest = max(length, longest)
        return longest
        