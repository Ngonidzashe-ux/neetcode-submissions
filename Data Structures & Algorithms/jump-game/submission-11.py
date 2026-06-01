"""
Understand:
- Input: nums, output = boolean
- If not nums, return True

Plan:
- Create a dp array, dp[n] to store the answer of whether I can reach to the end by starting from index i.
- Initialise with False and set True the last index.
- For each dp[i], find a step that allows reaching to the end. This means checking each possible step to see if where you land is True. If you find it, stop search.
     for j in range(len(nums[i])): 
        if not dp[i]:
            dp[i] = dp[i] or nums[i+j]
        else:
            break


"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[n] = dp[n-1] = True
        for i in range(n-2, -1, -1):
            for step in range(1, nums[i] + 1):
                if not dp[i] and i + step <= n:
                    dp[i] = dp[i+step] 
                else:
                    break
        print(dp)
        return dp[0]


        