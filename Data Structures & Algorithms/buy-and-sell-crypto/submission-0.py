class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 #buying
        R = 1 #selling
        max_profit = 0
        while R < len(prices):
            if prices[R] > prices[L]:
                max_profit = max(max_profit, prices[R] - prices[L])
            else:
                L=R
            R+=1
            
        return max_profit
        