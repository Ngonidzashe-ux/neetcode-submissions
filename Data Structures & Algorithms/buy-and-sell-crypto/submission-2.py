class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
        while l<r and r<len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                curProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit , curProfit)
            r+=1
        return maxProfit
       
