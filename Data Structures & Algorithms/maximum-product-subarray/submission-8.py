"""
Understand:
-Given an integer array of nums, find a subarray with the largest product and return the product
-Input = List[int] and output = int
-Edge cases = nums = [], nums[All negative], nums[mixture of positive and negative]

Match:
- Like the maximum sub array problem that uses kadane's algorithm, I need to track contigous sequence of elements
- Instead of keeping track of the cursum, I will keep track of the current max and min product of a subarry

Plan:
- For num in nums:
    maxProd = max(maxProd * num, minProd * num, 1)
    minProd = min(maxProd * num, minProd * num, num)
    res = max(minProd, maxProd)

"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        minProd, maxProd = 1, 1
        for num in nums:
            temp = maxProd
            maxProd = max(maxProd * num, minProd * num, num)
            minProd = min(temp * num, minProd * num, num)
            res = max(res, maxProd)
        return res


      