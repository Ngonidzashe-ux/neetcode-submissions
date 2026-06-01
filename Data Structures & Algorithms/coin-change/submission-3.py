"""
Understand:
- Find the fewest number of coins that make up a certain amount


Plan:
- Have dp[i] that stores the min amount of coins to make up i amount
- Initialise dp[i] to amount + 1
- For each value i, iterate through each coin
- if i >= coin, then we update the current dp[i] with a min between itself or the 1 + dp[remainder]

"""



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for amt in range(amount + 1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
            
        return dp[amount] if dp[amount] != amount + 1 else -1

        
        