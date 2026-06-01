class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        curr = 0
        for i in range(len(nums)):
            curr = curr + nums[i]
            if curr < 0:
                curr = 0
            else:
                maxSum = max(maxSum, curr)
        return maxSum
        