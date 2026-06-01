class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(n-1, -1, -1):
            if i == (n-1):
                dp[i] = nums[i] + dp[i+2]
            else:
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]
        