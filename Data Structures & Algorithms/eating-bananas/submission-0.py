"""
Understand:
Given an array of integers called piles, and an integer h for number of hours to eat all bananas return the minimum rate k to eat all bananas
Input: List[int], h. Output = k
Constraints: If you finish the bananas before hour is over, you can't eat from another pile


Match:
Like a binary search we want to find the target k within a short period of time byy halving the search space each time.

Plan:
Find the max number of bananas and that becomes the max of our seach range
Find the mid point and calculate the total hours using that range
If the total hours is more, then we have to increase our rate
If its less, we try to find the minimim plausible rate

maxBananas = max(piles)
l, r = 0, maxBananas
k = h
while l <= r:
    mid = (l + r) // 2
    hours = 0
    for pile in piles:
        hours += ceil(pile / k)
    
    if hours <= h:
        k = min(k, mid)
        r = mid - 1
    else:
        l = mid + 1
return k

"""



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = max(piles)
        l, r = 1, maxBananas
        k = maxBananas
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return k
        