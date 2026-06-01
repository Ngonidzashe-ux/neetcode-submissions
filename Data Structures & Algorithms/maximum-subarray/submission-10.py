
"""
Given an array of integers (positive/negative, -1000 to 1000), return the maximum sum of any contiguous subarray. Input: List[int], Output: int. 
Edge cases: nums = [], nums = [1], all negative, all zeros.

Like Maximum Product Subarray (dynamic programming for subarray optimization) or Maximum Sum Circular Subarray. Kadane’s algorithm is ideal for finding the
 maximum subarray sum in O(n) by tracking local/global sums.

Plan: 1. If nums is empty, return 0. 2. Initialize 
res = nums[0], curSum = nums[0]. 3. For each num in 
nums[1:], set curSum = max(num, curSum + num), update
 res = max(res, curSum). 4. Return res.”
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            res = max(res, curSum)
        return res

      