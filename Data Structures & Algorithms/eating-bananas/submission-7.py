"""
Understand:
Determine the minimum eating rate k such that you finish all bananas in the given h hours
Minimum k = 1 and maximum K = max(piles)
Plan:
    k can be anywhere on those extremes so we can use binary search to serach for the valid k such that the time needed is less than h

"""


class Solution:
    def eatingTime(self, piles, k):
        time = 0
        for bananas in piles:
            time += bananas // k
            if bananas % k != 0:
                time+=1
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            k = l + (r - l) // 2
            time = self.eatingTime(piles, k)
            if time <= h:
                r = k - 1
                minK = min(minK, k)
            else:
                l = k + 1
        return minK


            



        