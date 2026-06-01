
"""
Understand:
- Look for a subarray that has the max sum and return the sum
- Input = array and output = int
- 2 pointers keeping track of the window
- maxSum and CurSum
- If we add a number that results in a negative, we restart the window by getting onto the next one

Plan:
- l = 0
- maxSum, curSum = 0, 0
- for r in range(len(nums)):
    curSum += nums[r]
- If curSum < 0:
    curSum = 0
    l = r
    maxSum = max(curSum, maxSum)

maxSum = nums[0] so that if its one number, we get that back
curSum = 0 because we want to start with a clean slate at the beginning and its really 0 at the start

For each number you are on, check if the cursum is negative
If negative, then reset curSum and then add that number
If not just add the number to the current sum

Greedy means making the locally optimum decision
This algorithm is greedy because it assumes starting with a 0 cursum is better than continuing with a negative sum and therefore the locally optimum decision would be to take 0.


"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub

        