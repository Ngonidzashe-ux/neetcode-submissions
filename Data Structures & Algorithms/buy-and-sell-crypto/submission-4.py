"""
Understand:
Choose two pointers r and l such that prices[r] - prices[l] is the maximum.
Return that maximum or 0
if prices <= 1:
    give us 0


Plan:
Initialise two pointers, l, r = 0, 1
While r is not at the end:
    Compute prices[r] - prices[l] 
    If that difference is greater than 0:
        Potentially update our maxProfit
    Then, if price[r] is smaller than our price[l],
        l=r
        update r
    else:
        just update r

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        maxProfit = 0
        l = 0
        for r in range(1, n):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
            if prices[r] < prices[l]:
                l = r
        return maxProfit

        