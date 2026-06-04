"""
Understand:
Given an array called nums, return the length of the longest consecutive sequence of elements that can be formed.
Edge case: Empty nums.

Constraints:


Match:
First of its kind
max_count = 1
Plan:
    for each element:
        initialise count = 1
        element -= 1
        while element in set:
            count+=
            element -=1
        add the original element in the set
        max_count = max(max_count, count)

    return max_count

    need to make sure that we dont modify the element in the numbs
        
        


"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxCount = 0
        count = 0
        numSet = set(nums)
        for i in range(len(nums)):
            count, num = 1, nums[i]
            num -=1
            while num in numSet:
                count += 1
                num -= 1
            maxCount = max(maxCount, count)
        return maxCount


        