class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp1 = [0] * (n+1)
        for i in range(n-1, 0, -1):
            if i == (n-1):
                dp[i] = nums[i]
            else:
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        for i in range(n-2, -1, -1):
            if i == (n-2):
                dp1[i] = nums[i]
            else:
                dp1[i] = max(nums[i] + dp1[i+2], dp1[i+1])
        return max(dp1[0], dp[1], nums[0])
        