class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp= [float("inf")]*(amount + 1)
        dp[0] = 0
        print(dp)
        for i in range(1, len(dp)):
            for j in coins:
                if i-j>=0:
                    temp = 1 +dp[i-j]
                    if temp<dp[i]:
                        dp[i] = temp
        return -1 if dp[amount] == float("inf") else dp[amount]

                




        


