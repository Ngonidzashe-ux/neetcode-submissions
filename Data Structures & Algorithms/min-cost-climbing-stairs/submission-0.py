class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]* (n+1)
        for i in range(n-1, -1, -1):
            if (i + 2) < len(dp):
                dp[i] = min(cost[i]+dp[i+1], cost[i]+dp[i+2])
            else:
                dp[i] = cost[i]+dp[i+1]
        return min(dp[0], dp[1])