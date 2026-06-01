class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            dp = [0] * (len(nums) + 1)
            for i in range(len(nums)-1, -1, -1):
                if i == len(nums) - 1:
                    dp[i] = nums[i]
                else:
                    dp[i] = max(nums[i] + dp[i+2], dp[i+1])
            return dp[0]
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
            
            
        