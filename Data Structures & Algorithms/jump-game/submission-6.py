class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]* n
        dp[n-1] = True
        last = n-1
        for i in range(n-2, -1, -1):
            if nums[i]>=(last-i):
                dp[i] = True
                last = i
        return dp[0]


       