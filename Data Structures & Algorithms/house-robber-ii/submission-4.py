class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            n = len(nums)
            dp = [0]* (n+1)
            for i in range(n-1, -1, -1):
                if i+2 < len(dp):
                    dp[i] = max((nums[i] + dp[i+2]), dp[i+1])
                else:
                    dp[i]= nums[i]
            return dp[0]
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

        
        