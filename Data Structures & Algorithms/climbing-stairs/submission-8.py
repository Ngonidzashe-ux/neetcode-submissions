"""
Understand:
1. Bottom-up approach where you start from the target

Plan:
1. Initialise a dp array that has n spaces
2. Initialise the last index with 1 because thats the number of ways to get there
3. Then for each position, going back, its number of ways to get to the next and the next next
4. Then return the dp[0]


"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[n] = dp[n-1] = 1
        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        return dp[0]
        