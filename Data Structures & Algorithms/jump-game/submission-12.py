"""
Understand:
Given an integer array with max jump lengths, return true if you can reach the end of the list
Input: List[int], Output: Bool
Edge cases: Empty List, One element, 

Match: 
Like Maximus subarray, we can use a greedy approach where we determine locally if we can reach the goal and make that for the global solution
DP Solution where we break down the prbolem into smaller problemes

Plan:
Decision Tree, the root is index 0. 
Node is the index
Decisions are the possible jump lenghts we can take at each index
The base case is when our current node = last index

So in our dp, we can have a dp for storing if we can reach the end from each index
Then our base case is the dp[lastindex] = True
Since the base case is the last, then we do bottom up





"""

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         dp = [False] * len(nums)
#         dp[len(nums) - 1] = True
#         for i in range(len(nums) - 2, -1, -1):
#             for j in range(nums[i]):
                # if not dp[i] and i + j <= n:
#                 dp[i] = dp[i+j+1]
#                 else:
#                     break
#         return

"""Then we have a greedy solution here"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if goal - i <= nums[i]:
                goal = i

        return True if goal == 0 else False

        


       

        