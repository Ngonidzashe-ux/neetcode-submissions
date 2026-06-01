class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = 0
        largestsum = nums[0]
        for i in nums:
            currentsum += i
            largestsum = max(largestsum, currentsum)
            if currentsum < 0:
                currentsum = 0

        return largestsum
            
        