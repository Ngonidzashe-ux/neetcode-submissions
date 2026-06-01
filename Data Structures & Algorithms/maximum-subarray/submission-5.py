class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        for i in range(n-1, -1, -1):
            if i != (n-1):
                dp[i] = max(nums[i], nums[i]+dp[i+1])
            else:
                dp[i] = nums[i]

        print(dp)
        return max(dp)


        