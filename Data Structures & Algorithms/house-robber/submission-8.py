"""
Understand:
1. Max amount that can be robbed while avoiding robbing adjacent houses
2. Bottom up approach: Start at the end houses and make your way to the beginning
3. dp[i] is the maximum amount that can be robbed starting from house i until the end of the house
4. Then go back to the beginning


"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[n-1] = nums[-1]
        for i in range(n-2, -1, -1):
            if i + 2 > (n-1):
                dp[i] = max(nums[i], dp[i+1])
            else:
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return max(dp[0], dp[1])
        