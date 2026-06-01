"""
Understand:
Given different coin denominations, return the fewest coins to make the target amount
Input: List[int], output = int
Constraints: No need to use all the coins, can use the same coin multiple times
Edge Cases: Empty coin array, One coin, Positive and Negative coins, same coin denomination throughout

Match:
This is similar to other dp problems?

Plan.
Decision Tree. Current root = current choice of the coins, decision branch is choosing any of the coins leaf is if the total sum of coins = the amount
Base case is when sum = amount but we are gonna make it that it means for dp[0], the fewest coins we need is 0
So we have a dp array, that is of length amount + 1. Values all default to amount + 1 too
Then base case is when total = 12 just means that the fewest coins we need to get to amount 
DP:
Then for each index or amount right, for each coin, if amount >= coin: dp[amount] = 1 + dp[coin - amount]
return the value of the index of 12

"""



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for amt in range(amount + 1):
            for c in coins:
                if amt >= c:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
        return dp[amount] if dp[amount] < (amount + 1) else -1
        
        