class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) #Number of items to be dealt with
        dp = [1] * (n+1) #Include a spot for the base case
        dp[n] = 0 #LIS for nothing is 0

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])               
        return max(dp)



        