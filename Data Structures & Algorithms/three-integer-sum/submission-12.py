
"""
1. Understand
Return any distinct triplets that sum up to one.
Input: list and output is list of lists
Edge cases: nothing since the nums list start from 3

2. Plan
for each num a in nums:
    find the other two nums b, c such that b + c = -a. Use two pointers to find b and c

To ensure no duplicates and improve the two pointer approach, sort the numbers before hand

nums.sort()
for each num in nums:
    if num != prev:
        initialise two pointers l, r with l be elemnt to the right of num and then r the last
        if current sum is big, advance left, if small advance left. if exact, then add that to the output

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if (i > 0):
                if nums[i] == nums[i-1]:
                    continue
            target = -1 * nums[i]
            l, r = i+1, len(nums) - 1
            while (l < r):
                if (nums[l] + nums[r] > target):
                    r-=1
                elif (nums[l] + nums[r] < target):
                    l+=1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while (l < r and nums[l] == nums[l-1]):
                        l+=1
                    while (l < r and nums[r] == nums[r+1]):
                        r-=1

        return output
        