class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]* (n+1)
        dp[n] = 1
        dp[n-1] = 1
        for i in range(n-2, -1, -1):
            dp[i] = dp[i+2] + dp[i+1]
        return dp[0]





        