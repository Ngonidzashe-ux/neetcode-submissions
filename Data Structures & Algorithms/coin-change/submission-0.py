class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Initialize the dp array with amount+1 slots so that we have the indices which run from 0 to amount.
        #The array is initialized with the maximum value which is amount +1
        #if the target amount is 7
        #We have an array of 8 entries
        #These entries are initialized with the value 8 
        dp = [amount + 1] * (amount +1)

#This is our base case and we put it in
        dp[0] = 0
#We want to do this in reverse order such that we start by finding the minimum number of coins for needed to get 1, 2,... up to the amount
        for a in range(1, amount+1):
            #We are still doing it in the brute force way so we are gonna go through every single coin
            for coin in coins:
                #We are trying to compute the a amount using the coins we have
                #Lets say our coin array is like this: [1,4,6,7]
                #If the current coin is 4 and we are trying to compute the amount 10.
                #First of all we need to check if the coin is less than the amount and we can do that by checking if amount - coin or 10-4 is positive
                if a - coin >= 0:
                    #If its positive, then we would like to take that 1 coin of value 4 +  the minimum number of coins needed for the remaining target in this case dp[10-4] or dp[6]
                    #But we need to take the min between that result and the exisiting dp[a]
                    dp[a] = min(dp[a], 1+dp[a-coin])
        #return this only if the dp[amount] is not the default value we have set at the beginning which is amount + 1. If its default value showing that we did not end up finding any combination of coins, then we return -1 to say we havent found it.
        return dp[amount] if dp[amount] != amount+1 else -1


