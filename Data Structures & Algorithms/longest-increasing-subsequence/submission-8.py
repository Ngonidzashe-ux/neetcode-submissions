
"""
Understand:
Given an array of numbers, return the longest strictly increasing subsequence
Input: List[int], output = int
Edge cases: Single element, empty nums, one element repeated multiple times

Match:
This is similar to coin change in that we can break down the problem into subproblem and solve them.
The subproblem here is what is the LIS starting from each index. The base case would be the last element though because is 1.

Plan:
Firstly, of course this is a decision tree in nature
Current choice = the subsequence thus far
Branch is the subsequence formed by considering each index as the start
So each number is a node, right at the beginning
Then if any number on the right is bigger, creatign tthe branch as a child
Until you are done. Then return the longest path/.
We only stop if there is no number on the right that is greater than the curretn node.

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
        