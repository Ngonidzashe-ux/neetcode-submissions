"""
Understand:
Have two pointers, buy and sell where buy is always behind the sell
Keep track of the maxProfit
If we currently have a loss, sell is smaller than buy, then move the buy to sell and sell one step furhter
If we have a profit curretnly, then just move the sell to see if there is more profit. Update the maxProfit
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return maxProfit


        