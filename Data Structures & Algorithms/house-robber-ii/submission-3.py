class Solution:
    
    def rob(self, nums: List[int]) -> int:
      
        def helper( nums):
            n = len(nums)
            if not n:
                return 0
            dp= [0] * (n+1)
            dp[n-1] = nums[n-1]
            for i in range(n-2, -1, -1):
                dp[i] = max(nums[i]+dp[i+2], dp[i+1])
            return dp[0]
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))





        